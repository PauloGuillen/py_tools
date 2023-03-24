from py_tools.src.dataset import load_data


def process_data():
    data = load_data()
    processed_data = data['key1']
    return processed_data
