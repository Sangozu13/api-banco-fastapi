from fastapi import APIRouter
from models.bank_models import Account, UpdateSaldoAccount
from services.bank_services import (
    get_all_accounts,
    get_account_by_id,
    create_new_account,
    update_account_balance,
)

bank = APIRouter()

@bank.get('/accounts')
def all_accounts():
    return get_all_accounts()


@bank.get('/accounts/{id}')
def find_account(id: str):
    return get_account_by_id(id)


@bank.post('/accounts')
def create_account(account: Account):
    return create_new_account(account)


@bank.patch('/accounts/{id}')
def update_account(id: str, newBalance: UpdateSaldoAccount):
    return update_account_balance(id, newBalance)
