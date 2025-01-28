import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class FlaskAppSecurityTestCase(unittest.TestCase):

    def test_idor_attack(self):
        """ Test for Insecure Direct Object References (IDOR) vulnerability """
        response = requests.get(f"{BASE_URL}/user/1")
        self.assertNotEqual(response.status_code, 200, "IDOR vulnerability detected: Unauthorized user access allowed")

    def test_access_control(self):
        """ Test for Broken Access Control vulnerability """
        headers = {"Authorization": "Bearer invalid_token"}
        response = requests.get(f"{BASE_URL}/user/1", headers=headers)
        self.assertEqual(response.status_code, 401, "Access control missing: Unauthorized access allowed")

    def test_sensitive_data_exposure(self):
        """ Test for Sensitive Data Exposure vulnerability """
        response = requests.get(f"{BASE_URL}/user/1")
        response_data = response.json()
        self.assertNotIn("password_hash", response_data, "Sensitive data exposure: password_hash found in response")

    def test_sql_injection(self):
        """ Test for SQL Injection vulnerability """
        response = requests.get(f"{BASE_URL}/user/1' OR '1'='1")
        self.assertNotEqual(response.status_code, 200, "SQL Injection vulnerability detected")

    def test_input_validation(self):
        """ Test for Improper Input Validation vulnerability """
        response = requests.get(f"{BASE_URL}/user/abc")
        self.assertEqual(response.status_code, 400, "Improper input validation: Non-integer values should return 400")

    def test_rate_limiting(self):
        """ Test for Rate Limiting to prevent brute-force attacks """
        for _ in range(1000):
            response = requests.get(f"{BASE_URL}/user/1")
            if response.status_code == 429:
                break
        self.assertEqual(response.status_code, 429, "Rate limiting not implemented")

    def test_authentication_bypass(self):
        """ Test for Authentication Bypass vulnerability """
        response = requests.get(f"{BASE_URL}/user/1")
        self.assertEqual(response.status_code, 401, "Authentication bypass detected")

    def test_xss_attack(self):
        """ Test for Cross-Site Scripting (XSS) vulnerability """
        payload = "<script>alert('XSS')</script>"
        response = requests.get(f"{BASE_URL}/user/{payload}")
        self.assertNotIn("<script>", response.text, "XSS vulnerability detected in response")

    def test_error_handling(self):
        """ Test for Improper Error Handling to prevent information leakage """
        response = requests.get(f"{BASE_URL}/user/999999999")
        self.assertNotIn("Internal Server Error", response.text, "Server error details leaked")

    def test_security_headers(self):
        """ Test for missing security headers """
        response = requests.get(f"{BASE_URL}/user/1")
        self.assertIn("X-Content-Type-Options", response.headers, "Security headers missing")

if __name__ == '__main__':
    unittest.main()
