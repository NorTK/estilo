==========================================
Guía de Estilo de Documentación para NorTK
==========================================

:Entidad: NorTK: Infraestructura Crítica y Soberanía Digital con Software Libre
:Sitio Web: https://nortk.com/
:Estado: En desarrollo
:Formato Canónico: reStructuredText
:Inspiraciones: `GNU Press Style Guide`_, `Documentación de RHEL 10`_ y `The IBM Style Guide`_

.. _GNU Press Style Guide: https://www.fsf.org/gnu-press/GNU-Press-styleguide.pdf
.. _Documentación de RHEL 10: file:///home/renich/Documents/documentation/RHEL/10/
.. _The IBM Style Guide: file:///home/renich/Downloads/the-ibm-style-guide-conventions-for-writers-and-editors_compress.pdf

Visión y filosofía
==================
En NorTK diseñamos, desplegamos y operamos infraestructura crítica empresarial sobre cimientos de Software Libre: sistemas operativos GNU/Linux Enterprise, clústeres de virtualización KVM, bases de datos PostgreSQL, almacenamiento distribuido, redes y Kubernetes bare-metal. En este nivel de misión crítica, la documentación no es un añadido decorativo ni una tarea secundaria: es un entregable de ingeniería indispensable para la reproducibilidad operativa, la soberanía tecnológica y la mitigación de fallos en producción.

Esta guía de estilo establece las directrices normativas para la redacción, arquitectura, tipografía y validación de toda la documentación técnica de NorTK. Nuestro objetivo es erradicar la ambigüedad, evitar explicaciones a medias y producir manuales, guías y especificaciones que garanticen una ejecución determinista.


Fuentes de inspiración y fundamentos
====================================
El marco documental de NorTK se construye a partir de la convergencia de tres grandes pilares de la ingeniería de sistemas, la documentación modular y la edición técnica:

Guía de estilo de GNU Press de la Free Software Foundation
----------------------------------------------------------
Inspirada en las pautas editoriales de Ron Hale-Evans, Robert J. Chassell y Richard M. Stallman en la `GNU Press Style Guide`_:

* **Didáctica de hechos**: Sustentar cada concepto en ejemplos prácticos, funcionales y directamente reproducibles, evitando redundancias estériles.

* **Control estricto de la carga cognitiva**: Progresión pedagógica gradual. No realizar saltos conceptuales abruptos ni asumir conocimientos previos no declarados. Si un tema no puede abordarse con la profundidad requerida para el usuario, se omite por completo en lugar de dejar explicaciones superficiales.

* **Fundamentación técnica de juicios de valor**: Evitar calificar una herramienta, configuración o patrón como "útil", "mejor" o "óptimo" sin explicar los criterios empíricos, métricas de rendimiento o requerimientos arquitectónicos que justifican esa postura.

* **Identificación proactiva de trampas operativas**: Anticipar y documentar de manera explícita las aristas filosas, efectos secundarios no evidentes y problemas reales que el operador enfrentará en el terreno.

* **Neutralidad y sobriedad técnica**: Eliminar el tono publicitario, la condescendencia y la editorialización superflua ajena a la tarea técnica.

* **Disciplina de accesibilidad**: Redactar con una coherencia estructural y semántica tan nítida que el contenido mantenga total claridad al ser procesado por herramientas de lectura por voz o lectores de pantalla, sin depender de artificios visuales.

Documentación de Red Hat Enterprise Linux 10
--------------------------------------------
Inspirada en la arquitectura de documentación modular de Red Hat en la `Documentación de RHEL 10`_:

