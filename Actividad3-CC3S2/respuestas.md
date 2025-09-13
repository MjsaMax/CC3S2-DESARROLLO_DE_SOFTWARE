#### Parte teórica

1. **Introducción a DevOps: ¿Qué es y qué no es?**
   Explica DevOps desde el código hasta la producción, diferenciándolo de waterfall. Discute "you build it, you run it" en el laboratorio, y separa mitos (ej. solo herramientas) vs realidades (CALMS, feedback, métricas, gates).

   * *Tip:* Piensa en ejemplos concretos: ¿cómo se vería un gate de calidad en tu Makefile?

   ```
   DevOps es el conjunto de constumbres en las que deben desarrollar en equipo, el area de Delopment y de Operaciones, ambos compartiendo los mismos objetivos, su flujo va desde codigo, pruebas, integracion continua,despliegue a monitoreo de este,.A diferencia de waterfall este administra un flujo mas dinamico, conteniendo asi mayor cantidad de iteraciones para desarrollar el producto, mientras que waterfall, beneficiado de objetivos concretos, tiende a pasar de un proceso a otro solo una vez por proyecto.
   ```

2. **Marco CALMS en acción:**
   Describe cada pilar y su integración en el laboratorio (ej. Automation con Makefile, Measurement con endpoints de salud). Propón extender Sharing con runbooks/postmortems en equipo.

   * *Tip:* Relaciona cada letra de CALMS con un archivo del laboratorio.

3. **Visión cultural de DevOps y paso a DevSecOps:**
   Analiza colaboración para evitar silos, y evolución a DevSecOps (integrar seguridad como cabeceras TLS, escaneo dependencias en CI/CD).
   Propón escenario retador: fallo certificado y mitigación cultural. Señala 3 controles de seguridad sin contenedores y su lugar en CI/CD.

   * *Tip:* Usa el archivo de Nginx y systemd para justificar tus controles.

4. **Metodología 12-Factor App:**
   Elige 4 factores (incluye config por entorno, port binding, logs como flujos) y explica implementación en laboratorio.
   Reto: manejar la ausencia de estado (statelessness) con servicios de apoyo (backing services).

   * *Tip:* No solo describas: muestra dónde el laboratorio falla o podría mejorar.
