1. SingletonMeta guarda una unica instancia en _instances, mientras que lock asegura que solo un hilo cree la instancia evitando asi condiciones de carrera.

2. Encapsula la creacion de null_resource el factory. Los triggers generan identificadores unicos de tiempos, permite que Terraform detecte cambios y asi regenere recursos auitomaticamente.

3.  El mutator modifica cada copia para personalizarla sin afectar el original, garantizando independencia entre instancias.


4. CompositeModule combina varios recursos en un solo JSON valido, ya que JSON tiene una estructura modular en la que permite agrupar distintos valores como valor-clave y generar mapas con estos.

5. InfrastructureBuilder usa Factory para crear, Prototype para clonar y Composite para unir. Luego exporta todo en JSON, automatizando la generación completa de infraestructura.