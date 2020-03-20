from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = "1234"
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name']==name, items), None)
        return {'item': None}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'an item with name {} already exists'.format(name)}, 400

        request_data = request.get_json(force=True)
        item = {'name': name, 'price': request_data['price']}
        items.append(item)
        return item, 201

    def put(self, name):
        pass

    def delete(self, name):
        pass


class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(debug=True)
