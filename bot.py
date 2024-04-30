import telebot
import config
from telebot import types

bot = telebot.TeleBot(token=config.TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_start_message(message: types.Message) -> None:
    """
    Instruction message
    :param message: types.Message
    :rtype: None
    """
    print(message.chat.id)
    bot.reply_to(message, 'Hello! Send me video or text and i will forward it to other chats.')


@bot.message_handler(content_types=['text', 'video'])
def forward_message(message: types.Message) -> None:
    """
    Forward text or video messages
    :param message: types.Message
    :rtype: None
    """
    content_handlers = {
        'text': send_text_message,
        'video': send_video_message
    }
    user_mark = f'/ send by: '
    if message.reply_to_message:
        text_and_owner = message.reply_to_message.text.split(user_mark)
        if len(text_and_owner) == 2:
            message_owner = text_and_owner[1]
            bot.send_message(message.chat.id, f'@{message_owner}')
    elif message.content_type in content_handlers:
        handler = content_handlers[message.content_type]
        send_message_to_chats(message=message, user_mark=user_mark, callback=handler)
    else:
        bot.send_message(message.chat.id, 'Content type not supported.')


def send_message_to_chats(message: types.Message, user_mark: str, callback: callable) -> None:
    """
    Send tg message from bot chat to all chats
    :param message: types.Message
    :param user_mark: str
    :param callback: callable
    :rtype: object
    """

    for chat_id in config.CHATS_IDS:
        callback(message=message, user_mark=user_mark, chat_id=chat_id)


def send_text_message(message: types.Message, user_mark: str, chat_id: int) -> None:
    """
    Send text message to chat by chat id

    :param message: types.Message
    :param user_mark: str
    :param chat_id: int
    :rtype: None
    """
    bot.send_message(
        chat_id=chat_id,
        text=f'{message.text} {user_mark}'
    )


def send_video_message(message: types.Message, user_mark: str, chat_id: int) -> None:
    """

    :param message: types.Message
    :param user_mark: str
    :param chat_id: int
    :rtype: None
    """
    bot.send_video(
        chat_id=chat_id,
        video=message.video.file_id,
        caption=f'{message.caption} {user_mark}'
    )


if __name__ == '__main__':
    bot.polling(non_stop=True)
