import json

from classes.engine_hh import HeadHunter


def test_hh_get_content():
    """Тест для метода get_content класса HeadHunter"""
    with open('resquest.json', 'r') as file:
        result = HeadHunter('1').get_content(json.load(file))
        assert result[0] == 3529
        assert len(result) == 9
        assert result[-1] == "https://hh.ru/vacancy/3529"
