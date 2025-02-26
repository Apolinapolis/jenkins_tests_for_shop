from models.place_dbo import *
import pytest


def get_server_response(place:PlaceDbo, flag:bool = True) -> str:
    """Логика сервера"""
    if flag and place.dbo and not place.agr:
        return f'{place.name} dbo: False, agr: False'
    else:
        return f'{place.name} dbo: {place.dbo}, agr: {place.agr}'


def get_server2_response(place: PlaceDbo, flag: bool = True) -> str:
    """Логика второго сервера"""
    if flag and place.dbo and not place.agr:
        return f'{place.name} dbo: False, agr: False'
    else:
        return f'{place.name} dbo: {place.dbo}, agr: {place.agr}'


@pytest.fixture(params=[
    ("dbo- agr-", False, False),
    ("dbo- agr+", False, True),
    ("dbo+ agr-", True, False),
    ("dbo+ agr+", True, True)
], ids=lambda param: f"{param[0]}") # ids - для логирования параметра с которым упадем
def place_dbo(request):
    name, dbo, agr = request.param
    return PlaceDbo(name=name, dbo=dbo, agr=agr)

# server = end point, где мы проверяем как отработает логика, ids - для логирования с какой ручкой падаем
# flag - это кверя. их будет 3 ( "" , has_sales_agreement=true, has_sales_agreement=false)
@pytest.mark.parametrize('server', [get_server_response, get_server2_response], ids=lambda func: func.__name__)
@pytest.mark.parametrize("flag", [True, False], ids=['flag=True', 'flag=False'])
def test_dbo_agr_logic(place_dbo,server, flag):
    response = server(place_dbo, flag=flag)

    if flag and place_dbo.dbo and not place_dbo.agr:
        expected_response = f'{place_dbo.name} dbo: False, agr: False'
    else:
        expected_response = f"{place_dbo.name} dbo: {place_dbo.dbo}, agr: {place_dbo.agr}"

    assert expected_response == response


"""
Одна функция для проверки логики по задаче.
Отдельно будет простая функция для проверки невалидных значений
Вероятно, захочется убрать параметризацию server и дублировать код для каждой ручки. 
"""