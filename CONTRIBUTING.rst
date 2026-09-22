=======================================================
Directrices para Contribuir a la Documentación de NorTK
=======================================================

:Entidad: NorTK: Infraestructura Crítica y Soberanía Digital con Software Libre
:Sitio Web: https://nortk.com/
:Licencia: `GNU Free Documentation License, Versión 1.3 o posterior <https://www.gnu.org/licenses/fdl-1.3.html>`__

Este documento establece las normas operativas, estándares de calidad y flujos técnicos obligatorios para colaborar en la redacción, mantenimiento y evolución de la documentación técnica de NorTK.


Principios editoriales indispensables
=====================================
Toda contribución debe satisfacer de manera estricta los preceptos fundacionales del proyecto:

* **Realismo técnico y rigor empírico**: Todo procedimiento debe ser reproducible en un entorno limpio y contrastarse mediante comandos de verificación obligatorios con salidas de terminal reales.
* **Voz activa y modo imperativo directo**: Redacte los pasos procedimentales como órdenes directas: Configure la interfaz, Inicie el daemon, Instale el paquete. Queda erradicada la voz pasiva.
* **Erradicación del antropomorfismo**: No atribuya intenciones, emociones o pensamientos al software ni al hardware.
* **Español técnico sin anglicismos superfluos**: Emplee la traducción canónica consolidada en español cuando exista y preserve términos técnicos estándar de la industria únicamente cuando constituyan estándar de facto en sistemas operativos POSIX/Linux.
* **Títulos limpios**: Prohibido utilizar paréntesis en títulos o subtítulos. En español, los encabezados llevan mayúscula únicamente en la letra inicial y en los nombres propios. Queda prohibida la mayúscula sostenida.
* **Directiva cardinal de diagonales**: Jamás coloque espacios alrededor de barras diagonales. Escriba siempre ``palabra/palabra``, nunca ``palabra / palabra``.


Requerimientos del entorno en Fedora Linux
==========================================
Para garantizar un entorno determinista, instale los paquetes requeridos mediante DNF:

.. code-block:: bash

   # dnf install -y make python3-sphinx python3-sphinx_rtd_theme python3-sphinx-autobuild python3-rstcheck weasyprint


Flujo de desarrollo y verificación
==================================

#. Configure los hooks de Git en su copia local:

   .. code-block:: bash

      $ make hooks

#. Inicie el servidor de desarrollo interactivo con recarga en vivo:

   .. code-block:: bash

      $ make dev

#. Valide y corrija automáticamente omisiones comunes de formato en fuentes RST:

   .. code-block:: bash

      $ make fix

#. Ejecute la auditoría estática de sintaxis antes de preparar sus confirmaciones:

   .. code-block:: bash

      $ make lint

#. Genere el documento PDF para validar la maquetación imprimible:

   .. code-block:: bash

      $ make pdf


Protocolo de control de cambios y confirmaciones
================================================

* **Formato de confirmación**: Utilice el estándar Conventional Commits:

  .. code-block:: text

     tipo(alcance): descripción breve en imperativo

* **Tráilers obligatorios**: Toda confirmación debe incluir firma formal y registro de coautoría:

  .. code-block:: text

     Co-authored-by: Antigravity <antigravity@google.com>
     Signed-off-by: Nombre Apellido <correo@dominio.com>


Mandato de registro en Bitácora y mantenimiento documental
==========================================================

Toda modificación realizada en el repositorio debe cumplir obligatoriamente con las siguientes directivas de sincronización:

#. **Registro obligatorio en la Bitácora (CHANGELOG.rst)**:
   Ninguna adición, corrección, rediseño o ajuste estructural se considera concluido sin su correspondiente registro en el archivo ``CHANGELOG.rst`` bajo las secciones canónicas ``Agregado``, ``Modificado``, ``Deprecado``, ``Eliminado``, ``Corregido`` o ``Seguridad``.

#. **Evaluación y actualización de README.rst y CONTRIBUTING.rst**:
   Ante cualquier cambio que altere dependencias, herramientas, flujos de trabajo, objetivos de compilación o políticas de desarrollo, el colaborador debe evaluar de forma obligatoria el estado de ``README.rst`` y ``CONTRIBUTING.rst`` y aplicar las actualizaciones necesarias en el mismo conjunto de cambios.


Licencia de las contribuciones
==============================
Al colaborar en este proyecto, usted acepta de forma vinculante que toda su documentación, código, hojas de estilo y artefactos complementarios se publiquen bajo los términos de la Licencia de Documentación Libre de GNU (GNU Free Documentation License), Versión 1.3 o cualquier versión posterior aprobada por la Free Software Foundation.
