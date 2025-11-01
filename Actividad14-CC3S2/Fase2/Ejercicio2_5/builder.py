import json
from composite import CompositeModule
from factory import NullResourceFactory, TimestampedNullResourceFactory
from prototype import ResourcePrototype


class InfrastructureBuilder:
    def __init__(self):
        self.module = CompositeModule()

    def build_null_fleet(self, count: int):
        """Construye una flota de null_resource clonados y mutados."""
        base = NullResourceFactory.create("app")
        proto = ResourcePrototype(base)
        for i in range(count):
            def mutator(block, idx=i):
                res = block["resource"]["null_resource"].pop("app")
                block["resource"]["null_resource"][f"app_{idx}"] = res
            self.module.add(proto.clone(mutator))
        return self

    def build_group(self, name: str, size: int):
        """Construye un grupo de recursos dentro de un submódulo.

        Ahora genera módulos con estructura Terraform válida:
        - source apunta al módulo
        - Los recursos se quedan en la raíz, no dentro del módulo
        """
        # Generar recursos individuales para este grupo
        base = NullResourceFactory.create(name)
        proto = ResourcePrototype(base)

        for i in range(size):
            def mutator(block, idx=i, group_name=name):
                res = block["resource"]["null_resource"].pop(group_name)
                block["resource"]["null_resource"][f"{group_name}_{idx}"] = res

            self.module.add(proto.clone(mutator))

        self.module.add({
            "module": {
                name: {
                    "source": f"./modules/{name}"
                }
            }
        })
        return self

    def build_with_welcome_file(self):
        """Agrega un recurso local_file con contenido de bienvenida."""
        base = NullResourceFactory.create("app")
        proto = ResourcePrototype(base)

        def mutator(block):
            block["resource"]["null_resource"]["app"]["triggers"]["welcome"] = "¡Hola!"
            block["resource"]["local_file"] = {
                "welcome_txt": {
                    "content": "Bienvenido a la infraestructura IaC con patrones",
                    "filename": "${path.module}/bienvenida.txt"
                }
            }

        self.module.add(proto.clone(mutator))
        return self

    def export(self, path: str = "terraform/main.tf.json"):
        """Exporta la infraestructura construida a un archivo JSON."""
        with open(path, "w") as f:
            json.dump(self.module.export(), f, indent=2)
