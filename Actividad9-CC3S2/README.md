
# ACTIVIDAD 9
## Creacion del entorno virtual python
```bash
python3 -m venv venv
source venv/bin/activate
```
## Instalando dependencias

```bash
pip install -r requirements.txt
```
## Ejecutar todas las pruebas
```bash
make test_all
```

## Ejecutar pruebas con cobertura
```bash
make coverage_individual
```
# ACTIVIDAD: Aserciones_Pruebas

![asercopme](evidencias/aserciones_pruebas.png)

# ACTIVIDAD: coverage_pruebas

**Documentar las observaciones:** No se han encontrado pruebas con coverturas menores que 100%.
```
Ejecuta nuevamente make test y make coverage_individual para verificar que el nuevo método está completamente cubierto por pruebas.
```
![imagendecovertura](evidencias/coverage_pruebas/Covertura100.png)

# ACTIVIDAD: factories_fakes

![](evidencias/factories_fakes/EjecucióndePytest.png)

![](evidencias/factories_fakes/factories_fakes1.png)
![](evidencias/factories_fakes/factories_fakes2.png)
![](evidencias/factories_fakes/factories_fakes3.png)
![](evidencias/factories_fakes/factories_fakes4.png)
![](evidencias/factories_fakes/factories_fakes5.png)
![](evidencias/factories_fakes/factories_fakes6.png)
![](evidencias/factories_fakes/factories_fakes7.png)
![](evidencias/factories_fakes/factories_fakes8.png)

'''
Resultados despues de verificar los tests:
'''

![](evidencias/factories_fakes/factories_fakes9.png)

# ACTIVIDAD: mocking_objetos

### test_movie_reviews_failure:
![](evidencias/mocking_objetos/test_movie_reviews_failure.png)
### test_movie_ratings_failure:
![](evidencias/mocking_objetos/test_movie_ratings_failure.png)

## Resultados:
![](evidencias/mocking_objetos/RESULTADO_mocking_objetos.png)

# ACTIVIDAD: practica_tdd

### test_update_counter_failure

![](evidencias/practica_tdd/test_update_couter_failure.png)

![](evidencias/practica_tdd/test_delete_counter_failure.png)

## Resultados:
![](evidencias/practica_tdd/test_oractica_tdd.png)

# ACTIVIDAD: pruebas_fixtures

![](evidencias/pruebas_fixtures/metodostest.png)

![](evidencias/pruebas_fixtures/metodos2.png)

## Resultados:

![](evidencias/pruebas_fixtures/test_pruebas_fixtures.png)

# ACTIVIDAD: pruebas_pytest

## Resultados:

![](evidencias/pruebas_pytest/Ejecucion_Test.png)

```
pytest -v
```
![](evidencias/pruebas_pytest/pytest_v.png)

**Explicación breve de la actividad:**
Aserciones:La parte de aserciones se implementó cada vez que se verifican las salidas o statements de los metodos de una clase en python.
Fixtures: Los fixtures automatizaron la configuración inicial y limpieza posterior en cada prueba ejecutada usando bases de datos.
Factories/Fakes: Se implementó factories para generar datos de prueba aleatorios para conseguir un gran volumen de datos para las pruebas.
Coverage: Utilicé coverage al medir qué líneas ejecutaban mis tests, logrando así cobertura total.
Mocking: Usé mocks para simular respuestas externas sin depender de servicios reales durante los tests.
TDD: Seguí el ciclo TDD escribiendo primero tests fallidos que luego fuí implementando código y refactorizando, para que tenga mismo comportamiento, pero mejor estructura.
