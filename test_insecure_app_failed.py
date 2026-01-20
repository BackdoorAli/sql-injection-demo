import requests

def test_sql_injection_insecure_app():
    payload = {
        "username": "' OR 1=1 --",
        "password": "anything"
    }
    response = requests.post("http://127.0.0.1:5000/login", data=payload)

    assert "Welcome back" in response.text, "SQL Injection test failed when it should have passed on the insecure app"