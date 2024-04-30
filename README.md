# relaying-bot

This bot created to forward message (e.g. memes) in Telegram to few chats. Current version 1.0 include text ad video support with labels.

# Instruction 

To using the bot you need to paste your botFather token ([instruction]([https://duckduckgo.com](https://core.telegram.org/bots/tutorial) "BotFather token instruction") into TOKEN variable in config.py. Also add all chat's ID in CHATS_IDS where you prefer to forward your message.

When all variables filled in config, run bot with ``python bot.py``.

Now you can send any message to your bot and check that bot forward it to other chats (by id in CHATS_IDS variable).
