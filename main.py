from discord.ext import commands
import discord
from datetime import datetime
import json


token = "Place your account bot token here"


bot = commands.Bot(command_prefix="!", self_bot=True)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready")


@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"Hey {ctx.author.mention}! This is a prefix command")


@bot.command(name="say")
async def say(ctx, *, arg: str):
    await ctx.send(f"{ctx.author.name} said: `{arg}`")


@bot.command(name="addrole")
async def addrole(ctx, member: discord.Member, role: discord.Role):
    if not ctx.author.guild_permissions.manage_roles:
        return await ctx.send("No permission")
    try:
        await member.add_roles(role)
        await ctx.send(f"Added {role.name} to {member.mention}")
    except discord.Forbidden:
        await ctx.send("Bot lacks permission")


@bot.command(name="remove_role")
async def removerole(ctx, member: discord.Member, role: discord.Role):
    if not ctx.author.guild_permissions.manage_roles:
        return await ctx.send("No permission")
    try:
        await member.remove_roles(role)
        await ctx.send(f"Removed {role.name} from {member.mention}")
    except discord.Forbidden:
        await ctx.send("I don't have permission to remove this role")
    except Exception as e:
        await ctx.send(f"Error: -[{e}]")


@bot.command(name="messagehistory")
async def message_history(ctx, member: discord.Member, limit: int):
    if not ctx.author.guild_permissions.read_message_history:
        await ctx.send("No permission.")
        return
    channel = ctx.channel
    records = []
    async for msg in channel.history(limit=limit):
        if msg.author == member:
            content = msg.content if msg.content else "[No Text]"
            timestamp = msg.created_at.strftime("%Y-%m-%d %H:%M:%S")
            records.append(f"```[{timestamp}]{member}:{content}```")
    if not records:
        await ctx.send(f"No messages found from {member.id}")
        return
    records.reverse()
    output = "\n".join(records)
    await ctx.send(output[:1900])


@bot.command(name="create_text_channel")
async def create_text_channel(ctx, name: str):
    if not ctx.author.guild_permissions.manage_channels:
        await ctx.send(f"You don't have the permission to execute this command {ctx.author.mention}")
        return
    try:
        channel = await ctx.guild.create_text_channel(name=name)
        await ctx.send(f"Created channel : {channel.mention}")
    except discord.Forbidden:
        await ctx.send("Bot lacks the permission")


@bot.command(name="create_voice_channel")
async def create_voice_channel(ctx, name: str):
    if not ctx.author.guild_permissions.manage_channels:
        return await ctx.send(f"{ctx.author.mention} You don't have permission to use this")
    if not ctx.guild.me.guild_permissions.manage_channels:
        return await ctx.send("I don't have permission to create channels.")
    try:
        lookup = discord.utils.get(ctx.guild.voice_channels, name=name)
        if lookup is None:
            channel = await ctx.guild.create_voice_channel(name=name)
            await ctx.send(f"Created voice channel: {channel.name}")
        else:
            await ctx.send(f"{name} already exists")
    except discord.Forbidden:
        await ctx.send("Bot lacks permission")


@bot.command(name="delete_channel")
async def delete_channel(ctx, name: str):
    if not ctx.author.guild_permissions.manage_channels:
        return await ctx.send(f"{ctx.author.mention} You don't have permission to execute this command")
    if not ctx.guild.me.guild_permissions.manage_channels:
        return await ctx.send("I don't have the permission to delete channels")
    channel = discord.utils.get(ctx.guild.channels, name=name)
    if channel is None:
        return await ctx.send(f"{name} Channel not found")
    try:
        await channel.delete()
        await ctx.send(f"Deleted channel: {name}")
    except discord.Forbidden:
        await ctx.send(f"I can't delete the channel {name}, role heirarchy issue")


@bot.command(name="my_perms")
async def my_perms(ctx,member:discord.Member):
    perms = member.guild_permissions
    output = ""
    for name, value in perms:
        if value:
            clean = name.replace("_", " ").title()
            output += f"{clean}\n"
    if output == "":
        output = "No permissions found"
    await ctx.send(output[:1900])


@bot.command(name="create_webhook")
async def create_webhook(ctx, name: str):
    if not ctx.author.guild_permissions.manage_webhooks:
        return await ctx.send("You need `Manage webhook` permission.")
    if not ctx.guild.me.guild_permissions.manage_webhooks:
        return await ctx.send("I don't have perms to manage webhooks")
    try:
        webhook = await ctx.channel.create_webhook(name=name)
        await ctx.send(f"Webhook created: `{webhook.name}` \n ```{webhook.url}```")
    except discord.Forbidden as f:
        await ctx.send(f"Failed to create a webhook {f}")


@bot.command(name="delete_webhook")
async def delete_webhook(ctx, name: str):
    if not ctx.author.guild_permissions.manage_webhooks:
        return await ctx.send("You need `Manage Webhooks` permission.")
    if not ctx.guild.me.guild_permissions.manage_webhooks:
        return await ctx.send("I don't have permission to manage webhooks.")
    try:
        webhooks = await ctx.channel.webhooks()
        matches = [wh for wh in webhooks if wh.name.lower() == name.lower()]
        if not matches:
            return await ctx.send(f"No webhook found with name: `{name}`")
        deleted = 0
        for wh in matches:
            try:
                await wh.delete()
                deleted += 1
            except:
                pass
        await ctx.send(f"Deleted {deleted} webhook(s) named `{name}`.")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.command(name="backup")
async def backup_channels(ctx):
    guild = ctx.guild
    backup_data = {
        "guild_name": guild.name,
        "backup_date": datetime.now().isoformat(),
        "categories": [],
        "loose_channels": []
    }
    for category in guild.categories:
        category_data = {
            "name": category.name,
            "position": category.position,
            "channels": []
        }
        for channel in category.channels:
            channel_data = {
                "name": channel.name,
                "type": str(channel.type),
                "position": channel.position
            }
            if isinstance(channel, discord.TextChannel):
                channel_data.update({
                    "topic": channel.topic,
                    "slowmode_delay": channel.slowmode_delay,
                    "nsfw": channel.nsfw
                })
            elif isinstance(channel, discord.VoiceChannel):
                channel_data.update({
                    "bitrate": channel.bitrate,
                    "user_limit": channel.user_limit
                })
                category_data["channels"].append(channel_data)
            backup_data["categories"].append(category_data)
    for channel in guild.channels:
        if channel.category is None and not isinstance(channel, discord.CategoryChannel):
            channel_data = {
                "name": channel.name,
                "type": str(channel.type),
                "position": channel.position
            }
            if isinstance(channel, discord.TextChannel):
                channel_data.update({
                    "topic": channel.topic,
                    "slowmode_delay": channel.slowmode_delay,
                    "nsfw": channel.nsfw
                })
            elif isinstance(channel, discord.VoiceChannel):
                channel_data.update({
                    "bitrate": channel.bitrate,
                    "user_limit": channel.user_limit
                })
            backup_data["loose_channels"].append(channel_data)
    filename = f"backup_{guild.id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(backup_data, f, indent=4, ensure_ascii=False)
    await ctx.send(
        f"Backup created successfully!\n"
        f" File: `{filename}`\n"
        f"Categories: {len(backup_data['categories'])}\n"
        f"Loose channels: {len(backup_data['loose_channels'])}",
        file=discord.File(filename)
    )


bot.run(token=token)
