import telebot
from telebot import types

TOKEN = "8519435495:AAGaz4j2HPc96yOkqG5a9PxoTf1rtx0OO28"

bot = telebot.TeleBot(TOKEN)

# ------------------------
#       START COMMAND
# ------------------------
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Admin Contact")
    btn2 = types.KeyboardButton("Bot Rules")
    btn3 = types.KeyboardButton("Start")
    keyboard.add(btn1, btn2, btn3)

    bot.send_message(
        message.chat.id,
        "Hi, I'm Tanzim bot 👋\nWelcome to Tanzim bot ❤️",
        reply_markup=keyboard
    )

# ------------------------
#     TEXT BUTTONS
# ------------------------
@bot.message_handler(func=lambda message: True)
def reply_msg(message):

    if message.text == "Admin Contact":
        bot.send_message(
            message.chat.id,
            "📧 যে কোন সমস্যায় আমাদের সাথে যোগাযোগ করুন:\n\nEmail: **mrghii34@gmail.com**"
        )

    elif message.text == "Bot Rules":
        bot.send_message(
            message.chat.id,
            "এই বটটি ইউজ করুন এবং মজা করুন ✅\n\nভবিষ্যতে এই বটের মধ্যে আরও অনেক আপডেট আনবো ❤️\nআরো ভালো ভালো ফিচার যুক্ত করব ইনশাআল্লাহ 😊"
        )

    elif message.text == "Start":
        bot.send_message(
            message.chat.id,
            "Hi, I'm Tanzim bot 👋\nWelcome to Tanzim bot ❤️"
        )

# ------------------------
#       BOT RUN
# ------------------------
print("Bot running...")
bot.infinity_polling()