=====================================
Convenciones de interfaz y tipografía
=====================================

La interacción con sistemas de infraestructura crítica exige precisión tipográfica sin ambigüedades. Este módulo establece las convenciones formales para documentar herramientas de línea de comandos, interfaces en modo texto o gráficas, acciones de teclado y unidades de medición, fundamentadas en las normas de estilo de IBM.


Notación formal de sintaxis de comandos
=======================================
Para documentar la sintaxis de un comando o herramienta en módulos de referencia, utilice la notación estándar POSIX/GNU:

.. code-block:: text

   comando [opciones] <argumento-obligatorio> [argumento-opcional]...

* **Literales de comando**: Todo comando, subcomando o palabra clave invariable se escribe en texto monoespaciado exacto: ``nmcli``, ``podman run``, ``zpool create``.

* **Argumentos obligatorios**: Se delimitan mediante corchetes angulares como ``<nombre_volumen>`` o ``<interfaz>``. Indican valores que el operador debe sustituir por identificadores reales de su entorno.

* **Argumentos opcionales**: Se encierran entre corchetes rectos como ``[--verbose]`` o ``[-f <ruta>]``.

* **Valores mutuamente excluyentes**: Se separan mediante una barra vertical o tubería como ``enable|disable`` o ``start|stop|restart``. Si el grupo es obligatorio, se agrupa entre llaves como ``{on|off}``; si es opcional, entre corchetes como ``[on|off]``.

* **Argumentos repetibles**: Se indican con puntos suspensivos inmediatamente después del elemento como ``<archivo>...``.


Elementos tipográficos de la línea de comandos
==============================================
Al mencionar elementos de interfaz en el cuerpo del texto:

* **Nombres de binarios y comandos**: En monoespaciado: ``systemctl``, ``parted``, ``dnf``.
* **Banderas y parámetros**: En monoespaciado: ``--all``, ``-y``, ``--now``.
* **Rutas y nombres de archivo**: En monoespaciado: ``/etc/fstab``, ``/var/log/messages``.
* **Variables de entorno y directivas**: En monoespaciado y mayúsculas cuando corresponda: ``PATH``, ``SELINUX=enforcing``.
* **Nombres de demonios y servicios**: En monoespaciado: ``sshd.service``, ``chronyd``.


Interfaces en modo texto y gráficas
===================================
Para herramientas con pantallas interactivas, tales como nmtui, Anaconda, consolas web Cockpit o interfaces web de virtualización:

* **Elementos visuales en negrita**: Etiquetas de campos, botones, casillas de selección, menús desplegables y títulos de ventana se formatean en **negrita**.

   * *Ejemplo*: Haga clic en el botón **Aplicar**, seleccione la casilla **Habilitar en el arranque** y pulse **Guardar**.

* **Rutas jerárquicas de menús**: Utilice el separador mayor que ``>`` con espacios para representar secuencias de navegación.

   * *Ejemplo*: Diríjase a **Redes** > **Configuración de Interfaces** > **Editar Enlace**.


Nomenclatura y acciones de teclado
==================================
Las instrucciones que involucran el teclado deben emplear verbos precisos y nombres de teclas estandarizados:

* **Verbos de interacción**:

   * *Presione*: Para teclas individuales o combinaciones simultáneas: *Presione Enter*, *Presione Ctrl+C*.
   * *Escriba*: Para cadenas de caracteres o secuencias de texto literales: *Escriba :wq y presione Enter*.
   * *Seleccione*: Para elegir entre opciones en menús interactivos.

* **Combinaciones de teclas**: Se expresan uniendo las teclas con el signo más ``+`` sin espacios.

   * *Correcto*: ``Ctrl+Alt+Del``, ``Shift+Tab``, ``Alt+F4``.
   * *Incorrecto*: ``Ctrl-C``, ``Control + C``, ``Ctrl más C``.


Unidades de medida y prefijos binarios frente a decimales
=========================================================
En sistemas de almacenamiento, virtualización y redes existe una distinción crítica entre prefijos binarios IEC y decimales del Sistema Internacional que no debe confundirse:

