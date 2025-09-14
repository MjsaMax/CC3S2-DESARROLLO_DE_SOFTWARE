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

    ```
    CALMS: 
    Cultura: el equipo responsable del proyecto debe ser consistente respecto a las prácticas que realizan en su colaboración, un archivo representativo constaría del README.md; 
    Automatización: El Makefile para build/test/deploy se involucra en este punto, el archivo makefile representaria asi como los archivos .sh; 
    Lean: iteraciones cortas;
    Medición: endpoints de salud; 
    Sharing: runbooks/postmortems en equipo para aprender y mejorar continuamente.
   ```

3. **Visión cultural de DevOps y paso a DevSecOps:**
   Analiza colaboración para evitar silos, y evolución a DevSecOps (integrar seguridad como cabeceras TLS, escaneo dependencias en CI/CD).
   Propón escenario retador: fallo certificado y mitigación cultural. Señala 3 controles de seguridad sin contenedores y su lugar en CI/CD.

   * *Tip:* Usa el archivo de Nginx y systemd para justificar tus controles.
   ```
   Para romper silos se puede implementar DevOps para que trabajen en colaboración y halla mayor comunicación fluida entre trabajadores, ahora con la tendencia de vulnerar software se adquiere un nuevo integrante a devops que es el equipo de seguridad, el TLS aparece desde esta incorporación en los proyectos. Ahora que existe DevSecOps y falla el certificado TLS la responsabilidad es de ambos equipos en DevSecOps, por lo que se elimina culpas y fortalece colaboración.
   Tres controles de seguridad podrían ser la revicion de código entre pares, comprobación de testeos, y control de accesos del repositorio en curso.
   ```

4. **Metodología 12-Factor App:**
   Elige 4 factores (incluye config por entorno, port binding, logs como flujos) y explica implementación en laboratorio.
   Reto: manejar la ausencia de estado (statelessness) con servicios de apoyo (backing services).

   * *Tip:* No solo describas: muestra dónde el laboratorio falla o podría mejorar.

   ```
   En el laboratorio, la configuración por entorno se manejó con variables como PORT y MESSAGE evitando cambios en código. Port binding por la app Flask mediante Nginx en puertos definidos. Los logs fluyen a stdout, facilitando monitoreo por parte del desarrollador. 
   ```