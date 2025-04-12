import requests

def test_admin_bypass_insecure():
    payload = "' OR role='admin' --"
    response = requests.get(f"http://127.0.0.1:5000/admin?username={payload}")
    assert "Welcome, Admin" in response.text, "❌ Admin bypass failed on insecure app when it should pass"