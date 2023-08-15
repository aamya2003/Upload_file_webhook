from flask import Flask, request
import telebot

app = Flask(__name__)

bot = telebot.TeleBot("Your_Bot_Token")

@app.route('/bot_webhook', methods=['POST'])
def bot_webhook():
  bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
  return 'OK'

@app.route('/', methods=['GET'])
def home():
  return "I'm Alive"

@app.route('/set_app', methods=['GET'])
def set_app():
  bot.remove_webhook()
  bot.set_webhook("https://" + request.host + "/bot_webhook")
  return 'Done'


@bot.message_handler()
def Myfunc(message):
  bot.send_message(message.chat.id, "Hi, What's happend?")


if __name__ == '__main__':
  app.run(port=8000, host='0.0.0.0')
