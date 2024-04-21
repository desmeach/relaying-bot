import telebot
import config

bot = telebot.TeleBot(token=config.TOKEN, parse_mode=None)


@bot.message_handler()
def send_start_message(message):
    bot.reply_to(message, 'Hello! Send me video or text and i will forward it to other chats.')


if __name__ == '__main__':
    bot.polling(non_stop=True)
