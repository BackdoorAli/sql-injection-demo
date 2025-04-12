import requests

def test_blind_sql_injection_insecure():
    payload = {
        "username": "' OR 1=1 --",
        "password": "anything"
    }
    response = requests.post("http://127.0.0.1:5000/blind-login", data=payload)
    assert response.text.strip() == "Success", "❌ Blind SQLi failed on insecure app when it should pass"