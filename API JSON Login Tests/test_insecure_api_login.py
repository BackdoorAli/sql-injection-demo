import requests

def test_api_sql_injection_insecure():
    payload = {
        "username": "' OR 1=1 --",
        "password": "anything"
    }
    response = requests.post("http://127.0.0.1:5000/api/login", json=payload)
    assert response.json()["status"] == "success", "❌ API SQLi failed on insecure app when it should pass"