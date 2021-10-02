from flask import Flask
import requests

app = Flask(__name__)

# if you go to this route while in the app,
# make this request.
# set in a decorator.
@app.route('/api', methods=['GET'])
def api():
    r = requests.get('https://learning.oreilly.com/api/v1/book/9780137611676/chapter/nje1_01_05_02.html')
    print(r.content)
    return r.content
    # return {
    #     'userId': 1,
    #     'title': 'Flask + React Application 1.5',
    #     'completed': False
    # }
