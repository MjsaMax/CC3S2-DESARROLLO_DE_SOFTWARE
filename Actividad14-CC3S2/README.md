# Estructura
``` bash
├── Actividad14-CC3S2.md
├── Fase1
│   ├── Diagrama_UML_Patrones.png
│   └── Entregable_Fase1.md
├── Fase2
│   ├── Ejercicio2_1
│   │   └── singleton.py
│   ├── Ejercicio2_2
│   │   └── factory.py
│   ├── Ejercicio2_3
│   │   └── prototype.py
│   ├── Ejercicio2_4
│   │   └── composite.py
│   └── Ejercicio2_5
│       ├── __pycache__
│       │   └── builder.cpython-312.pyc
│       └── builder.py
├── Fase3
│   ├── __pycache__
│   │   ├── builder.cpython-312.pyc
│   │   ├── composite.cpython-312.pyc
│   │   ├── factory.cpython-312.pyc
│   │   └── prototype.cpython-312.pyc
│   ├── builder.py
│   ├── composite.py
│   ├── factory.py
│   ├── generate_infra.py
│   ├── prototype.py
│   ├── singleton.py
│   ├── terraform
│   │   ├── bienvenida.txt
│   │   ├── main.tf.json
│   │   ├── modules
│   │   │   ├── app
│   │   │   │   └── main.tf.json
│   │   │   └── network
│   │   │       └── main.tf.json
│   │   └── terraform.tfstate
│   └── test_patterns.py
└── README.md
```

### Ejecucion

```bash
cd Fase3/
rm -fr terraform/*
python3 generate_infra.py
cd terraform/
terraform init
terraform plan
terraform apply
```

### test

```bash
cd Fase3/
pytest test_patterns.py
```