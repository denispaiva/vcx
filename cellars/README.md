# Instancias de Cellar

Este es el punto de entrada de los portfolios concretos de VCX. Todavía no contiene instancias; no están decididos el nombre, propietario o ubicación del primer Cellar.

Cada instancia reúne ideas y proyectos con contexto propio, configuración, decisiones, estado y evidencia. Su responsable de custodia conserva las referencias a los almacenamientos canónicos y las condiciones de acceso y recuperación.

El [producto Cellar](../cellar/README.md) aporta estructura y mecanismos reutilizables; las instancias conservan la información concreta de B. Esta separación no duplica el código del producto.

Para preparar una instancia, partir de la [plantilla](../cellar/templates/cellar/README.md) después de acordar identidad, custodia y destino. La pertenencia lógica de una iniciativa no decide por sí sola la ubicación de su código o su repositorio. Las instancias con requisitos diferentes de confidencialidad necesitan aislamiento efectivo, no solo carpetas distintas.

Los nombres y rutas se decidirán según el [registro de decisiones](../docs/decisions/README.md). El sistema existente y su backlog continúan en sus fuentes actuales; esta carpeta no es una copia ni un reemplazo de ese portfolio.


Si la instancia se alojará en otro repositorio, resolver antes de activarla el [disparador de distribución de principios](../docs/architecture/interoperability.md#distribución-de-principios-a-instancias-externas). No se necesita implementar ese mecanismo mientras no se prepare la primera instancia externa.
