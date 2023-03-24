from py_tools.src.example_data import Engine


def test_engine_load_data(mocker):
    mocker.patch('py_tools.src.example_data.DBConnector.__init__',
                 return_value=None)
    mocker.patch('py_tools.src.example_data.DBConnector.get',
                 return_value='xyz')
    output = Engine().load_data()
    assert output == 'xyzxxx'
