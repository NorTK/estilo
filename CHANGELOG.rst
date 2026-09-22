========
Bitácora
========

Registro de cambios y evolución de la Guía de Estilo de Documentación para NorTK.

El formato se basa en `Keep a Changelog <https://keepachangelog.com/es-ES/1.1.0/>`_, y este proyecto se adhiere a `Semantic Versioning <https://semver.org/lang/es/>`_.


[Sin publicar]
==============

.. rubric:: Agregado

* Documento canónico ``CONTRIBUTING.rst`` en la raíz del repositorio y enlace simbólico ``source/contributing.rst`` integrado en el árbol de navegación de Sphinx.
* Regla formal de ciclo de vida en ``GEMINI.md`` que establece la obligatoriedad de registrar cada cambio en la Bitácora (``CHANGELOG.rst``) y evaluar de forma coordinada la actualización de ``README.rst`` y ``CONTRIBUTING.rst``.

.. rubric:: Modificado

* Optimización estructural de ``GEMINI.md`` para maximizar la densidad informativa, eliminar redundancias y consolidar directivas de calidad y estilo.
* Corrección y ampliación del espaciado editorial en los títulos de grupo del menú lateral en ``source/_static/css/nortk.css`` para erradicar el amontonamiento sobre los enlaces subordinados.
* Corrección del contraste tipográfico en encabezados de tabla (``thead th p``), asegurando texto blanco nítido sobre fondo oscuro.
* Actualización de ``README.rst`` incorporando la sección de contribuciones y reflejando los nuevos archivos del proyecto.


[0.1.0] - 2026-09-21
====================

.. rubric:: Agregado

* Inicialización del proyecto de documentación en Sphinx con soporte completo en idioma español.
* Tres fuentes maestras integradas como pilares: `GNU Press Style Guide`_, `Documentación de RHEL 10`_ y `The IBM Style Guide`_.
* Módulo 01: Principios editoriales, voz activa, didáctica de hechos, erradicación del antropomorfismo y accesibilidad estructural.
* Módulo 02: Arquitectura modular basada en temas: conceptos, procedimientos, referencias y ensamblajes.
* Módulo 03: Contrato procedimental de 5 bloques, verificación determinista con salidas de terminal y gestión de prompts para superusuario y usuario sin privilegios.
* Módulo 04: Convenciones de interfaz de comandos conforme a POSIX/GNU, teclado, interfaces visuales, unidades binarias IEC frente a decimales del Sistema Internacional, fechas ISO 8601 y reglas para capturas de pantalla.
* Módulo 05: Mensajería de sistema con anatomía de cuatro componentes, jerarquía de admoniciones y catálogo preventivo de trampas operativas.
* Módulo 06: Estándar de marcado reStructuredText, jerarquía formal de títulos, indentación a 3 espacios y directiva cardinal de diagonales sin espacios como ``palabra/palabra``.
* Módulo 07: Glosario técnico y catálogo normativo de traducciones al español.
* Logotipo oficial SVG de NorTK obtenido de ``nortk.com`` e integrado en la barra lateral.
* Servidor interactivo de desarrollo local mediante ``make dev`` con ``sphinx-autobuild`` y constructor ``dirhtml``.
* Archivo ``GEMINI.md`` con directivas de ingeniería, realismo técnico, reglas de capitalización ortográfica, pautas de capturas de pantalla y prohibición de paréntesis en títulos.
* Automatización en ``GNUmakefile`` con validación estática estricta mediante ``rstcheck`` recursivo en ``make lint`` y formateo asistido con ``crstlint`` en ``make fix``.
* Hook de Git para pre-push en ``.githooks/pre-push`` configurado con ``make hooks`` para validar el árbol documental antes de cada envío remoto.

.. rubric:: Modificado

* Rediseño editorial formal del tema en ``source/_static/css/nortk.css``: escala tipográfica incrementada a 16.5px para mayor legibilidad y descanso visual, columna de lectura acotada a 90 caracteres para párrafos y listas sin sacrificar el ancho fluido de tablas y bloques de código.
* Reestructuración del espaciado del menú lateral, otorgando separación holgada a los títulos de grupo y eliminando transformaciones a mayúsculas sostenidas mediante ``text-transform: none``.
* Estandarización de títulos en español con mayúscula inicial únicamente, erradicando mayúsculas sostenidas y el estilo *Title Case* anglosajón en todos los módulos de la guía.
* Unificación de la denominación canónica del manual como *Guía de Estilo de Documentación para NorTK* y adopción formal del término *Bitácora* para el control de cambios.
* Incorporación del protocolo y especificaciones técnicas para capturas de pantalla y recursos gráficos en interfaces GUI y TUI.
* Corrección y optimización del flujo de linter automático con ``crstlint -fr .`` y hook pre-push con ``rstcheck -r .``.

.. _GNU Press Style Guide: https://www.fsf.org/gnu-press/GNU-Press-styleguide.pdf
.. _Documentación de RHEL 10: file:///home/renich/Documents/documentation/RHEL/10/
.. _The IBM Style Guide: file:///home/renich/Downloads/the-ibm-style-guide-conventions-for-writers-and-editors_compress.pdf
