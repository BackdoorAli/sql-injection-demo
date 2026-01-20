import requests

def test_sql_injection_secure_app():
    payload = {
        "username": "' OR 1=1 --",
        "password": "anything"
    }
    response = requests.post("http://127.0.0.1:5000/login", data=payload)

    assert "Login failed" in response.text, "SQL Injection succeeded on the secure app when it should not have"