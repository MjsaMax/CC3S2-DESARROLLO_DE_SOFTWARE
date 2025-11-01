import pytest
from singleton import ConfigSingleton
from factory import NullResourceFactory, TimestampedNullResourceFactory
from prototype import ResourcePrototype
from composite import CompositeModule
from builder import InfrastructureBuilder


# Ejercicio 2.1: Test Singleton reset()
def test_singleton_reset():
    """Valida que reset() limpia settings pero mantiene created_at."""
    c1 = ConfigSingleton("dev")
    created = c1.created_at
    c1.settings["x"] = 1
    c1.reset()
    assert c1.settings == {}
    assert c1.created_at == created
    print("✓ test_singleton_reset PASSED")


def test_singleton_meta():
    """Valida que SingletonMeta garantiza una sola instancia."""
    a = ConfigSingleton("X")
    b = ConfigSingleton("Y")
    assert a is b
    print("✓ test_singleton_meta PASSED")


# Ejercicio 2.2: Test TimestampedNullResourceFactory
def test_timestamped_factory():
    """Valida que TimestampedNullResourceFactory usa strftime correctamente."""
    resource = TimestampedNullResourceFactory.create("test_app", "%Y%m%d")
    triggers = resource["resource"]["null_resource"]["test_app"]["triggers"]
    assert "timestamp" in triggers
    assert len(triggers["timestamp"]) == 8  # YYYYMMDD format
    print("✓ test_timestamped_factory PASSED")


# Ejercicio 2.3: Test Prototype con mutator
def test_prototype_clone_independent():
    """Valida que clones independientes no se afectan mutuamente."""
    proto = ResourcePrototype(NullResourceFactory.create("app"))

    def mutator1(block):
        block["f1"] = 1

    def mutator2(block):
        block["b1"] = 2

    c1 = proto.clone(mutator1)
    c2 = proto.clone(mutator2)

    assert "f1" in c1 and "f1" not in c2
    assert "b1" in c2 and "b1" not in c1
    print("✓ test_prototype_clone_independent PASSED")


def test_prototype_with_local_file():
    """Valida que mutator puede agregar local_file a un null_resource."""
    base = NullResourceFactory.create("app")
    proto = ResourcePrototype(base)

    def add_welcome_file(block):
        block["resource"]["null_resource"]["app"]["triggers"]["welcome"] = "¡Hola!"
        block["resource"]["local_file"] = {
            "welcome_txt": {
                "content": "Bienvenido",
                "filename": "${path.module}/bienvenida.txt"
            }
        }

    cloned = proto.clone(add_welcome_file)
    assert "local_file" in cloned["resource"]
    assert "welcome_txt" in cloned["resource"]["local_file"]
    print("✓ test_prototype_with_local_file PASSED")


# Ejercicio 2.4: Test Composite con módulos
def test_composite_with_modules():
    """Valida que Composite agrupa recursos y módulos correctamente."""
    composite = CompositeModule()

    # Agregar recursos
    composite.add({"resource": {"null_resource": {"res1": {"triggers": {}}}}})
    composite.add({"resource": {"null_resource": {"res2": {"triggers": {}}}}})

    # Agregar módulos
    composite.add({"module": {"network": {"resource": {"null_resource": {"net": {}}}}}})

    exported = composite.export()

    assert "resource" in exported
    assert "null_resource" in exported["resource"]
    assert "res1" in exported["resource"]["null_resource"]
    assert "res2" in exported["resource"]["null_resource"]
    assert "module" in exported
    assert "network" in exported["module"]
    print("✓ test_composite_with_modules PASSED")


# Ejercicio 2.5: Test Builder con build_group
def test_builder_build_group():
    """Valida que build_group genera estructura module -> name -> resource."""
    builder = InfrastructureBuilder()
    builder.build_group("network", 2)

    exported = builder.module.export()

    assert "module" in exported
    assert "network" in exported["module"]
    print("✓ test_builder_build_group PASSED")


def test_builder_integration():
    """Valida que builder orquesta correctamente todos los patrones."""
    builder = InfrastructureBuilder()
    builder.build_with_welcome_file()
    builder.build_group("app", 2)

    exported = builder.module.export()

    # Validar que tiene recursos
    assert "resource" in exported
    assert "local_file" in exported["resource"]

    # Validar que tiene módulos
    assert "module" in exported
    assert "app" in exported["module"]
    print("✓ test_builder_integration PASSED")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("Ejecutando tests de Actividad 14-CC3S2 Fase 2")
    print("="*60 + "\n")

    test_singleton_reset()
    test_singleton_meta()
    test_timestamped_factory()
    test_prototype_clone_independent()
    test_prototype_with_local_file()
    test_composite_with_modules()
    test_builder_build_group()
    test_builder_integration()

    print("\n" + "="*60)
    print("✓ TODOS LOS TESTS PASARON")
    print("="*60 + "\n")
