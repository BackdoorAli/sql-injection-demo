# SQL Injection Demo Project

A comprehensive educational demo by [Mira2720](https://github.com/Mira2720) that illustrates how SQL injection attacks work and how to properly defend against them using Flask apps.

---

## What This Project Covers

| Layer        | Feature                                                                |
|--------------|------------------------------------------------------------------------|
| Vulnerable   | Basic SQL injection on login forms                                     |
| Secure       | Defense using parameterized queries                                    |
| Dashboard    | Side-by-side comparison of vulnerable vs. secure app responses         |
| Tests        | Pytest scripts showing both failed and passing attempts                |
| Red vs Blue  | Notebook split: Attacker (Red) and Defender (Blue) perspectives        |
| Bonus        | Admin Role Bypass, API Login JSON, Blind SQL Injection support         |

---

## Project Structure

```
sql-injection-demo/
│
├── app/                       # Application code
│   ├── database.py
│   ├── insecure_app_with_advanced_routes.py
│   ├── secure_app_with_advanced_routes.py
│   └── templates/
│       └── compare.html
│
├── static/                    # CSS styles
│
├── run_insecure.py            # Run insecure app on port 5000
├── run_secure.py              # Run secure app on port 5001
├── compare_app.py             # Side-by-side dashboard on port 5002
│
├── tests/                     # Structured test cases
│   ├── test_insecure_app_failed.py
│   ├── test_insecure_app_pass.py
│   ├── test_secure_app_failed.py
│   ├── test_secure_app_pass.py
│   └── others...
│
├── demo_walkthrough_final.ipynb  # Red Team & Blue Team SQLi walkthrough
├── requirements.txt
├── Makefile
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

## Usage

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the apps in three terminal tabs:

```bash
# Tab 1
PYTHONPATH=. python3 run_insecure.py

# Tab 2
PYTHONPATH=. python3 run_secure.py

# Tab 3
PYTHONPATH=. python3 compare_app.py
```

### 3. Open your browser at:
```
http://127.0.0.1:5002/compare
```

Use this test case:
- Username: `' OR 1=1 --`
- Password: `anything`

---

## Red Team vs Blue Team Notebook

Check out `demo_walkthrough_final.ipynb` to explore:
- How the attack works (Red Team)
- How it's defended (Blue Team)
- Side-by-side code examples and query breakdown

---

## Advanced Features

- Admin Role Bypass simulation
- Blind SQL Injection test cases
- API login endpoint via JSON POST
- Separate pass/fail test files
- Code coverage and testing badge coming soon
- GitHub Pages-ready documentation `/docs` (TBD)

---

## Author

Created and maintained by [Mira2720](https://github.com/Mira2720)  
Inspired by real-world attack & defense scenarios for portfolio and recruiter demo purposes.
