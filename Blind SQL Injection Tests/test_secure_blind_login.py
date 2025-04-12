import requests

def test_blind_sql_injection_secure():
    payload = {
        "username": "' OR 1=1 --",
        "password": "anything"
    }
    response = requests.post("http://127.0.0.1:5000/blind-login", data=payload)
    assert response.text.strip() == "Failure", "❌ Blind SQLi succeeded on secure app when it should fail"