* **Prefijos binarios IEC en base 2**: Obligatorios para dimensionar memoria RAM, cachés, tamaños de disco, particiones, volúmenes lógicos y asignaciones de memoria virtual.

   * *Unidades*: Kibibyte o KiB, Mebibyte o MiB, Gibibyte o GiB, Tebibyte o TiB.
   * *Ejemplo*: "Asigne un volumen LVM de 50 GiB a la máquina virtual."

* **Prefijos decimales del Sistema Internacional en base 10**: Se reservan para frecuencias de procesador y tasas de transferencia en redes de telecomunicaciones.

   * *Unidades*: Kilobit por segundo o Kbps, Megabit por segundo o Mbps, Gigabit por segundo o Gbps, Kilohertz o kHz, Gigahertz o GHz.
   * *Ejemplo*: "El enlace agregado proporciona un ancho de banda teórico de 20 Gbps."


Formatos de fecha, hora y redes
===============================

* **Fechas y horas**: Aplique el estándar internacional ISO 8601:

   * Fechas: ``YYYY-MM-DD``, por ejemplo ``2026-09-21``.
   * Horas: ``HH:MM:SS`` en formato de 24 horas, indicando zona horaria si aplica, como ``19:30:00Z`` o ``19:30:00-06:00``.

* **Direcciones de red y máscaras**: Utilice la notación CIDR estandarizada en lugar de máscaras de subred en formato decimal punteado, a menos que el software requiera explícitamente la sintaxis clásica.

   * *Recomendado*: ``192.168.100.0/24``, ``10.0.0.0/8``.
   * *Solo cuando sea forzoso por la interfaz*: ``192.168.100.0 netmask 255.255.255.0``.


Reglas para capturas de pantalla y recursos gráficos
====================================================
La documentación de infraestructura crítica debe priorizar siempre el texto copiable y auditable. Las imágenes y capturas de pantalla están sujetas a un criterio estricto de necesidad:

* **Criterio de necesidad exclusiva**:
   Se autorizan capturas de pantalla únicamente cuando se documentan interfaces gráficas o en modo texto interactivas donde la disposición espacial o los controles visuales no pueden reproducirse en texto plano. Casos válidos: instaladores del sistema operativo, consolas web de administración de hipervisores o menús de firmware UEFI.

* **Prohibición absoluta en texto y consola**:
   Queda estrictamente prohibido utilizar capturas de pantalla para mostrar salidas de terminal, comandos CLI, código fuente, trazas de depuración o archivos de configuración. Todo texto debe presentarse mediante bloques de código ``.. code-block::`` para permitir copia determinista, indexación en motores de búsqueda y accesibilidad mediante lectores de pantalla.

* **Encuadre estricto y resolución**:

   * Recorte la imagen exactamente a la ventana o área interactiva de interés. Prohibido capturar pantallas completas con fondos de escritorio, escritorios vacíos o barras de tareas del sistema operativo anfitrión.
   * La resolución máxima admitida es 1920x1080 píxeles. La resolución recomendada se sitúa entre 800x600 y 1280x720 píxeles.
   * Ajuste el tamaño de fuente en la interfaz antes de la captura para asegurar que el texto sea legible a un tamaño de al menos 14 a 16 píxeles.

* **Formatos y optimización**:

   * Utilice formato PNG con compresión sin pérdidas para capturas de pantalla, optimizado previamente mediante herramientas como ``optipng``.
   * Utilice formato SVG para diagramas vectoriales, esquemas de arquitectura y logotipos.
   * Almacene los archivos en el directorio ``source/_static/images/`` con nombres descriptivos en minúsculas separados por guiones.

* **Inclusión en reStructuredText y accesibilidad**:

   * Inserte imágenes mediante la directiva ``.. figure::`` o ``.. image::``.
   * El parámetro ``:alt:`` es obligatorio en la totalidad de las imágenes, proporcionando una descripción funcional exhaustiva para lectores de pantalla.
   * Aplique ``:align: center`` y dimensionamiento adaptable mediante ``:width: 100%`` o un porcentaje acotado. Prohibido definir alturas fijas en píxeles.
