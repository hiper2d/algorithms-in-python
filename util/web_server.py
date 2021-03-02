from flask import Flask

api = Flask(__name__)


@api.route('/', methods=['GET'])
def get_companies():
    return 'Hey'


if __name__ == '__main__':
    api.run(host='0.0.0.0')
