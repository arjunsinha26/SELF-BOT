<div align="center">

# 🤖 Discord.py Utility Bot

### A beginner-friendly collection of prefix commands for common Discord server tasks

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/discord.py-Commands-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="discord.py">
  <img src="https://img.shields.io/badge/Commands-Prefix-2EA44F?style=for-the-badge" alt="Prefix commands">
  <img src="https://img.shields.io/badge/Backup-JSON-orange?style=for-the-badge&logo=json" alt="JSON backup">
</p>

<p>
  <a href="#-overview"><img src="https://img.shields.io/badge/Overview-5865F2?style=for-the-badge" alt="Overview"></a>
  <a href="#-commands"><img src="https://img.shields.io/badge/Commands-2EA44F?style=for-the-badge" alt="Commands"></a>
  <a href="#-installation"><img src="https://img.shields.io/badge/Installation-orange?style=for-the-badge" alt="Installation"></a>
  <a href="#-important-notes"><img src="https://img.shields.io/badge/Important%20Notes-red?style=for-the-badge" alt="Important notes"></a>
</p>

</div>

---

## 📌 Overview

This project is a `discord.py` bot that demonstrates prefix commands for everyday Discord server operations. It includes examples for role management, channel creation and deletion, permission inspection, webhook management, message-history lookup, and exporting a basic channel-structure backup to JSON.

> **Learning project:** This code is intended to help beginners get an idea of how `discord.py` commands and Discord server operations work. It is a starting point for experimentation, not a complete or production-ready administration bot.

## ✨ Features

- 👋 **Basic commands** — greet the command author and repeat supplied text.
- 🎭 **Role management** — add or remove a role from a member, with a basic permission check.
- 🧾 **Message history** — find recent messages by a selected member in the current channel.
- 🏗️ **Channel management** — create text or voice channels and delete a channel by name.
- 🔎 **Permission inspection** — display the enabled server permissions for a member.
- 🪝 **Webhook management** — create a webhook in the current channel or delete matching webhooks.
- 💾 **Channel backup** — export selected channel and category details to a JSON file and attach it to the command response.

## 🧭 Commands

The bot uses `!` as its prefix. Replace example values such as `@member`, `@role`, and `channel-name` with the appropriate Discord mentions or names.

| Command | Description | Example |
|---|---|---|
| `!hello` | Sends a greeting. | `!hello` |
| `!say <text>` | Repeats the text supplied after the command. | `!say Hello everyone` |
| `!addrole <member> <role>` | Attempts to assign a role. | `!addrole @Member @Role` |
| `!remove_role <member> <role>` | Attempts to remove a role. | `!remove_role @Member @Role` |
| `!messagehistory <member> <limit>` | Searches recent messages in the current channel. | `!messagehistory @Member 50` |
| `!create_text_channel <name>` | Creates a text channel. | `!create_text_channel announcements` |
| `!create_voice_channel <name>` | Creates a voice channel unless one with that name already exists. | `!create_voice_channel Gaming` |
| `!delete_channel <name>` | Deletes the first channel found with that name. | `!delete_channel old-channel` |
| `!my_perms <member>` | Lists enabled guild permissions for a member. | `!my_perms @Member` |
| `!create_webhook <name>` | Creates a webhook in the current channel. | `!create_webhook MyWebhook` |
| `!delete_webhook <name>` | Attempts to delete webhooks with the matching name in the current channel. | `!delete_webhook MyWebhook` |
| `!backup` | Creates and sends a JSON channel-structure backup. | `!backup` |

## 💾 What does `!backup` save?

The backup command creates a timestamped file similar to:

```text
backup_<guild_id>_<date_time>.json
```

The JSON structure includes:

- Server name and backup timestamp.
- Category names and positions.
- Channel names, types, and positions.
- Text-channel topic, slowmode delay, and NSFW setting.
- Voice-channel bitrate and user limit.
- Channels that are not inside a category.