* **Arquitectura modular rigurosa**: Estructuración del conocimiento en componentes atómicos y reutilizables:

   * **Módulos de Concepto**: Explican la arquitectura, principios de operación y contexto técnico: qué es y por qué se utiliza.

   * **Módulos de Procedimiento**: Secuencias de tareas orientadas a objetivos administrativos precisos: cómo ejecutar la labor, compuestas obligatoriamente por prerrequisitos, pasos numerados ejecutables y comandos reproducibles.

   * **Módulos de Referencia**: Tablas de parámetros, especificaciones de puertos, sintaxis CLI, variables de entorno y esquemas de configuración como detalle técnico de consulta.

   * **Ensamblajes**: Integración coherente de módulos de concepto, procedimiento y referencia para resolver un flujo operativo o caso de uso completo.

* **Verificación determinista**: Todo procedimiento técnico debe concluir con pasos formales de verificación que contrasten los comandos de auditoría contra las salidas esperadas en el sistema.

* **Orientación a tareas de misión crítica**: Terminología corporativa consistente, enfoque de menor privilegio con SELinux Enforcing, seguridad por diseño y directivas orientadas a la continuidad operativa en producción.

Guía de estilo de IBM Press
---------------------------
Inspirada en el manual canónico de redacción y edición técnica de IBM en `The IBM Style Guide`_:

* **Rigor editorial, gramatical y de estilo**: Aplicación consistente de voz activa, modo imperativo directo para procedimientos, eliminación estricta de la voz pasiva y erradicación del antropomorfismo: no atribuir capacidades humanas a procesos, daemons o componentes de software.

* **Fundamentos del autor modular**: Modelo conceptual y taxonómico precursor de la documentación basada en temas, garantizando independencia de contexto y cohesión en cada pieza informativa.

* **Convenciones tipográficas para interfaces técnicas**: Reglas tipográficas exactas para representar comandos CLI, parámetros, opciones, variables y marcadores de posición, rutas de archivos, nombres de demonios, teclas de acceso rápido y elementos visuales de interfaces gráficas o en modo texto.

* **Anatomía formal de mensajes de error**: Estándar para documentar mensajes del sistema con estructura de cuatro partes: identificador único, gravedad, explicación causal y acción correctiva requerida por el operador.

* **Precisión en unidades y formatos internacionales**: Uso estandarizado de prefijos binarios IEC como KiB, MiB, GiB frente a decimales del Sistema Internacional como KB, MB, GB, formatos de fecha y hora conforme a ISO 8601 y redacción pensada para claridad global y traducción sin ambigüedades.


La síntesis NorTK: la onda del proyecto
=======================================
La guía de estilo de NorTK amalgama estas tres fuentes para forjar un estándar unificado y adaptado a la infraestructura crítica en idioma español:

* **Español técnico de alta fidelidad**: Redacción nativa en español, sobria y precisa. Se evitan traducciones forzadas y anglicismos innecesarios, respetando los términos canónicos de la ingeniería de sistemas como ``socket``, ``cluster``, ``kernel``, ``firmware``, ``pool`` o ``pipeline``.

* **Reproducibilidad y verificación como ley**: Ninguna guía se da por concluida si un ingeniero no puede replicar el procedimiento en un entorno limpio obteniendo exactamente los resultados documentados.

* **reStructuredText como formato canónico**: Adopción de RST como lenguaje fuente estándar, compatible con Sphinx y docutils, permitiendo exportación automatizada a HTML, PDF y páginas man, con validación estática en pipelines de integración continua.

* **Documentación como código**: Todo documento se gestiona mediante control de versiones en Git, aplicando revisión por pares, análisis estático y políticas de cambios idénticas al software de producción.


Módulos de la guía de estilo
============================
La guía está estructurada en los siguientes módulos normativos dentro del directorio `source/`:

