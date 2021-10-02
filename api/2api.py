from flask import Flask

app = Flask(__name__)

# if you go to this route while in the app,
# make this request.
# set in a decorator.
@app.route('/', methods=['GET'])
def api():
    return {
        'userId': 1,
        'title': 'Flask React Application',
        'completed': False
    }
