# 🤖 Discord Self Bot Utility

A feature-rich **Discord self-bot** built using discord.py-self.
This bot provides utilities for **channel management, role handling, message tracking, and backups**.

---

## ⚠️ Disclaimer

> This project uses a **self-bot**, which operates on a user account instead of a bot account.
> Using self-bots **violates Discord’s Terms of Service** and may result in account suspension or ban.
> Use this project **only for educational purposes** and at your own risk.

---

## 🚀 Features

### 💬 Basic Commands

* `!hello` → Greets the user
* `!say <message>` → Echo message

---

### 👥 Role Management

* `!addrole <member> <role>` → Assign role
* `!remove_role <member> <role>` → Remove role

---

### 🧾 Message Tools

* `!messagehistory <member> <limit>`
  → Fetch recent messages from a user in the current channel

---

### 📁 Channel Management

* `!create_text_channel <name>`
* `!create_voice_channel <name>`
* `!delete_channel <name>`

---

### 🔐 Permission Check

* `!my_perms <member>` → Lists permissions of a member

---

### 🔗 Webhook Management

* `!create_webhook <name>`
* `!delete_webhook <name>`

---

### 🗂️ Server Utilities

* `!raw_copy_channels`
  → Displays all channels grouped by category

* `!backup`
  → Creates a full JSON backup of:

  * Categories
  * Channels
  * Metadata (topics, bitrate, etc.)

---

## 🛠️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/[yourusername]/discord-selfbot.git
cd discord-selfbot
```

### 2️⃣ Install dependencies

```bash
pip install -U discord.py-self
```

---

## 🔑 Configuration

⚠️ **Never expose your token publicly**

Replace this line in your code:

```python
token = "YOUR_TOKEN_HERE"
```

👉 Recommended:

```python
import os
token = os.getenv("DISCORD_TOKEN")
```

---

## ▶️ Running the Bot

```bash
python bot.py
```

---

## 📂 Project Structure

```
.
├── bot.py
├── backup_*.json
└── README.md
```

---

## ⚡ Rate Limiting Notes

* Commands like channel creation/deletion may hit Discord rate limits
* Use `asyncio.sleep()` to prevent API abuse
* Avoid running destructive commands repeatedly

---

## ❗ Known Issues

* Self-bots may break due to Discord API updates
* Risk of account restriction
* Limited scalability

---

## 📌 Future Improvements

* Restore backup feature
* Channel cloning system
* Advanced logging
* Rate-limit adaptive system

---

## 📜 License

This project is for **educational use only**.
No warranty or liability is provided.

---
