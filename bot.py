from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# =========================
# BOT TOKEN
# =========================

TOKEN = "8070825229:AAF3u9E-5aOhlrfxGNae8dQPFCUD4bK52oI"

# =========================
# START IMAGE
# =========================

START_IMAGE = "https://i.postimg.cc/RZYQtWzp/IMG-20260522-015805-713.jpg"

# =========================
# START COMMAND
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [
            InlineKeyboardButton(
                "🔥 OPTION 1",
                callback_data="op1"
            )
        ],

        [
            InlineKeyboardButton(
                "💎 OPTION 2",
                callback_data="op2"
            )
        ],

        [
            InlineKeyboardButton(
                "🎬 OPTION 3",
                callback_data="op3"
            )
        ],

        [
            InlineKeyboardButton(
                "👑 OPTION 4",
                callback_data="op4"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=START_IMAGE,
        caption="<b>🔥 WELCOME TO MY BOT 🔥</b>",
        parse_mode="HTML",
        reply_markup=reply_markup
    )

# =========================
# BUTTON HANDLER
# =========================

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    if data == "op1":

        await query.message.reply_text("🔥 OPTION 1 CLICKED")

    elif data == "op2":

        await query.message.reply_text("💎 OPTION 2 CLICKED")

    elif data == "op3":

        await query.message.reply_text("🎬 OPTION 3 CLICKED")

    elif data == "op4":

        await query.message.reply_text("👑 OPTION 4 CLICKED")

# =========================
# RUN BOT
# =========================

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CallbackQueryHandler(button_handler)
)

print("✅ BOT RUNNING...")

app.run_polling()
