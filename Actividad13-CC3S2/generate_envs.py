import os, json, re
from shutil import copyfile

# Lee PORT desde legacy/config.cfg
with open("legacy/config.cfg") as f:
    port_line = f.readline().strip()
    PORT = port_line.split("=")[1] if "=" in port_line else "8080"

# Lee comando desde legacy/run.sh
with open("legacy/run.sh") as f:
    lines = [l.strip() for l in f if l.strip() and not l.startswith("#!")]
    legacy_cmd = lines[-1].replace("$PORT", PORT) if lines else f"echo 'Arrancando {PORT}'"

# Parámetros de ejemplo para N entornos
ENVS = []
for i in range(1, 4):
    if i == 3:
        ENVS.append({"name": f"app{i}", "network": f"net{i-1}-peered"})
    else:
        ENVS.append({"name": f"app{i}", "network": f"net{i}"})


MODULE_DIR = "modules/simulated_app"
OUT_DIR    = "environments"
API_KEY = os.environ.get("API_KEY", "dummy_key")

def render_and_write(env):
    env_dir = os.path.join(OUT_DIR, env["name"])
    os.makedirs(env_dir, exist_ok=True)

    # 1) Copia la definición de variables desde el módulo
    network_path = os.path.join(env_dir, "network.tf.json")
    copyfile(
        os.path.join(MODULE_DIR, "network.tf.json"),
        network_path
    )

    # 2) Modifica el archivo copiado para añadir variable sensitive
    with open(network_path) as f:
        data = json.load(f)

    # Asegura que existe la clave "variable"
    if "variable" not in data:
        data["variable"] = []

    # Añade variable sensitive sin exponer valor
    data["variable"].append({
        "api_key": {
            "type": "string",
            "sensitive": True,
            "description": "Clave API sensible para el entorno"
        }
    })

    with open(network_path, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)

    # 3) Genera main.tf.json solo con recursos
    config = {
        "resource": [
            {
                "local_server": [
                    {
                        env["name"]: [
                            {
                                "triggers": {
                                    "name":    env["name"],
                                    "network": env["network"]
                                },
                                "provisioner": [
                                    {
                                        "local-exec": {
                                            "command": legacy_cmd
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

    with open(os.path.join(env_dir, "main.tf.json"), "w") as fp:
        json.dump(config, fp, sort_keys=True, indent=4)

if __name__ == "__main__":
    # Limpia entornos viejos (si quieres)
    if os.path.isdir(OUT_DIR):
        import shutil
        shutil.rmtree(OUT_DIR)

    for env in ENVS:
        render_and_write(env)
    print(f"Generados {len(ENVS)} entornos en '{OUT_DIR}/' (PORT={PORT})")