import json

from wsgi_pt_2.api.db import MyDB
from wsgi_pt_2.api.api import App
from wsgi_pt_2.middleware import LoggingMiddleware


mydb = MyDB()
app = App()
app.add_middleware(LoggingMiddleware)


@app.route('/query')
def home(request, response):
    response.text = f'Here are your Query Parameters:'
    queries = app.handle_query_string(request)
    if queries:
        response.text += ''.join(f'\n{key} = {value}' for key, value in queries.items())


@app.route('/secured')
def items(request, response):
    response.text = 'This is SECURE page. Your visit has been logged!'


@app.route('/items', methods=['GET', 'POST'])
@app.route('/items/{item_id}', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
class ItemResource:
    def get(self, request, response, item_id=None):
        try:
            if item_id:
                res_data = mydb.get_one_item(item_id)
            else:
                res_data = mydb.get_all_items()

            res_type = 'application/json'
            res_body = json.dumps(res_data).encode("UTF-8")
            app.set_response(response, code=200, type_=res_type, body=res_body)
        except Exception as e:
            print(e)
            app.set_response(response)

    def post(self, request, response):
        try:
            mydb.insert_item(**request.json_body)
            app.set_response(response, code=201, text='Resource has been created.')
        except Exception as e:
            print(e)
            app.set_response(response, code=400, text='Bad Request.')

    def put(self, request, response, item_id):
        try:
            item_old_body = mydb.get_one_item(item_id)
            item_old_body.pop('id', None)
            item_new_body = request.json_body
            item_new_body.pop('id', None)
            item_old_body.update(item_new_body)
            mydb.update_item(item_id, **item_old_body)
            app.set_response(response, code=204, text='Resource updated successfully.')
        except Exception as e:
            print(e)
            app.set_response(response, code=400, text='Bad Request.')

    def patch(self, request, response, item_id):
        try:
            item_old_body = mydb.get_one_item(item_id)
            item_old_body.update(request.json_body)
            item_old_body.pop('id', None)
            mydb.update_item(item_id, **item_old_body)
            app.set_response(response, code=204, text='Resource updated successfully.')
        except Exception as e:
            print(e)
            app.set_response(response, code=400, text='Bad Request.')

    def delete(self, request, response, item_id):
        try:
            mydb.delete_item(item_id)
            app.set_response(response, code=204, text='Resource deleted successfully.')
        except Exception as e:
            print(e)
            app.set_response(response, code=400, text='Bad Request.')
