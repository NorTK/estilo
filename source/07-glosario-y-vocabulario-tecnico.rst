===============================
Glosario y terminología técnica
===============================

Este módulo establece el criterio lingüístico de NorTK para la redacción técnica en español, definiendo qué términos deben traducirse al español estándar de ingeniería y cuáles deben preservarse en su forma canónica internacional para evitar confusiones en la consola de comandos.


Criterios de traducción al español técnico
==========================================
En NorTK se aplica una política de **español técnico de alta fidelidad**:

* **Evitar calcos anglicados**: No utilice construcciones sintácticas forzadas copiadas del inglés. Por ejemplo, evite "aplicar cambios a" cuando en español corresponde "aplicar los cambios en", o el gerundio de posterioridad como "creando el archivo y luego iniciando el servicio".

* **Evitar purismos extremos**: No intente traducir términos consolidados de la computación que generen ambigüedad o desconcierto en el operador de terminal. Traducir *socket* por "enchufe" o *buffer* por "memoria intermedia de amortiguamiento" degrada la claridad técnica.


Términos canónicos que no se traducen
=====================================
Los siguientes términos se mantienen en su denominación técnica universal en minúsculas o su grafía original:

* ``bare-metal``: Servidores físicos sin capa de virtualización.
* ``cluster/clustering``: Conjunto de nodos interconectados que actúan como una sola entidad.
* ``daemon``: Proceso que se ejecuta en segundo plano sin terminal controladora.
* ``firmware``: Software grabado en hardware no volátil.
* ``kernel``: Núcleo del sistema operativo.
* ``pipeline``: Tubería de ejecución secuencial en CI/CD o procesamiento de datos.
* ``pool``: Agrupación lógica de recursos de almacenamiento, memoria o conexiones.
* ``proxy/reverse proxy``: Agente intermediario de red.
* ``socket``: Extremo de comunicación bidireccional IPC o de red.
* ``storage``: Subsistema de almacenamiento de datos cuando forma parte de nombres propios de arquitectura.


Catálogo de traducciones obligatorias
=====================================
Para los siguientes conceptos, es obligatorio emplear la traducción técnica en español:

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Término en Inglés
     - Traducción Normativa en NorTK

   * - Backup
     - Respaldo/copia de seguridad

   * - Changelog
     - Bitácora

   * - Deployment
     - Despliegue

   * - Failover
     - Conmutación por error

   * - Filesystem
     - Sistema de archivos

   * - High Availability
     - Alta disponibilidad

   * - Hostname
     - Nombre de host

   * - Log/Logging
     - Registro/registro de eventos

   * - Prerequisite
     - Prerrequisito

   * - Storage
     - Almacenamiento

   * - Troubleshooting
     - Resolución de problemas

   * - Virtual Machine
     - Máquina virtual


Pronunciación y verbalización de código
=======================================
Inspirado en los lineamientos de la guía de estilo de GNU Press:

* Al introducir sintaxis de código no evidente o símbolos de configuración, indique explícitamente cómo debe verbalizarse en conversaciones entre ingenieros.

* *Ejemplo*: En expresiones de asignación o punteros, aclare cómo leer los operadores para fomentar una comunicación oral precisa dentro de los equipos de infraestructura y soporte.
