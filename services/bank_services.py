from bson import ObjectId
from config.bd import conn
from fastapi import HTTPException
from models.bank_models import Account, UpdateSaldoAccount
from schemas.bank_schemas import account_entity, accounts_entity


def get_all_accounts():
    return accounts_entity(conn.local.Account.find())


def get_account_by_id(id: str):
    return account_entity(conn.local.Account.find_one({"_id": ObjectId(id)}))


def create_new_account(account: Account):
    new_account = dict(account)
    id = conn.local.Account.insert_one(new_account).inserted_id
    return str(id)


def update_account_balance(id: str, newBalance: UpdateSaldoAccount):
    try:
        object_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail="Formato de ID no válido")

    account = conn.local.Account.find_one({"_id": object_id})
    if not account:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")

    new_balance = account["saldo"] + newBalance.saldo

    conn.local.Account.update_one(
        {"_id": object_id},
        {"$set": {"saldo": new_balance}}
    )

    return {"saldo_actualizado": new_balance}
