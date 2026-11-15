from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
# v2 - fixed bot
TOKEN = "9141701616:AAERVxkDKJgMJmp0utow6Q3GllnqJoyXlPY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("আসসালামু আলাইকুম! আমি মা-বাবা বট! ❤️\nআমাকে কিছু লিখো")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "মা" in text:
        await update.message.reply_text("মা হলো জান্নাত ❤️ মায়ের জন্য দোয়া করো।")
    elif "বাবা" in text:
        await update.message.reply_text("বাবা হলো ছায়া ❤️ বাবার জন্য দোয়া করো।")
    else:
        await update.message.reply_text("আমি শুনছি ❤️ মা বা বাবা নিয়ে কিছু লিখো।")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("Bot চলতেছে...")
    app.run_polling()

if __name__ == "__main__":
    main
