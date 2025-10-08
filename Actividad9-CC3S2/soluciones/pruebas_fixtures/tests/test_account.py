import json
import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models import db
from models.account import Account , DataValidationError

ACCOUNT_DATA = {}

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Configura la base de datos antes y después de todas las pruebas"""
    # Se ejecuta antes de todas las pruebas
    db.create_all()
    yield
    # Se ejecuta después de todas las pruebas
    db.session.close()

class TestAccountModel:
    """Modelo de pruebas de cuenta"""

    @classmethod
    def setup_class(cls):
        """Conectar y cargar los datos necesarios para las pruebas"""
        global ACCOUNT_DATA
        with open("tests/fixtures/account_data.json") as json_data:
            ACCOUNT_DATA = json.load(json_data)
        print(f"ACCOUNT_DATA cargado: {ACCOUNT_DATA}")

    @classmethod
    def teardown_class(cls):
        """Desconectar de la base de datos"""
        pass  # Agrega cualquier acción de limpieza si es necesario

    def setup_method(self):
        """Truncar las tablas antes de cada prueba"""
        db.session.query(Account).delete()
        db.session.commit()

    def teardown_method(self):
        """Eliminar la sesión después de cada prueba"""
        db.session.remove()

    #  Casos de prueba
    def test_create_an_account(self):
        """Probar la creación de una sola cuenta"""
        data = ACCOUNT_DATA[0]  # obtener la primera cuenta
        account = Account(**data)
        account.create()
        assert len(Account.all()) == 1

    def test_create_all_accounts(self):
        """Probar la creación de múltiples cuentas"""
        for data in ACCOUNT_DATA:
            account = Account(**data)
            account.create()
        assert len(Account.all()) == len(ACCOUNT_DATA)

    def test__repr__(self):
        test_account = Account(name="Ejemplo")
        assert "<Account 'Ejemplo'>" ==test_account.__repr__()

    def test__to_dict(self):
        test_account = Account(id=1, name="Ejemplo")
        resultado = test_account.to_dict()
        assert isinstance(resultado, dict)
        assert resultado["id"] == 1
        assert resultado["name"] == "Ejemplo"

    def test__from_dict(self):
        test_account = Account()
        data = {"id": 1, "name": "Ejemplo", "email": "test@example.com"}
        test_account.from_dict(data)

        assert test_account.id == 1
        assert test_account.name == "Ejemplo"
        assert test_account.email == "test@example.com"

    def test_update_con_id(self):

        account = Account(id=1, name="Ejemplo")
        account.update()
        # Si no lanza error, la prueba pasa
        assert True

    def test_update_sin_id(self):

        cuenta = Account(name="SinID")
        try:
            cuenta.update()
        except DataValidationError as e:
            assert str(e) == "Se llamó a update sin un ID"


    def test_delete_account(self):
        # Crear y guardar una cuenta
        account = Account(name="Cuenta de prueba")
        db.session.add(account)
        db.session.commit()

        account_id = account.id
        assert account_id is not None

        account.delete()

        deleted_account = Account.query.get(account_id)
        assert deleted_account is None

    def test_find_account(self):

        account = Account(name="Cuenta encontrada")
        db.session.add(account)
        db.session.commit()

        account_id = account.id
        assert account_id is not None

        found = Account.find(account_id)

        assert found is not None
        assert found.id == account_id
        assert found.name == "Cuenta encontrada"

        not_found = Account.find(999999)
        assert not_found is None