**Important:** This is a basic structural backup, not a full server backup. It does not save messages, members, roles, permissions/overwrites, emojis, webhooks, or other server settings, and this script does not include a restore command.

## 🛠️ Installation

### 1. Install Python

Install a supported Python version, then check that Python and pip are available:

```bash
python --version
python -m pip --version
```

### 2. Install discord.py

```bash
python -m pip install -U discord.py
```

### 3. Create a bot application

1. Open the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create an application and add a bot.
3. Copy the bot token.
4. Invite the bot to a test server with the permissions required by the commands you want to try.

### 4. Configure the token

The provided code contains this placeholder:

```python
token = "Place your account bot token here"
```

Use a **bot token from your Discord application**, not your personal user-account token. Self-bots that automate normal user accounts are prohibited by Discord. This script uses `commands.Bot` and should be configured as a regular bot account.

For a safer setup, store the token in an environment variable rather than committing it to source control. If a token is exposed, reset it in the Developer Portal.

### 5. Run the bot

Save the script as `bot.py`, then run:

```bash
python bot.py
```

Use commands in a server where the bot is present. Prefix commands require the bot to receive message events; configure the required message intent in the Developer Portal and in code when needed.

## 🔐 Permissions

Depending on the command, the invoking member and the bot need suitable permissions:

- **Manage Roles** — add and remove roles.
- **Manage Channels** — create and delete channels.
- **Manage Webhooks** — create and delete webhooks.
- **View Channels** and **Read Message History** — inspect channel history.
- **Send Messages** and **Attach Files** — reply to commands and send the JSON backup.
- **Role hierarchy** — the bot's highest role must be above roles it assigns or removes.

A user's permission does not grant the bot the same permission automatically. Both should be checked, and the bot's role hierarchy can prevent an operation even when a permission appears enabled.

## ⚠️ Important Notes

- **Use a normal bot account.** Do not use a personal account token or self-bot configuration. The `self_bot=True` option is not supported by current standard `discord.py` usage; use `commands.Bot(command_prefix="!", intents=...)` with a bot token.
- **Enable message content intent** for prefix commands that need to read message content. Set `intents.message_content = True` in code and enable the privileged Message Content Intent for the bot in the Developer Portal, where required.
- **Backup logic needs review.** In the supplied code, `category_data` is appended to `backup_data["categories"]` inside the channel loop, so categories may be duplicated. Also, the `category_data["channels"].append(channel_data)` line is currently nested under the voice-channel branch, meaning text channels are not added to category channel lists. Review and correct this before relying on backups.
- **Validate inputs.** Set a sensible positive range for the message-history `limit`, and account for Discord message-length limits when displaying results.
- **Use caution with destructive commands.** `!delete_channel` deletes a channel by name. Test in a private server and consider confirmation prompts and more precise channel selection.
- **Improve error handling.** Some API errors besides `discord.Forbidden` can occur. Avoid broad bare `except` blocks where possible, and log errors for debugging.
- **Treat webhook URLs as secrets.** A webhook URL can allow someone to post through that webhook. Avoid publicly sharing it and consider deleting any webhook whose URL has been exposed.
- The code imports `json` and `datetime` for the backup feature. Keep the JSON file somewhere safe if you need it later.

## 🧠 Concepts to Explore Next

- Application commands (slash commands) with `app_commands`.
- Environment variables for token management.
- `commands.CheckFailure` and command error handlers.
- Confirmation prompts before destructive actions.
- Better channel selection using Discord's typed command converters.
- A more complete backup schema and a carefully tested restore workflow.

## 📚 Resources

- [discord.py documentation](https://discordpy.readthedocs.io/en/stable/)
- [discord.py commands extension](https://discordpy.readthedocs.io/en/stable/ext/commands/index.html)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Discord Developer Documentation](https://discord.com/developers/docs)

---

<div align="center">

**Built for learning, testing, and experimentation.**

⭐ Try it in a private test server before adapting it for a real community.

</div>
