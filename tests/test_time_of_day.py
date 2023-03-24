import pytest
from datetime import datetime
from py_tools.src.time_of_day import get_time_of_day


@pytest.mark.parametrize(
        'datetime_obj, expect',
        [
            (datetime(2023, 3, 24, 0, 0, 0), 'Nigth'),
            (datetime(2023, 3, 24, 1, 00, 0), 'Nigth'),
            (datetime(2023, 3, 24, 6, 10, 0), 'Morning'),
            (datetime(2023, 3, 24, 12, 0, 0), 'Afternoon'),
            (datetime(2023, 3, 24, 14, 10, 0), 'Afternoon'),
            (datetime(2023, 3, 24, 18, 0, 0), 'Evening'),
            (datetime(2023, 3, 24, 19, 35, 0), 'Evening'),
        ],
)
def test_get_time_of_day(datetime_obj, expect, mocker):
    mock_now = mocker.patch('py_tools.src.time_of_day.datetime')
    mock_now.now.return_value = datetime_obj

    assert get_time_of_day() == expect
