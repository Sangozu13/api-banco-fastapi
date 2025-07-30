import pytest
from fastapi.testclient import TestClient
from routes.banco import banco
from config.bd import conn
from bson import ObjectId

client = TestClient(banco)
collection = conn.local.Account

@pytest.fixture(autouse=True)
def cleanup_accounts():
    yield
    collection.delete_many({"nombre_titular": {"$regex": "^TEST_"}})
    

def test_create_account():
    response = client.post("/accounts", json={
        "nombre_titular": "TEST_Santiago Gómez",
        "numero_cuenta": "1234567890",
        "saldo": 1000,
        "tipo_cuenta": "Ahorros",
        "is_active": True
    })
    assert response.status_code == 200
    id = response.json()
    assert ObjectId.is_valid(id)

    db_account = collection.find_one({"_id": ObjectId(id)})
    assert db_account["nombre_titular"] == "TEST_Santiago Gómez"
    assert db_account["numero_cuenta"] == "1234567890"
    assert db_account["saldo"] == 1000
    assert db_account["tipo_cuenta"] == "Ahorros"
    assert db_account["is_active"] == True


def test_get_all_accounts():
    client.post("/accounts", json={
        "nombre_titular": "TEST_Ana",
        "numero_cuenta": "1234567890",
        "saldo": 500,
        "tipo_cuenta": "ahorros",
        "is_active": True
    })
    
    response = client.get("/accounts")
    assert response.status_code == 200
    data = response.json()

    assert any("TEST_" in cuenta["nombre_titular"] for cuenta in data)


def test_update_account():
    res = client.post("/accounts", json={
        "nombre_titular": "TEST_Carlos",
        "numero_cuenta": "9876543210",
        "saldo": 100,
        "tipo_cuenta": "corriente",
        "is_active": True
    })
    id = res.json()
    
    response = client.patch(f"/accounts/{id}", json={"saldo": 150})
    assert response.status_code == 200
    assert response.json()["saldo_actualizado"] == 250

    cuenta = collection.find_one({"_id": ObjectId(id)})
    assert cuenta["saldo"] == 250

