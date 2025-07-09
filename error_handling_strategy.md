# Error Handling & Security Strategy

## 1. Missing Parameters
FastAPI handles missing required query parameters automatically by returning HTTP 422. We tested `/products` and `/outlets` endpoints without any query and confirmed this behavior.

## 2. API Downtime
We simulated API backend failure (e.g., raising an exception inside a route). This triggers an HTTP 500 response, which is handled gracefully with a user-friendly error message.

## 3. Malicious Input
Malicious inputs like SQL injection patterns (`'; DROP TABLE users;--`) are not interpreted as commands or code. Our endpoints treat them as plain text and respond securely without error or exposure.

## 4. Bot Behavior
The chatbot does not crash on invalid inputs. It prompts users to clarify instead of failing silently or exposing internal logic.

## 5. General Practices
- Wrapped endpoints in try-except blocks to catch and return controlled error responses.
- Sanitized bot and API inputs to ensure safe text handling.
- No sensitive logs or internal errors exposed to the user.
