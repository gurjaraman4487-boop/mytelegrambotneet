from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

# =========================
# BOT TOKEN
# =========================

TOKEN = "8070825229:AAF3u9E-5aOhlrfxGNae8dQPFCUD4bK52oI"

# =========================
# START IMAGE
# =========================

START_IMAGE = "https://i.postimg.cc/g0kV13q7/330px-Flag-of-India-svg.png"

# =========================
# QR IMAGE LINK
# =========================

QR_IMAGE = "https://i.postimg.cc/43dcWsXK/Screenshot-20260522-022954.png"

# =========================
# LINKS
# =========================

MAIN_CHANNEL = "https://t.me/re_neet_2026"

PROOF_LINK = "https://t.me/reneetproofs"

ADMIN_LINK = "https://t.me/dealer_x"

# =========================
# START COMMAND
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [
            InlineKeyboardButton(
                "🤗 Join Main Channel",
                url=MAIN_CHANNEL
            )
        ],

        [
            InlineKeyboardButton(
                "🧾 Click Here Chk Proof",
                url=PROOF_LINK
            )
        ],

        [
            InlineKeyboardButton(
                "💸 Get QR",
                url=QR_IMAGE
            )
        ],

        [
            InlineKeyboardButton(
                "👑 Admin",
                url=ADMIN_LINK
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
# RUN BOT
# =========================

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

print("✅ BOT RUNNING...")

app.run_polling()
