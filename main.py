
import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
) 
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing")

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
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐭 Welcome to the BadMickey Bot!",
        reply_markup=keyboard,
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
Available Commands

/start - Start the bot
/help - Show help
/website - Website
/x - X Account
/buy - Buy on Pump.fun
/contract - Show Contract
/telegram - Telegram Group
/raid - Raid Message
        """
    )

async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WEBSITE)

async def x(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(X_LINK)

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(PUMPFUN)

async def contract(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(CONTRACT)

async def telegram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(TG_LINK)

async def raid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 RAID TIME!\n\nLike ❤️ Retweet 🔁 Comment 💬\n\nPush BadMickey everywhere! LFG! 🔥"
    )

async def auto_post(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=GROUP_ID,
        text=AUTO_POST,
        reply_markup=keyboard,
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("website", website))
    app.add_handler(CommandHandler("x", x))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CommandHandler("contract", contract))
    app.add_handler(CommandHandler("telegram", telegram))
    app.add_handler(CommandHandler("raid", raid))

    app.job_queue.run_repeating(
        auto_post,
        interval=1200,
        first=30,
    )

    print("BadMickey Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
