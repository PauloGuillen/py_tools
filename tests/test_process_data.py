from py_tools.src.example_data import process_data


def test_process_data(mocker):
    mocker.patch('py_tools.src.example_data.load_data', return_value={'key1': 'val1', 'key2': 'val2'})
    assert process_data() == 'val1'
