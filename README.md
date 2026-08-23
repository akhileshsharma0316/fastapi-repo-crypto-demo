# Building a Secure FastAPI App: Repository Pattern & AES-GCM Encryption

This repository serves as the companion codebase for the Medium article: **"Clean Architecture & Cryptographic Security in FastAPI: Repository Pattern & AES-GCM Encryption"**.

It demonstrates how to decouple data persistence from business logic using the **Repository Pattern** while implementing authenticated symmetric encryption using **AES-256-GCM** to secure sensitive payload data at rest.

---

## Key Takeaways & Core Objectives

1. **Repository Pattern Implementation:** Abstract SQLAlchemy ORM logic away from FastAPI path operations, allowing seamless database swapping, cleaner unit testing, and isolated data access.
2. **Symmetric Payload Encryption (AES-GCM):** Secure sensitive crypto/financial data before writing to SQLite using **Galois/Counter Mode (GCM)**, providing both **confidentiality** and **authenticated integrity verification**.
3. **Clean Code Architecture:** Strict separation between routes, business logic, ORM models, Pydantic data validation schemas, and cryptographic utils.