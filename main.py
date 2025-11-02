import telebot
from logic import get_class

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(content_types=['photo'])

def get_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    class_name, score = get_class(file_name)
    if class_name == "Голубь" and score > 0.9:
        bot.reply_to(message, "Это голубь, его можно кормить и не кормить")
    if class_name == "Синица" and score > 0.9:
        bot.reply_to(message, "Это синица, её можно ловить")
    if class_name == "Орёл" and score > 0.9:
        bot.reply_to(message, "Это орёл, от него нужно убегать")
    else:
        bot.reply_to(message, "Произошла ошибка, попробуйте позже")
    bot.reply_to(message, class_name)
bot.polling()
