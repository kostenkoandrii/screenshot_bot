import telebot
from screenshot_maker_bot import make_screenshot
import settings


bot = telebot.TeleBot(settings.TELBOT_API_TOKEN)
WELCOME_TEXT = 'Hello, I will help you to make screenshot of website, Give me url please'


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, WELCOME_TEXT)


@bot.message_handler(content_types=['text'])
def handle_funcs(message):
    """
    Method witch get url from user message,
    take screenshot of website and send it to user
    """
    url = message.text if message.text.lower().find('http') != -1 else 'https://' + message.text
    screenshot = make_screenshot(url)
    if not screenshot:
        error_404 = open('404.png', 'rb')
        bot.send_photo(message.chat.id, error_404)
        bot.send_message(message.chat.id, 'Something wrong( Page not found')
    else:
        bot.send_photo(message.chat.id, screenshot)
        bot.send_message(message.chat.id, 'Great, one more time?')


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will happen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

# None stop polling users requests
if __name__ == '__main__':
    bot.polling(none_stop=True)
