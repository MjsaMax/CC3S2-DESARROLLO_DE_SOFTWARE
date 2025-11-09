import pytest
import json
from pathlib import Path

# Obtener la ruta del directorio donde está este archivo
TEST_DIR = Path(__file__).parent
CONFIG_FILE = TEST_DIR / 'network_config.json'

@pytest.fixture(scope="module")
def conf():
    return json.load(open(CONFIG_FILE))

def test_schema_keys(conf):
    """Verifica que el archivo de configuración tenga las claves esperadas"""
    expected_keys = ["network_id", "subnets", "status"]
    
    for key in expected_keys:
        assert key in conf, f"Falta la clave '{key}' en la configuración"
    
    # Verifica que subnets sea una lista
    assert isinstance(conf["subnets"], list), "subnets debe ser una lista"
    
    # Verifica que cada subnet tenga las claves necesarias
    subnet_keys = ["subnet_id", "cidr", "available_ips"]
    for subnet in conf["subnets"]:
        for key in subnet_keys:
            assert key in subnet, f"Falta la clave '{key}' en una subnet"
