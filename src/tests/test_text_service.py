import json
from app.services import word_count_service as wd


def test_word_count_service(test_app):
    first_url = {"url": "www.bbc.co.uk"}
    second_url = {"url": "ww.bbc.co.uk"}
    third_url = {"ul": "www.bbc.co.uk"}
    first_response = test_app.post("/wordcount/", json=first_url)
    second_response = test_app.post("/wordcount/", json=second_url)
    third_response = test_app.post("/wordcount/", json=third_url)
    assert first_response.status_code == 200
    assert second_response.status_code == 400
    assert second_response.json() == {"detail": "The provided URL is Invalid"}
    assert second_response.status_code == 400
    assert third_response.status_code == 422
    assert third_response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "url"
                ],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }


def test_health(test_app):
    response = test_app.get("/health")
    assert response.status_code == 200
    assert bool(response.json()) == False