#. **01-principios-y-filosofia.rst**: Reglas sobre tono, voz activa, persona gramatical, audiencia objetivo y rigor empírico.
#. **02-arquitectura-modular.rst**: Especificación formal de módulos de concepto, procedimiento, referencia y ensamblajes.
#. **03-procedimientos-y-verificacion.rst**: Protocolo para documentar prerrequisitos, ejecución de comandos y validación determinista con salidas esperadas.
#. **04-convenciones-cli-y-tipografia.rst**: Reglas para comandos CLI, opciones, variables, sintaxis, rutas, captura de pantallas y combinaciones de teclas.
#. **05-mensajeria-y-gestion-de-errores.rst**: Pautas para documentar advertencias, consideraciones de seguridad, catálogo de errores y trampas operativas.
#. **06-estandar-marcado-rst.rst**: Jerarquía formal de encabezados, directivas Sphinx, bloques de código, tablas, listas y reglas de diagonales sin espacios.
#. **07-glosario-y-vocabulario-tecnico.rst**: Convenciones de traducción, unidades de medida y catálogo de términos técnicos en español.
#. **changelog.rst**: Enlace simbólico hacia ``CHANGELOG.rst`` en la raíz, integrando la bitácora de cambios directamente en el sitio generado.


Estructura del proyecto
=======================

.. code-block:: text

   estilo/
   ├── .githooks/
   │   └── pre-push                             # Hook de Git para rstcheck recursivo pre-push
   ├── CHANGELOG.rst                            # Historial canónico de versiones y bitácora
   ├── GEMINI.md                                # Directivas de ingeniería, realismo técnico y reglas
   ├── GNUmakefile                              # Automatización para compilación, linting y dev server
   ├── README.rst                               # Índice principal y documentación del repositorio
   └── source/                                  # Fuentes de Sphinx en reStructuredText
       ├── conf.py                              # Configuración de Sphinx en español con sphinx_rtd_theme
       ├── index.rst                            # Página principal y árbol de contenidos toctree
       ├── changelog.rst -> ../CHANGELOG.rst    # Enlace simbólico para incluir la bitácora en la guía
       ├── 01-principios-y-filosofia.rst        # Tono, voz activa, pedagogía y accesibilidad
       ├── 02-arquitectura-modular.rst          # Taxonomía: concepto, procedimiento, referencia y ensamblaje
       ├── 03-procedimientos-y-verificacion.rst # Contrato de 5 bloques, verificación y prompts de superusuario
       ├── 04-convenciones-cli-y-tipografia.rst # Notación CLI y POSIX, teclado, interfaces, unidades IEC y SI
       ├── 05-mensajeria-y-gestion-de-errores.rst # Anatomía de 4 partes, admoniciones y trampas operativas
       ├── 06-estandar-marcado-rst.rst          # Jerarquía de títulos, 3 espacios, diagonales sin espacios
       ├── 07-glosario-y-vocabulario-tecnico.rst # Criterio lingüístico y catálogo de traducciones al español
       └── _static/
           ├── logo.svg                         # Logotipo vectorial oficial de NorTK
           └── css/nortk.css                    # Hoja de estilos con la identidad corporativa


Requerimientos del sistema en Fedora Linux
==========================================
Para compilar, validar y desarrollar la documentación localmente en Fedora Linux en sus versiones 41, 42, 43 y 44, se requieren los siguientes paquetes nativos de los repositorios oficiales:

* **make**: Motor de automatización para la ejecución del `GNUmakefile`.
* **python3-sphinx**: Generador de documentación técnica Sphinx en versión 8 o superior.
* **python3-sphinx_rtd_theme**: Tema base oficial Read the Docs.
* **python3-sphinx-autobuild**: Servidor de desarrollo con recarga en vivo mediante WebSockets.
* **python3-rstcheck**: Linter y analizador estático para fuentes reStructuredText.
* **crstlint**: Herramienta de formateo y corrección automática de fuentes reStructuredText.
* **weasyprint**: Motor de renderizado HTML/CSS a PDF para la generación de entregables imprimibles.


Instalación de dependencias
===========================
Como superusuario `root` o antecediendo `sudo`, instale las dependencias ejecutando en su terminal:

