import os
import json
from builder import InfrastructureBuilder


def create_module_structure():
    """Crea la estructura de directorios para los módulos de Terraform."""
    base_path = "terraform/modules"

    # Crear directorio base
    os.makedirs(base_path, exist_ok=True)

    # Crear módulo network
    network_path = os.path.join(base_path, "network")
    os.makedirs(network_path, exist_ok=True)

    network_main = {
        "terraform": {
            "required_version": ">= 1.0"
        },
        "variable": {
            "cidr_block": {
                "type": "string",
                "default": "10.0.0.0/16"
            },
            "name": {
                "type": "string",
                "default": "main-vpc"
            }
        },
        "resource": {
            "null_resource": {
                "network_placeholder": {
                    "triggers": {
                        "name": "${var.name}",
                        "cidr": "${var.cidr_block}"
                    }
                }
            }
        },
        "output": {
            "vpc_name": {
                "value": "${var.name}"
            }
        }
    }

    # Crear módulo app
    app_path = os.path.join(base_path, "app")
    os.makedirs(app_path, exist_ok=True)

    app_main = {
        "terraform": {
            "required_version": ">= 1.0"
        },
        "variable": {
            "instance_count": {
                "type": "number",
                "default": 3
            },
            "app_name": {
                "type": "string",
                "default": "myapp"
            }
        },
        "resource": {
            "null_resource": {
                "app_instance": {
                    "triggers": {
                        "name": "${var.app_name}",
                        "count": "${var.instance_count}"
                    }
                }
            }
        },
        "output": {
            "app_name": {
                "value": "${var.app_name}"
            }
        }
    }

    # Escribir archivos JSON
    with open(os.path.join(network_path, "main.tf.json"), "w") as f:
        json.dump(network_main, f, indent=2)

    with open(os.path.join(app_path, "main.tf.json"), "w") as f:
        json.dump(app_main, f, indent=2)

    print(f"✓ Módulos creados en {base_path}")


def main():
    """Genera la infraestructura base usando todos los patrones."""
    create_module_structure()

    builder = InfrastructureBuilder()

    # Ejercicio 2.1: Singleton (será validado en tests)
    # Ejercicio 2.2: Factory con timestamp
    # Ejercicio 2.3: Prototipo con local_file
    builder.build_with_welcome_file()

    # Ejercicio 2.4: Submódulos con Composite
    builder.build_group("network", 2)
    builder.build_group("app", 3)

    # Ejercicio 2.5: Build_group ya implementado arriba

    builder.export()
    print("✓ Infraestructura generada en terraform/main.tf.json")


if __name__ == "__main__":
    main()
