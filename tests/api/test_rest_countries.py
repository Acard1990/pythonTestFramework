import json

def test_validateSuccessCodeFromGetAll(api_client):
    response = api_client.get("all")
    assert response.status_code == 200

def test_validateSuccessCodeFromGetCountryByName(api_client):
    response = api_client.get("name/Italy")
    assert response.status_code == 200

def test_validateItalyInfoReturnedInbody(api_client):
    response = api_client.get("name/Italy")
    response_data = json.loads(response.text)
    for item in response_data:
        assert item['name']['common'] == 'Italy'
