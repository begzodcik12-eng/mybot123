from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "YOUR_TOKEN_HERE"
ADMIN_ID = 5517115287

menu = ReplyKeyboardMarkup(
    [["🎨 DIZAYN XIZMATLARI", "📁 PORTFOLIO"],
     ["📩 BUYURTMA BERISH"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ishlayapti 🚀", reply_markup=menu)

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("BOT STARTED")
app.run_polling()
