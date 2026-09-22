====================================
Estándar de marcado reStructuredText
====================================

Toda la documentación técnica de NorTK se escribe exclusivamente en reStructuredText compatible con docutils y Sphinx. Este módulo fija las reglas tipográficas y sintácticas para garantizar una salida HTML, PDF y man impecable y libre de errores de compilación.


Jerarquía canónica de encabezados
=================================
La estructura de títulos debe seguir estrictamente la jerarquía definida sin saltarse niveles. Tanto los sobrelineados como los subrayados deben coincidir con la longitud exacta de caracteres del título:

.. code-block:: text

   =======================
   Título de parte o libro
   =======================

   Título de capítulo
   ==================

   Sección H1
   ==========

   Sección H2
   ----------

   Sección H3
   ^^^^^^^^^^

   Sección H4
   """"""""""

* Título de parte o libro: sobrelineado y subrayado con ``=``
* Título de capítulo: sobrelineado y subrayado con ``=``
* Sección H1: subrayado con ``=``
* Sección H2: subrayado con ``-``
* Sección H3: subrayado con ``^``
* Sección H4: subrayado con ``"``

Todos los títulos deben cumplir con la norma ortográfica de capitalización en español: mayúscula inicial exclusivamente, sin mayúsculas sostenidas ni mayúsculas en cada palabra.


Indentación a tres espacios
===========================
A diferencia de proyectos que emplean cuatro espacios, en NorTK se aplica la directiva de ingeniería de **tres espacios de indentación** para el cuerpo de directivas RST y bloques anidados:

.. code-block:: rst

   .. note::

      Este es el cuerpo de la nota con sangría exacta de tres espacios.
      Todas las líneas subsecuentes deben alinearse en la columna 4.


Reglas para listas y sublistas anidadas
=======================================
Para evitar que el motor de Sphinx colapse las listas en un único párrafo en la salida HTML:

* **Línea en blanco obligatoria antes de cualquier lista**: Siempre debe existir una línea vacía entre el párrafo precedente y el primer elemento de la lista.

* **Línea en blanco obligatoria antes de sublistas anidadas**: Toda sublista, con viñetas o numerada, debe estar precedida por una línea en blanco inmediatamente después del texto del elemento padre.

   .. code-block:: rst

      * Elemento padre principal

         * Sub-elemento anidado precedido de línea en blanco
         * Segundo sub-elemento anidado

* **Espaciado de viñetas**: Un solo espacio tras el asterisco, como ``* Item``, nunca ``*   Item``.

* **Autonumeración estricta**: Emplee ``#.`` para listas numeradas en lugar de números manuales como ``1.`` o ``2.``, permitiendo reordenar pasos sin romper la secuencia.


Bloques de código y lenguajes soportados
========================================

* **Uso exclusivo de directivas code-block**: No use la sintaxis de doble dos puntos ``::``. Utilice siempre la directiva explícita ``.. code-block:: <lenguaje>``.

* **Prohibición absoluta de :caption:**: **JAMÁS incluya la opción :caption: en un bloque de código.** Sphinx genera artefactos visuales defectuosos y advertencias estructurales. Si se requiere un título explicativo, colóquelo como texto regular o título de sección previo al bloque.

* **Lenguajes normalizados**: ``bash``, ``python``, ``crystal``, ``yaml``, ``json``, ``sql``, ``ini``, ``text``.


Directiva cardinal para diagonales
==================================
**JAMÁS use espacios alrededor de barras diagonales.** Debe formatearse siempre como ``palabra/palabra``: ``offline/air-gapped``, ``activo/pasivo``, ``lectura/escritura``, ``TCP/UDP``, ``seguridad/CVE``. Queda estrictamente prohibido el formato ``palabra / palabra``.


Validación automática con rstcheck
==================================
Ningún cambio documental se incorpora al repositorio sin superar la verificación estática:

.. code-block:: bash

   $ make lint

Este comando ejecuta ``rstcheck`` sobre todos los archivos ``.rst`` del proyecto, validando la sintaxis docutils, niveles de títulos y directivas de código.
