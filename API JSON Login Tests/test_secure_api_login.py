import requests

def test_api_sql_injection_secure():
    payload = {
        "username": "' OR 1=1 --",
        "password": "anything"
    }
    response = requests.post("http://127.0.0.1:5000/api/login", json=payload)
    assert response.status_code == 401, "❌ API SQLi succeeded on secure app when it should fail"