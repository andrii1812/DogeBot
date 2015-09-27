import json
from flask import Flask, request
import telegram
from dogefactory.randomDoge import randomDoge
from dogefactory.DogeFactory import DogeFactory

app = Flask(__name__)
bot = telegram.Bot(token='118292594:AAEN19D9JozNBTM-9ppUt1sY4CIBoop6KLM')
#bot.setWebhook('https://dogebot21.herokuapp.com/')


@app.route('/', methods=['POST'])
def message():

    data = request.data
    update = json.loads(str(data, 'utf-8'))

    chat_id = update['message']['chat_id']
    text = str(update['message']['text'])
    if text.startswith('/doge'):
        doge_text = text.replace('/doge ', '')

        background = randomDoge()
        doge = DogeFactory(doge_text)\
            .load_image_from_bytes(background)\
            .create_doge()

        filename = 'doge_123.png'
        stream = open(filename, 'wb')
        doge.save(stream, 'PNG')
        stream.close()

        bot.sendPhoto(chat_id, photo=open(filename, 'rb'), caption='doge_123')
    else:
        bot.sendMessage(chat_id, 'wow. what?')
    return ''


if __name__ == '__main__':
    app.run('0.0.0.0', 80)
