import sqlite3


class MyDB:
    def __init__(self, db_name='items.db'):
        self.name = db_name
        self.connection = sqlite3.connect(self.name)
        self.create_items_table()

    def get_cursor(self):
        return self.connection.cursor()

    def create_items_table(self):
        cursor = self.get_cursor()
        create_table_query = "CREATE TABLE IF NOT EXISTS items (" \
                             "id INTEGER PRIMARY KEY AUTOINCREMENT," \
                             "name TEXT UNIQUE," \
                             "amount INTEGER," \
                             "price REAL NOT NULL);"
        cursor.execute(create_table_query)
        cursor.close()

    def get_all_items(self):
        self.connection.row_factory = sqlite3.Row
        cursor = self.get_cursor()
        get_items_query = "SELECT * FROM items"
        cursor.execute(get_items_query)
        items_data = cursor.fetchall()
        cursor.close()
        return list(map(dict, items_data))

    def get_one_item(self, item_id):
        self.connection.row_factory = sqlite3.Row
        cursor = self.get_cursor()
        get_item_query = "SELECT * FROM items WHERE id = ?"
        cursor.execute(get_item_query, item_id)
        item_data = cursor.fetchone()
        cursor.close()
        return dict(item_data)

    def insert_item(self, name, amount, price):
        cursor = self.get_cursor()
        insert_item_query = "INSERT INTO items (name, amount, price)" \
                            "VALUES(?, ?, ?)"
        cursor.execute(insert_item_query, (name, amount, price))
        cursor.close()
        self.connection.commit()

    def update_item(self, item_id, name, amount, price):
        cursor = self.get_cursor()
        update_item_query = "UPDATE items " \
                            "SET name = ?, amount = ?, price = ?" \
                            "WHERE id = ?"
        cursor.execute(update_item_query, (name, amount, price, item_id))
        cursor.close()
        self.connection.commit()

    def delete_item(self, item_id):
        cursor = self.get_cursor()
        delete_item_query = "DELETE FROM items WHERE id = ?"
        cursor.execute(delete_item_query, (item_id,))
        cursor.close()


if __name__ == '__main__':
    mydb = MyDB()
    items = mydb.get_all_items()
    print(items)
