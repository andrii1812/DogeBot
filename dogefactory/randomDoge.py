import random
import requests


def randomDoge():

    urls = [
        [
            'https://pbs.twimg.com/profile_images/378800000822867536/3f5a00acf72df93528b6bb7cd0a4fd0c.jpeg',
            (183, 280, 100)
        ],
        [
            'https://pbs.twimg.com/profile_images/417201275466690560/TzVjIXv2.jpeg',
            (779, 633, 150)
        ],
        [
            'http://barkpost-assets.s3.amazonaws.com/wp-content/uploads/2013/11/plainDoge-700x525.jpg',
            (331, 166, 100)
        ]
    ]

    url_num = random.randint(0, len(urls) - 1)
    response = requests.get(urls[url_num][0])
    return response.content, urls[url_num][1]