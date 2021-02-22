def test_app_creation(client):
    r = client.get('/health/')

    assert r.status_code == 200
    assert r.json.get('health') == True