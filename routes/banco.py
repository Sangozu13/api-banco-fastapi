from fastapi import APIRouter, Response, HTTPException
from models.modelo import Account, UpdateSaldoAccount
from schemas.banco import account_entity, accounts_entity
from config.bd import conn
from bson import ObjectId

banco = APIRouter()

@banco.get('/accounts')
def all_accounts():
    return accounts_entity(conn.local.Account.find())

@banco.get('/accounts/{id}')
def find_account(id: str):
    return account_entity(conn.local.Account.find_one({"_id": ObjectId(id)}))

@banco.post('/accounts')
def create_account(account: Account):
    new_account = dict(account)
    id = conn.local.Account.insert_one(new_account).inserted_id
    return str((id))

@banco.patch('/accounts/{id}')
def update_account(id: str, nuevoSaldo: UpdateSaldoAccount):
    try:
        object_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail="Formato de ID no válido")

    cuenta = conn.local.Account.find_one({"_id": object_id})
    if not cuenta:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")

    nuevo_saldo = cuenta["saldo"] + nuevoSaldo.saldo

    conn.local.Account.update_one(
        {"_id": object_id},
        {"$set": {"saldo": nuevo_saldo}}
    )

    return {"saldo_actualizado": nuevo_saldo}