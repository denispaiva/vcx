# Solera

Solera es la instancia de Cellar de este workspace: el portfolio privado con sus ideas, proyectos, decisiones, estado y evidencia. Su nombre, repositorio privado `denispaiva/solera`, propietario y ubicación se fijan en VCX-D009, VCX-D036 y VCX-D053. La carpeta `solera/` es su checkout local y hay una instancia por workspace; otro portfolio o equipo usa su propio `vcx/`.

Esta carpeta está ignorada por la raíz pública, salvo este README. El repositorio de la instancia todavía no existe: hasta la migración, el sistema y el backlog vigentes siguen en el precursor. Esta carpeta no los copia ni los reemplaza.

Solera custodia íntegra en todas las etapas y conduce sus proyectos graduados con sus Product Owners (PO), bajo el método de Blends. El código de cada proyecto vive en su propio repositorio; la instancia registra su ubicación sin alojarlo en su historia. Teyst es el primero extraído, en `solera/teyst/`, según VCX-D043. Una propuesta en preparación puede custodiarse antes de confirmar su ingreso y queda fuera del portfolio activo hasta entonces.

El [producto Cellar](https://github.com/denispaiva/cellar/blob/main/README.md) aporta estructura y mecanismos reutilizables; esta instancia conserva la información concreta. Esa separación no duplica el código del producto.

Para preparar otra instancia en su propio workspace, partir de la [plantilla](https://github.com/denispaiva/cellar/blob/main/templates/cellar/README.md) después de acordar identidad, custodia y destino. Las instancias con requisitos diferentes de confidencialidad necesitan aislamiento efectivo, no solo carpetas distintas.

Si la instancia se alojará en otro repositorio, resolver antes de activarla el [disparador de distribución de principios](../docs/architecture/interoperability.md#distribución-de-principios-a-instancias-externas). No se necesita implementar ese mecanismo mientras no se prepare la primera instancia externa.
