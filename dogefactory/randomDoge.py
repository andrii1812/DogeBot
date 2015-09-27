import random
import requests


def randomDoge():

    urls = [
        'https://pbs.twimg.com/profile_images/378800000822867536/3f5a00acf72df93528b6bb7cd0a4fd0c.jpeg',
        'https://pbs.twimg.com/profile_images/417201275466690560/TzVjIXv2.jpeg',
        'http://barkpost-assets.s3.amazonaws.com/wp-content/uploads/2013/11/plainDoge-700x525.jpg'
    ]

    url_num = random.randint(0, len(urls) - 1)
    response = requests.get(urls[url_num])
    return response.content