Un archivo `README.md` que explique:
     - El propósito de la actividad.
     La actividad realizada profundiza la manipulacion de archivos terraform '*.tf' se ejecuta con cambios de variables siguiente el flujo correspondiente:
     terraform init -> terraform plan -> terraform apply 
     Ademas se modifica el script python que genera 10 entornos
     - La estructura de los archivos y carpetas.
     ```
     Actividad13-CC3S2/
     ├── modules/
     │   └── simulated_app/
     │       ├── network.tf.json
     │       └── main.tf.json
     ├── environments/
     │   ├── app1/
     │   │   ├── network.tf.json
     │   │   └── main.tf.json
     │   ├── app2/
     │   │   ├── network.tf.json
     │   │   └── main.tf.json
     │   └── env3/
     │       ├── network.tf.json
     │       └── main.tf.json
     ├── legacy/
     │   ├── config.cfg
     │   └── run.sh
     ├── scripts/
     │   └── gitops_regenerate.sh  # Para GitOps Local (ejercicio 4)
     ├── generate_envs.py
     ├── .git/
     ├── .pre-commit-config.yaml  # Hook de pre-commit (ejercicio 4)
     └── README.md
     ```
     - Instrucciones para ejecutar el proyecto ( source temp/bin/activate ->  `python generate_envs.py` -> (por cada entorno -> ) `terraform init`  -> `terraform plan`).
     - Respuestas a las preguntas de la **Fase 1**:
		  * ¿Cómo interpreta Terraform el cambio de variable?
			Genera una actualizacion de la variable, es decir no llega a colapsarse.
		  * ¿Qué diferencia hay entre modificar el JSON vs. parchear directamente el recurso?
		 	 Puede llegar a corromperse ya que el comando terraform tambien llega a establecer dependencias y verificaciones de esta para que produzca correctamente la infraestructura.
		  * ¿Por qué Terraform no recrea todo el recurso, sino que aplica el cambio "in-place"?
		 	 Si es posible que lo haga, depende del programador, en este caso terraform modifica in-place porque le hemos indicado que lo haga, y este es una buena practica debido a que se esta manipulando una variable.
		  * ¿Qué pasa si editas directamente `main.tf.json` en lugar de la plantilla de variables?
			El efecto de cambio solo se dará al app1 y no para los demas entornos.
     - Respuestas a las preguntas abiertas de la **Fase 4**:
	   * ¿Cómo extenderías este patrón para 50 módulos y 100 entornos?
	    dependiendo de la configuracion del script que hace python se generaria tanto personalizables como automaticos, y por la parte literal automatizaria la ejecucion de terraform para inicializarlos. 
	   * ¿Qué prácticas de revisión de código aplicarías a los `.tf.json`?
	    el comando terraform fmt para verificar el formateo, con un linter JSON.
	   * ¿Cómo gestionarías secretos en producción (sin Vault)?
	    generaria variables que pondria en el .gitignore para evitar que se muestre publicamente.
	   * ¿Qué workflows de revisión aplicarías a los JSON generados?
		terraform fmt -> terraform validate -> tflint -> tfsec
