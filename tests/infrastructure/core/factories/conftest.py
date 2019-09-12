from pytest import fixture
from json import dump
from injectark import Injectark
from instark.infrastructure.core.configuration.config import (
    TrialConfig, DevelopmentConfig, ProductionConfig)


@fixture
def production_config(tmp_path):
    production_config = ProductionConfig()
    production_config["firebase_credentials_path"] = str(
        tmp_path / "firebase_credentials.json")
    data = {
        "type": "service_account",
        "project_id": "massive-graph-230014",
        "private_key_id": "d085f36c8a0d294077a5554f53e0d590b2ca8539",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCZGooJI0oSy2Fz\nyx970ZgOzD8R8wHbkkff+bHH0JL6Ro4O0Q7oAVnIPZtItBx8nvBIcuXnYFxN+HQs\ntJ6FxbCfHUIjGD4IAzyIE8ld1iNUA5L7M1DgyVx187TWQkC/bNYWIxxllaIkE7vI\nB4LED+0ktkkkmSGXF7HoKChB1iNl1JnMSXh5nUoaU+eB0SWXNbMjuizXb6ykC1mE\nXsxHUfZjJ5QsaAaevbklCwa/aGQwTD5JtwkuJFic0dTQ5H4pWbCaBKKLugUzcadR\nLQxn3CZhTnpSq4ll9cATl5Xgt6ciUVD/gxBVOzgQZDJWN3NJz+DQLeJpLy0UY7UP\nXNM+o6WpAgMBAAECggEAAadFd9lLdr3/CKzYI3JtQbWndbZp3fjrsUnFR3rjZ3QF\nGzhbQJqpIU43A9c8GoVt415oSLIj9QyalpQBxUCQCnvap73eh6AfUnniOhLysTjT\nqMZSWIccKkLuQEUZZWfTvQv2hctSo7CZ3cxk92CTp0qXqh9EO1k8aN0sKB/bpIEd\nuJbpPa2NVUHSxGiqG6fefj7bpkvHs5KdPGmqJHENLROhjgKlHntK9sAHbEsE2mtc\nkfqH7vDlwBn8hKjQMvJ0a9cSeaYK5kMHgcSVjyagQMrDPgxuycndmpQ1EF/Vf7xy\nAWTmE3CeKOPEN66CAAKzCl2NNKiLCM+lGrKiwPk+bQKBgQDXOmL5bLR90oiuImSr\nZFzaEpAva0Rk1mkiDa3+04WuWuNc0qCOqu2toeb16Zkw3KRj/OXpzz4w6NB48Icx\nNWjXjbHQL4kdMa3+Y2Z+HuBPgJ7+T+N77STODqC6k0HY/IAY0gAfgWtg55zNJv+O\nccOfU2dHzuvRSzeEzL/6J3oZdQKBgQC2G2SF5AVHVKsdE0797QudQMhdwy+ID1nD\nWFfNUs/yQsCYx8HQtNEPNEpvTkeYzwLquael79MvwGYNPgSNVV2t/Qst+UHMf02l\nNEap3u+Tcs97t6nRh2jnAd4eR56LHZvHp1oUD+BDIHx7ie0LcyYwpPuRkweEK0/Y\n9taO5oNg5QKBgQCqaQ5Ikutt3C5gQdcXZUWnXJ9RDEuA08s2LUKgy3XDES+IJTT/\nARNjMRefia/DYk++41RfBbomG5BE0Z0ZN0KluQka3yhfNyCelLFoFqZgDGTW0wY4\n7xD/HdHhKAsw9Ouvu0Zhq6ULexdJ0CDz9dt/4RebYZiRhE6XFU7DkFI6qQKBgDBq\nd/9g8EZWrGe+inHYZA4a+ypyimCSNDtLcYyVR9QRC0OTWGQ0rqBsNp4BIefuocfm\nNDxZ1rwLWxaKNouc9psbe61tZ6EG943EqEThkLCTBbbOzcd3SNyiEnvabrxt0szy\nIXDUB7vRF0eBFBTHOJAWTQwXGxh4q3HzrnevsZ5BAoGAOBqsNgfbyEXx+qTfF/2V\nTiMFixc/5qbHNj5ET1G9WFuxAp+ldAJ2fxkthP3KdfwVfEHrkcEK7HootMQISknW\nVGZmr6cXJNbceYGTeADWtHJIR80qeX5BF+caaUX1lkizfC79+SeDspT2FSaVe2/Z\nOR7HAygqK/j5ep3TOFcFC1Y=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-dc744@massive-graph-230014.iam.gserviceaccount.com",
        "client_id": "117987315633038245097",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-dc744%40massive-graph-230014.iam.gserviceaccount.com"
    }

    with open(production_config["firebase_credentials_path"], "w") as f:
        dump(data, f, indent=2)
    return production_config


@fixture
def test_data(production_config):
    return [
        TrialConfig(),
        DevelopmentConfig(),
        production_config
    ]
