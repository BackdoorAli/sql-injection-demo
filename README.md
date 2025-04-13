# SQL Injection Demo Web App

A deliberately vulnerable web application that demonstrates how SQL injection works, how it can be exploited, and how to properly secure an application against it.

**Author:** [@BackdoorAli](https://github.com/Mira2720)

---

## Features

- Two app versions: `insecure_app.py` (vulnerable) and `secure_app.py` (safe)
- Simple login and search system built with Flask and SQLite
- SQL injection demonstration with clear test cases
- Docker support with multi-stage build and runtime toggle
- Bootstrap UI for improved visuals
- Jupyter notebook walkthrough
- GitHub Actions CI pipeline
- Makefile and docker-compose for local workflow

---

## Folder Structure

```
sql-injection-demo/
├── app/                       # Core application (secure + insecure)
├── templates/                 # HTML templates (login, search, results)
├── static/                    # Optional styling
├── tests/                     # Includes pass/fail injection test cases
├── Dockerfile                 # Multi-stage container setup
├── docker-compose.yml         # Simplified container management
├── Makefile                   # Shortcut commands
├── demo_walkthrough.ipynb     # Step-by-step notebook explanation
├── resume_summary.md          # Bullet-point resume description
└── README.md                  # This file
```

---

## Test Coverage Overview

| Test File                      | Description                              | Target App      | Expected Result        |
|-------------------------------|------------------------------------------|------------------|------------------------|
| `test_insecure_app_failed.py` | Uses SQL injection to bypass login       | Insecure App     | ✅ Injection should succeed |
| `test_insecure_app_pass.py`   | Tests login with correct credentials     | Insecure App     | ✅ Should allow login  |
| `test_secure_app_failed.py`   | Uses SQL injection to bypass login       | Secure App       | ✅ Injection should fail |
| `test_secure_app_pass.py`     | Tests login with correct credentials     | Secure App       | ✅ Should allow login  |

---

## Docker Usage

### Build and Run Insecure App:
```bash
docker build -t sql-demo .
docker run -p 5000:5000 sql-demo
```

### Run Secure Version:
```bash
docker run -e APP_MODE=secure -p 5000:5000 sql-demo
```

### Using Docker Compose:
```bash
docker compose up --build
```

To run secure app with compose:
```bash
APP_MODE=secure docker compose up --build
```

---

## Makefile Shortcuts

```bash
make build         # Build container
make run           # Run insecure version
make run-secure    # Run secure version
make down          # Stop containers
make test          # Run pytest manually
```

---

## Resume Summary

Check `resume_summary.md` for a clean, bullet-point summary of this project.

---

## Educational Notebook

Open `demo_walkthrough.ipynb` to see a detailed, step-by-step explanation of the vulnerability, exploit, and mitigation.

---

## Additional Advanced Test Coverage

| Test File                            | Description                                | Target App      | Expected Result        |
|-------------------------------------|--------------------------------------------|------------------|------------------------|
| `test_insecure_blind_login.py`      | Blind SQLi using form login                | Insecure App     | ✅ Injection should succeed |
| `test_secure_blind_login.py`        | Blind SQLi using form login                | Secure App       | ✅ Injection should fail |
| `test_insecure_admin_bypass.py`     | SQLi bypass of admin role                  | Insecure App     | ✅ Injection should succeed |
| `test_secure_admin_bypass.py`       | SQLi bypass of admin role                  | Secure App       | ✅ Injection should fail |
| `test_insecure_api_login.py`        | JSON API login with SQLi                   | Insecure App     | ✅ Injection should succeed |
| `test_secure_api_login.py`          | JSON API login with SQLi                   | Secure App       | ✅ Injection should fail |

---

## ⚠️ Note on GitHub Actions Test Failures

Some test cases in this project are **intentionally designed to fail** to simulate vulnerabilities like:

- SQL Injection
- Admin Role Bypass
- Blind SQL Injection

Because of this, the GitHub Actions CI workflow may report test failures.  
This is **expected behavior** for educational purposes and does not indicate problems with the project's implementation.

> These failures showcase real-world attack scenarios and are part of the intended design.
