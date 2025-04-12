import requests

def test_correct_login_insecure_app():
    payload = {
        "username": "admin",
        "password": "admin123"
    }
    response = requests.post("http://127.0.0.1:5000/login", data=payload)

    assert "Welcome back" in response.text, "✅ Correct login passed on insecure app"