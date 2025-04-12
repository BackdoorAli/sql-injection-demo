import requests

def test_admin_bypass_secure():
    payload = "' OR role='admin' --"
    response = requests.get(f"http://127.0.0.1:5000/admin?username={payload}")
    assert "Access denied" in response.text, "❌ Admin bypass succeeded on secure app when it should fail"