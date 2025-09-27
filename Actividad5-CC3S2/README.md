# Actividad 5 - CC3S2

## Entorno utilizado
Se trabajó en Linux, con bash como shell.  
Versiones principales: `make 4.3`, `bash 5.2`, `python3 3.12`, `tar 1.35 (GNU tar)`, `sha256sum (GNU coreutils 9.4)`.  
Detalles completos en `meta/entorno.txt`.

---

## Parte 1 - Construir

Explica qué hace `build` y cómo `$(PYTHON) $< > $@` usa `$<` y `$@`.
```
 `build` genera el archivo de salida (`out/hello.txt`) a partir de la fuente (`src/hello.py`).  
En la receta, `$<` significa “la primera dependencia” (`hello.py`) y `$@` “el target” (`hello.txt`).
```

Menciona el **modo estricto** (`-e -u -o pipefail`) y `.DELETE_ON_ERROR`.
```
El modo estricto (`-e -u -o pipefail`) detiene el script si hay error, variable indefinida o fallo en un pipe.  
`.DELETE_ON_ERROR` asegura que si falla la construcción se borre el archivo incompleto.
```

Diferencia entre la 1.ª y 2.ª corrida de `build` (idempotencia).
```
En la primera corrida se genera el archivo.  

En la segunda, Make detecta que no hubo cambios y no lo vuelve a generar (ejecución idempotente).
```



## Parte 2 - Leer

Qué observaste con `make -n` y `make -d` (decisiones de rehacer o no).
```
`make -n` muestra qué comandos se ejecutarían sin correrlos.  
`make -d` detalla cómo Make decide si rehacer o no en base a timestamps.
```

Rol de `.DEFAULT_GOAL`, `.PHONY` y ayuda autodocumentada.
```
`.DEFAULT_GOAL := help` muestra por defecto la ayuda en vez de otro target.  
`.PHONY` marca targets que no corresponden a archivos reales (ej. `help`, `clean`).  
```


## Parte 3 - Extender

Qué detectó `shellcheck`/`shfmt` (o evidencia de que no están instalados). 
```
`shellcheck` detecta malas prácticas o errores en scripts bash, y `shfmt` formatea el código.  
Si no están instalados, Make procederá a mostrar el aviso correspondiente.
```
Demostración de **rollback** con `trap` (códigos de salida y restauración).
```
Con `trap` se captura un fallo (exit code ≠ 0), se limpian archivos temporales y se restauran los originales.
```
**Reproducibilidad**: factores que la garantizan (`--sort`, `--mtime`, `--numeric-owner`, `TZ=UTC`) y el resultado de `verify-repro`.
```
Se usaron opciones `--sort=name --mtime=@0 --numeric-owner`, junto con `gzip -n` y `TZ=UTC`.  
Gracias a eso, `make verify-repro` dio hashes idénticos en reiteradas ejecuciones.
```
* **Incidencias y mitigaciones**: cualquier problema y cómo lo resolviste.
```
Al inicio faltaban herramientas como shellcheck y shfmt, lo que impedía ejecutar make tools.
Se resolvió instalando los paquetes
```
* **Conclusión operativa**: 2-3 líneas sobre por qué el pipeline es apto para CI/CD.
```
El pipeline es apto para CI/CD porque es reproducible, estricto y detecta errores temprano.
Cabe mencionar que integra validaciones automáticas linting,formateo o rollback.
Uso correcto de git para el control de versiones.
```