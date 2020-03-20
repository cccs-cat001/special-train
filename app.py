from flask import Flask, jsonify

app = Flask(__name__)
stores = [
    {
        'name': 'store1',
        'items': [
            {
                'name': 'item1',
                'price': 10.99
            }
        ]
    }
]
@app.route('/')
def home():
    return "Hello world!"


@app.route('/store', methods=['POST'])
def create_store():
    pass


@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    pass


@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
    pass


app.run(port=5000)
