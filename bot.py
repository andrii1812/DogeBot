import io
import telegram
from dogefactory.DogeFactory import DogeFactory
from dogefactory.randomDoge import randomDoge

bot = telegram.Bot(token='118292594:AAEN19D9JozNBTM-9ppUt1sY4CIBoop6KLM')

print(bot.getMe())

last_update_id = -1

while True:
    update = bot.getUpdates()[-1]
    if update.update_id == last_update_id:
        continue

    last_update_id = update.update_id
    chat_id = update.message.chat_id
    text = str(update.message.text)
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



