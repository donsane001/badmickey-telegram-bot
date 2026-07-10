import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

WEBSITE = "https://badmickey.netlify.app/"
X_LINK = "https://x.com/Badmickeycoin"
PUMPFUN = "https://pump.fun/coin/4wd7faasQAakmYmNokeQ9aA1Czq27DYHEDChUYxppump"
TG_LINK = "https://t.me/+6mN9rvu70U41NmQx"

CONTRACT = "4wd7faasQAakmYmNokeQ9aA1Czq27DYHEDChUYxppump"

AUTO_POST = f"""
🐭 BADMICKEY

🚀 The memes are back!

💰 Contract:
{CONTRACT}

🌐 Website:
{WEBSITE}

🐦 X:
{X_LINK}

🔥 Buy:
{PUMPFUN}

💬 Telegram:
{TG_LINK}

LFG 🚀
"""

keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🌐 Website", url=WEBSITE),
            InlineKeyboardButton("🐦 X", url=X_LINK),
        ],
        [
            InlineKeyboardButton("🚀 Buy", url=PUMPFUN),
            InlineKeyboardButton("💬 Telegram", url=TG_LINK),
        ],
    ]
)
