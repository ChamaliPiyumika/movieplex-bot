from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ඔබේ නිවැරදි Bot Token එක
BOT_TOKEN = "8845160703:AAGkTLzifU6rrNCSB9UxrAbF12v8uuzn76M"

MOVIES_DATABASE = {
    "movie_1": (
        "BAACAgUAAxkBAAMSaso6PiUAAROJzlgLtx_cV2kSAxsQAAK3IgACEutQVqTIPUWnDcm2PQQ"
    ),  # මෙතැනට අලුත් ID එක දෙන්න
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  if context.args:
    movie_key = context.args[0]
    if movie_key in MOVIES_DATABASE:
      file_id = MOVIES_DATABASE[movie_key]

      keyboard = [
          [
              InlineKeyboardButton("WhatsApp", url="https://whatsapp.com"),
              InlineKeyboardButton("Facebook", url="https://facebook.com"),
          ]
      ]
      reply_markup = InlineKeyboardMarkup(keyboard)

      # වීඩියෝව සහ බටන් යැවීම
      await update.message.reply_video(
          video=file_id, caption="ඔන්න ඔබේ චිත්‍රපටය!", reply_markup=reply_markup
      )
    else:
      await update.message.reply_text("සමාවන්න, එම චිත්‍රපටය හමු නොවීය!")
  else:
    await update.message.reply_text(
        "කරුණාකර වෙබ් අඩවියේ ඇති ලින්ක් එක හරහා පැමිණෙන්න."
    )


def main():
  application = ApplicationBuilder().token(BOT_TOKEN).build()
  application.add_handler(CommandHandler("start", start))

  print("Movie Bot is running...")
  application.run_polling()


if __name__ == "__main__":
  main()