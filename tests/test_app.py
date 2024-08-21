from http import HTTPStatus

from fastapi.testclient import TestClient

from todo_app_backend_fast_api.app import app


def test_index_root_return_ok_and_olar_mundo():
    client = TestClient(app)  # arange(preparação)

    response = client.get("/")  # act (ação)

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olar mundo!'}
