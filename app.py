from fastapi import FastAPI
from routes.bank_routes import bank

app = FastAPI(
    title="API Bancaria",
    description="API for bank account management.",
    version="1.0.0",
)
app.include_router(bank, tags=["Bank Accounts"])