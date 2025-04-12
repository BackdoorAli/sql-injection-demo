# Makefile for SQL Injection Demo Project

.PHONY: build run run-secure down test

build:
	docker compose build

run:
	docker compose up -d

run-secure:
	APP_MODE=secure docker compose up -d

down:
	docker compose down

test:
	pytest test_sql_injection.py