.. code-block:: bash

   # dnf install -y make python3-sphinx python3-sphinx_rtd_theme python3-sphinx-autobuild python3-rstcheck weasyprint


Flujo de desarrollo local
=========================
El proyecto cuenta con un entorno de desarrollo interactivo que compila la documentación utilizando el constructor ``dirhtml`` para generar rutas limpias en la web, recargando automáticamente la página en el navegador al guardar cualquier cambio en los archivos fuente dentro de ``source/``:

#. Configure los hooks de Git en el repositorio local:

   .. code-block:: bash

      $ make hooks

#. Inicie el servidor de desarrollo:

   .. code-block:: bash

      $ make dev

#. Abra su navegador web en la dirección local indicada por el servidor:

   .. code-block:: text

      http://127.0.0.1:8000/

#. Edite o agregue archivos en el directorio `source/`. El servidor detectará los cambios en tiempo real, recompilará únicamente los archivos afectados y refrescará la vista en el navegador sin intervención manual.

#. Si requiere formatear o reparar automáticamente inconsistencias de listas o espaciado en archivos RST:

   .. code-block:: bash

      $ make fix

#. Si requiere utilizar otro puerto de red o interfaz de escucha, proporcione las variables `PORT` o `HOST`:

   .. code-block:: bash

      $ make dev PORT=8080 HOST=0.0.0.0


Objetivos de compilación
========================
El archivo `GNUmakefile` contiene los siguientes objetivos de automatización:

* **make dev**: Inicia el servidor con recarga en vivo ejecutando ``sphinx-autobuild -b dirhtml`` en el puerto 8000.
* **make html**: Compila la documentación completa a HTML estándar en `build/html/`.
* **make dirhtml**: Compila la documentación a formato de directorios con `index.html` en `build/dirhtml/`.
* **make singlehtml**: Compila la totalidad de la guía en una sola página HTML en `build/singlehtml/`.
* **make pdf**: Compila el documento monolítico e invoca `weasyprint` para producir el artefacto PDF formal en `build/nortk-guia-estilo-v0.1.0.pdf`.
* **make lint**: Ejecuta ``rstcheck -r .`` de forma recursiva sobre la totalidad de los archivos RST del proyecto.
* **make fix**: Ejecuta ``crstlint -fr .`` para corregir de forma automática problemas comunes de formato.
* **make hooks**: Configura el hook ``.githooks/pre-push`` en Git para impedir envíos remotos con errores.
* **make linkcheck**: Verifica la vigencia de todos los enlaces externos.
* **make clean**: Elimina el directorio de compilación `build/`.


Repositorios y publicación
==========================

* **Repositorio principal (GitHub)**: https://github.com/NorTK/estilo
* **Publicación en línea (GitHub Pages)**: https://nortk.github.io/estilo/
* **Réplica en Codeberg**: https://codeberg.org/NorTK/estilo
* **Réplica en GitLab**: https://gitlab.com/renich/estilo


Licencia
========
Este proyecto y toda la documentación técnica de NorTK se publican bajo los términos de la `GNU Free Documentation License, Versión 1.3 o posterior <https://www.gnu.org/licenses/fdl-1.3.html>`__. Consulte el archivo ``COPYING`` o ``LICENSE`` en la raíz del repositorio.


Referencias y enlaces
=====================

* `GNU Press Style Guide <https://www.fsf.org/gnu-press/GNU-Press-styleguide.pdf>`__ — Ron Hale-Evans, Robert J. Chassell, Richard M. Stallman, Free Software Foundation.
* `Red Hat Enterprise Linux 10 Documentation <file:///home/renich/Documents/documentation/RHEL/10/>`__ — Red Hat Enterprise Linux 10 Reference Library, Red Hat, Inc.
* `The IBM Style Guide: Conventions for Writers and Editors <file:///home/renich/Downloads/the-ibm-style-guide-conventions-for-writers-and-editors_compress.pdf>`__ — Francis Bush et al., IBM Press.

