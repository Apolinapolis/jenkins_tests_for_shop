from models.place_dbo import *
import pytest



def get_server_response(place:PlaceDbo, flag:bool = True) -> str:
    if place.dbo and  place.agr == False and flag:
        return f'{place.id} dbo: False, agr: False'
    else:
        return f'{place.id} dbo: {place.dbo}, agr: {place.agr}'

@pytest.fixture
def get_db_place():
    return PlaceDbo(1)


def test_positive(get_db_place):
    response = get_server_response(get_db_place)
    assert 'dbo: False, agr: False' in response


# реализовать каждый тестовый случай с помощью параметризации
# вынести серверную логику в отдельный файл




