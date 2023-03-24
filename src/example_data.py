from py_tools.src.dataset import load_data
from py_tools.src.db_connection import DBConnector


def process_data():
    data = load_data()
    processed_data = data['key1']
    return processed_data


class Engine:
    def __init__(self):
        self.connector = DBConnector()

    def load_data(self):
        data = self.connector.get(123)
        print(data)
        data += 'xxx'
        return data
