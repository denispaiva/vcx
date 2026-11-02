# Instancias de Cellar

Este es el punto de entrada de los portfolios concretos de VCX. Todavía no contiene instancias. El primer Cellar se llama Solera, según VCX-D009; su propietario y su ubicación siguen pendientes.

Cada instancia reúne ideas y proyectos con contexto propio, configuración, decisiones, estado y evidencia. Su responsable de custodia conserva las referencias a los almacenamientos canónicos y las condiciones de acceso y recuperación. La instancia custodia íntegra en todas las etapas y conduce sus proyectos graduados con sus Product Owners (PO), bajo el método de Blends; registra dónde vive el código de cada proyecto sin alojarlo. Una propuesta en preparación puede custodiarse antes de elegir instancia y queda fuera del portfolio activo hasta la confirmación humana de ingreso.

El [producto Cellar](../cellar/README.md) aporta estructura y mecanismos reutilizables; las instancias conservan la información concreta de B. Esta separación no duplica el código del producto.

Para preparar una instancia, partir de la [plantilla](../cellar/templates/cellar/README.md) después de acordar identidad, custodia y destino. El código de cada proyecto vive en su propio repositorio, según VCX-D029; la instancia registra esa ubicación. Las instancias con requisitos diferentes de confidencialidad necesitan aislamiento efectivo, no solo carpetas distintas.

Los nombres y rutas se decidirán según el [registro de decisiones](../docs/decisions/README.md). El sistema existente y su backlog continúan en sus fuentes actuales; esta carpeta no es una copia ni un reemplazo de ese portfolio.


Si la instancia se alojará en otro repositorio, resolver antes de activarla el [disparador de distribución de principios](../docs/architecture/interoperability.md#distribución-de-principios-a-instancias-externas). No se necesita implementar ese mecanismo mientras no se prepare la primera instancia externa.
