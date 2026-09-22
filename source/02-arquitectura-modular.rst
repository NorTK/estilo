==================================
Arquitectura modular de documentos
==================================

NorTK adopta una arquitectura modular de documentación basada en temas, heredera de los estándares de IBM y la estructura de publicación de Red Hat Enterprise Linux. Este paradigma sustituye los manuales monolíticos tradicionales por componentes atómicos, autocontenidos y reutilizables.


Fundamentos del modelo basado en temas
======================================
Un tema es una unidad de información autónoma que responde a un objetivo específico del lector y puede leerse, mantenerse y reutilizarse con total independencia de los documentos circundantes.

* **Monotemático**: Cada archivo cubre un único tema, proceso o subsistema.

* **Autocontenido**: No asume que el lector ha leído secuencialmente los capítulos anteriores. Si un tema depende de otro, se declara como prerrequisito o enlace de referencia cruzada.

* **Reutilizable**: Un módulo de procedimiento, como la creación de un volumen LVM, puede ensamblarse tanto en una guía de almacenamiento como en un manual de despliegue de bases de datos.


Taxonomía de unidades documentales
==================================
Toda la documentación técnica de NorTK se clasifica rigurosamente en una de las siguientes cuatro categorías:


Módulos de concepto
-------------------
Los módulos de concepto proporcionan el contexto teórico, arquitectónico y operativo indispensable antes de ejecutar cualquier acción.

* **Preguntas a las que responde**: ¿Qué es este componente? ¿Por qué se utiliza? ¿Cómo interactúa con el resto del sistema? ¿Cuáles son sus restricciones arquitectónicas?

* **Contenido canónico**: Diagramas de bloques, explicaciones de flujo de datos, comparativas de diseño y restricciones de soporte.

* **Prohibición**: No debe contener pasos procedimentales ni instrucciones de comandos paso a paso.


Módulos de procedimiento
------------------------
Los módulos de procedimiento guían al operador paso a paso hacia un objetivo operativo concreto mediante instrucciones secuenciales y reproducibles.

* **Preguntas a las que responde**: ¿Cómo se realiza esta tarea específica? ¿Cuáles son los prerrequisitos? ¿Cómo se comprueba que el resultado es correcto?

* **Contenido canónico**: Estructura de cinco bloques obligatorios: Contexto, Prerrequisitos, Procedimiento con pasos numerados, Verificación determinista y Recursos adicionales.

* **Prohibición**: No debe incluir explicaciones teóricas extensas ni disquisiciones sobre arquitectura. Si se requiere teoría, se enlaza al módulo de concepto correspondiente.


Módulos de referencia
---------------------
Los módulos de referencia proporcionan acceso veloz a especificaciones técnicas, catálogos de parámetros y esquemas para consulta durante la operación o resolución de incidencias.

* **Preguntas a las que responde**: ¿Qué opciones admite esta directiva? ¿Qué puerto TCP utiliza este daemon? ¿Qué valores devuelve este comando?

* **Contenido canónico**: Tablas de opciones de configuración, especificaciones de sintaxis de comandos, matrices de puertos y cortafuegos, variables de entorno y códigos de retorno.

* **Prohibición**: No debe contener narrativas procedimentales ni tutoriales. Se redacta en enunciados fácticos directos y tablas de consulta rápida.


Ensamblajes
-----------
Un ensamblaje es un documento integrador que combina módulos de concepto, procedimiento y referencia para resolver un flujo de trabajo complejo de inicio a fin.

* **Propósito**: Resolver casos de uso completos de infraestructura, como el despliegue de un clúster KVM en alta disponibilidad o la instalación y endurecimiento de PostgreSQL 16.

* **Estructura típica**:

   #. Introducción y arquitectura global conceptual.
   #. Procedimiento de preparación del host.
   #. Procedimiento de instalación y configuración del servicio.
   #. Procedimiento de verificación del clúster.
   #. Tabla de referencia de puertos y directivas de configuración.


Independencia de contexto y reutilización
=========================================
Para garantizar que los módulos funcionen tanto de manera aislada como integrados en ensamblajes:

* **Eliminación de conectores contextuales**: No use frases como "Como vimos en el capítulo anterior", "Más adelante explicaremos" o "En la siguiente página".

* **Referencias explícitas**: Si se requiere conocimiento previo, vincule directamente al módulo correspondiente utilizando roles de Sphinx como ``:doc:`` o ``:ref:``.


Convenciones de nomenclatura y títulos
======================================
Siguiendo las directrices consolidadas de la industria:

* **Títulos de concepto**: Sintagmas nominales o sustantivos en singular o plural que describen el objeto técnico, como "Arquitectura de almacenamiento distribuido Ceph" o "Modos de control de acceso en SELinux".

* **Títulos de procedimiento**: Formas verbales activas o gerundios en español que denotan una acción, como "Configuración de enlaces de red agregados" o "Aprovisionamiento de volúmenes cifrados con LUKS2".

* **Títulos de referencia**: Sustantivos en plural que indican una lista o catálogo, como "Parámetros del kernel para virtualización" o "Directivas de configuración de PostgreSQL".

* **Títulos de ensamblaje**: Enunciados orientados a la solución completa, como "Despliegue de infraestructura de virtualización KVM".
