from Flask import Flask
import telegram

app = Flask(__name__)
bot = telegram.Bot(token='118292594:AAEN19D9JozNBTM-9ppUt1sY4CIBoop6KLM')


@app.route('/', methods=['POST'])
def message():
    return 200
