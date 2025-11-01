from copy import deepcopy
from typing import Callable


class ResourcePrototype:
    def __init__(self, template: dict):
        self.template = template

    def clone(self, mutator: Callable[[dict], None]) -> dict:
        """Clona profundamente el template y aplica el mutator."""
        new_copy = deepcopy(self.template)
        mutator(new_copy)
        return new_copy


def add_welcome_file(block: dict):
    """
    Mutator que agrega:
    - Trigger en null_resource con contenido de bienvenida
    - Recurso local_file que crea bienvenida.txt
    """
    # Asegura que exista la estructura necesaria
    if "resource" not in block:
        block["resource"] = {}
    if "null_resource" not in block["resource"]:
        block["resource"]["null_resource"] = {}
    if "local_file" not in block["resource"]:
        block["resource"]["local_file"] = {}
    
    # Agrega trigger de bienvenida a null_resource.app_0
    if "app_0" not in block["resource"]["null_resource"]:
        block["resource"]["null_resource"]["app_0"] = {"triggers": {}}
    
    if "triggers" not in block["resource"]["null_resource"]["app_0"]:
        block["resource"]["null_resource"]["app_0"]["triggers"] = {}
    
    block["resource"]["null_resource"]["app_0"]["triggers"]["welcome"] = "¡Hola!"
    
    # Agrega recurso local_file para crear bienvenida.txt
    block["resource"]["local_file"]["welcome_txt"] = {
        "content": "Bienvenido",
        "filename": "${path.module}/bienvenida.txt"
    }
