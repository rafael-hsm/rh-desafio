from django.test import Client


# Testando conexão
def test_status_code(client: Client):
    resp = client.get('')
    assert resp.status_code == 200
