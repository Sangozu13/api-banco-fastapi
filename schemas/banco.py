def account_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "nombre_titular" : item["nombre_titular"],
        "numero_cuenta" : item["numero_cuenta"],
        "saldo": item["saldo"],
        "tipo_cuenta": item["tipo_cuenta"],
        "is_active": item["is_active"]
    }
    
def accounts_entity(entity) -> list:
    return [account_entity(item) for item in entity]