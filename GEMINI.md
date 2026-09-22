# Directivas de Ingeniería: Guía de Estilo de Documentación para NorTK

Este documento formaliza los mandatos técnicos, reglas editoriales, estándares ortográficos y convenciones operativas para el desarrollo y mantenimiento de la Guía de Estilo de Documentación para NorTK.

---

## 1. Fidelidad Lingüística y Realismo Técnico

La documentación de NorTK está dirigida a ingenieros de sistemas, arquitectos de infraestructura y operadores de misión crítica. Se rige por el principio de fidelidad técnica y precisión empírica:

* **Rechazo a la ingeniería lingüística ideológica**:
  * Prohibido el uso de desdoblamientos artificiales, morfemas inventados o circunloquios forzados que degraden la claridad y velocidad de lectura del operador.
  * El masculino gramatical en español opera como término genérico no marcado conforme a la norma de la Real Academia Española y el uso estándar en ingeniería.

* **Preservación incondicional de la terminología canónica técnica**:
  * Prohibida la censura o sustitución eufemística de términos estándar. Mantener de forma estricta términos consolidados como `master`/`slave`, `whitelist`/`blacklist`, `abort`, `kill` o `parent`/`child` donde las interfaces del kernel Linux, protocolos de red, buses de hardware o archivos de configuración así lo requieran.
  * La compatibilidad con RFCs, llamadas al sistema POSIX y código fuente upstream prima siempre sobre susceptibilidades o corrección política corporativa.

* **Español técnico sin anglicismos superfluos**:
  * Prohibido intercalar términos en inglés cuando exista un equivalente técnico consolidado en español.
  * Preservar exclusivamente la terminología canónica cuando sea estándar de facto en consolas y llamadas al sistema: *socket*, *cluster*, *kernel*, *bare-metal*, *daemon*, *pipeline*, *pool* y *firmware*.
  * Traducir de manera sobria y consistente los conceptos con equivalente consolidado: *despliegue*, *almacenamiento*, *alta disponibilidad*, *conmutación por error*, *sistema de archivos*, *bitácora*.

* **Reglas de capitalización y ortografía técnica**:
  * **Prohibición estricta de mayúsculas sostenidas**: Ningún título, encabezado, sección, etiqueta de menú o título de admonición debe escribirse en mayúsculas sostenidas.
  * **Prohibición del estilo de titular en inglés**: En español, los títulos y subtítulos llevan mayúscula únicamente en la letra inicial y en los nombres propios. Queda prohibido el estilo anglosajón (*Title Case*) en el cual cada palabra comienza con mayúscula.
  * **Acrónimos consolidados**: Se escriben en mayúsculas sin puntos intermedios exclusivamente cuando sean siglas técnicas estandarizadas como POSIX, LACP, KVM, CPU, RAM, DNS o SELinux.

* **Prohibición de paréntesis en títulos y erradicación en el contenido**:
  * Ningún título o encabezado debe contener paréntesis.
  * En el cuerpo del texto, erradicar los paréntesis innecesarios como muletas para sobre-explicar o traducir. Si una precisión técnica es indispensable, redáctela de forma directa en la oración; si no lo es, descártela.

* **Cero sobre-explicación**:
  * Mantener alta densidad de información técnica. Omitir explicaciones obvias, circunloquios y notas redundantes. Dirigirse al lector asumiendo competencia profesional en ingeniería.

---

## 2. Mandatos Editoriales y de Redacción

* **Voz activa y modo imperativo estricto**:
  * Todo procedimiento técnico se redacta en modo imperativo directo: Configure el adaptador, Cree el volumen, Inicie el daemon.
  * Prohibida la voz pasiva.

* **Erradicación absoluta del antropomorfismo**:
  * El software, los procesos y el silicio no tienen intenciones, sentimientos ni conciencia.
  * Prohibido: El kernel decide inteligentemente, El daemon piensa que, El sistema le pide al usuario.
  * Correcto: El kernel enruta el tráfico, El daemon evalúa la condición, El proceso retorna el código de error.

* **Didáctica basada en hechos**:
  * Prohibido documentar conceptos abstractos sin acompañarlos inmediatamente de un comando o configuración real, funcional y comprobable en un entorno limpio.
  * Si un tema no puede cubrirse con la profundidad requerida, se omite por completo antes de dejar explicaciones a medias.

* **Fundamentación técnica de juicios de valor**:
  * Prohibido calificar una tecnología o configuración como útil, mejor, insegura u óptima sin desglosar los criterios técnicos cuantitativos y cualitativos que respaldan la afirmación.

* **Identificación proactiva de trampas operativas**:
  * Visibilizar aristas filosas, límites de arquitectura, cambios silenciosos entre versiones y fallos comunes antes de que ocurran en producción.

---

## 3. El Contrato Procedimental de Cinco Bloques

Todo módulo de procedimiento debe cumplir obligatoriamente con la siguiente estructura de cinco partes:

1. **Propósito y contexto operativo**: Una o dos oraciones que definen la meta del procedimiento y el perfil del operador.
2. **Prerrequisitos**: Lista comprobable de paquetes, permisos de superusuario o cuenta específica, módulos del kernel y estado del sistema.
3. **Procedimiento**: Pasos numerados secuenciales con directivas `#.`, comandos en bloques `.. code-block:: bash` sin la opción `:caption:` y desglose inmediato de parámetros.
4. **Verificación**: Mandatorio en el 100% de los casos. Comando de auditoría explícito acompañado de la salida esperada de terminal para que el operador contraste el resultado.
5. **Recursos adicionales**: Enlaces a páginas man con su sección UNIX, RFCs o documentación upstream.

---

## 4. Estándar de Marcado reStructuredText

* **Jerarquía de títulos con coincidencia exacta**: Los sobrelineados y subrayados de encabezados deben coincidir carácter por carácter con la longitud del texto. Títulos limpios sin paréntesis y con mayúscula inicial únicamente.
* **Indentación a tres espacios**: Todo bloque anidado o cuerpo de directiva en RST se indenta exactamente a tres espacios, nunca cuatro ni tabuladores.
* **Listas y sublistas anidadas**: Obligatoria una línea en blanco antes del primer elemento de una lista y antes de cualquier sublista anidada.
* **Bloques de código**:
  * Usar exclusivamente `.. code-block:: <lenguaje>`.
  * Prohibido incluir la opción `:caption:` en bloques de código.
* **Directiva cardinal de diagonales**: Jamás use espacios alrededor de barras diagonales. Siempre `palabra/palabra`, nunca `palabra / palabra`.

---

## 5. Reglas para Capturas de Pantalla y Recursos Gráficos

* **Criterio estricto de necesidad**:
  * Se autorizan capturas de pantalla **únicamente** cuando se documentan interfaces de usuario en modo texto complejas (TUI) o interfaces gráficas (GUI) en las que la disposición espacial, controles interactivos o asistentes visuales no pueden representarse en texto puro: instaladores del sistema operativo (Anaconda), consolas web de administración (Cockpit), paneles de hipervisores o menús de firmware UEFI/BIOS.
  * Para topologías de red o diagramas de arquitectura de software, utilice diagramas declarativos generados por código (D2) o gráficos vectoriales SVG.

* **Prohibición absoluta en salidas textuales**:
  * **Estrictamente prohibido** utilizar capturas de pantalla para documentar comandos de terminal, salidas de consola, trazas de error, archivos de configuración o código fuente.
  * Razón técnica: Las imágenes de texto degradan la accesibilidad, impiden la copia determinista, no son indexables y complican el mantenimiento evolutivo. Todo contenido textual debe residir en bloques `.. code-block::`.

* **Encuadre, dimensiones y legibilidad**:
  * **Encuadre estricto**: Recortar la imagen exactamente a la ventana activa o control relevante. Prohibido capturar pantallas completas con escritorios vacíos o barras del sistema anfitrión.
  * **Resolución máxima**: No superar 1920x1080 píxeles. Dimensiones recomendadas entre 800x600 y 1280x720 píxeles.
  * **Tamaño tipográfico**: Incrementar la escala o tamaño de fuente en la interfaz antes de la captura, asegurando que el texto sea legible a un tamaño de al menos 14 a 16 píxeles sin ampliar la imagen.
  * **Tema visual**: Utilizar temas oscuros o de alto contraste conformes con la estética de NorTK.

* **Formato y optimización**:
  * Rasterizado: PNG con compresión sin pérdidas (`optipng`).
  * Vectorial: SVG para diagramas, esquemas y logotipos.
  * Almacenamiento: Directorio `source/_static/images/` con nombres en minúsculas y guiones (`kebab-case.png`).

* **Inclusión en reStructuredText y accesibilidad**:
  * Utilizar la directiva `.. figure::` o `.. image::`.
  * Parámetro `:alt:` obligatorio en el 100% de las imágenes con una descripción exhaustiva del estado visual para lectores de pantalla.
  * Usar `:align: center` y ancho porcentual adaptable (`:width: 100%` o `:width: 85%`). Prohibido definir alturas fijas en píxeles.

---

## 6. Flujo de Validación, Compilación y Calidad

* **Corrección automática de formato con crstlint**:
  * Para corregir automáticamente inconsistencias comunes de marcado, ejecute localmente:
    ```bash
    make fix
    ```
    (invoca `crstlint -fr .`).

* **Linter de marcado obligatorio con rstcheck**:
  * Todo archivo `.rst` debe pasar limpio con `make lint` utilizando `rstcheck -r .` con cero errores y cero advertencias antes de integrarse.

* **Hook pre-push de Git**:
  * Configurado mediante `make hooks` (`.githooks/pre-push`). Ejecuta automáticamente `rstcheck -r .` antes de cualquier envío remoto, abortando la operación si detecta advertencias o errores.

* **Compilación estricta y generación de entregables**:
  * Compilación estricta con `SPHINXOPTS ?= -W --keep-going`, convirtiendo cualquier advertencia en error fatal.
  * Generación de PDF formal con `make latexpdf` (o `make pdf`) utilizando el constructor LaTeX de Sphinx y `latexmk`, produciendo el manual íntegro.
  * Servidor interactivo con recarga en vivo mediante `make dev` en `http://127.0.0.1:8000/`.

* **Memoria del proyecto**:
  * Toda decisión arquitectónica, trampa descubierta o hito resuelto debe registrarse en el diario de proyecto mediante `ajourn log -m "<mensaje>" -t "<TAG>"`.

---

## 7. Mandato de Ciclo de Vida: Bitácora, README y Guía de Contribución

Todo cambio o entrega técnica en el repositorio debe cumplir obligatoriamente con las siguientes reglas de mantenimiento y sincronización:

* **Registro obligatorio en la Bitácora (`CHANGELOG.rst`)**:
  * Cada cambio, por mínimo que sea (funcional, editorial, de estilos o de infraestructura), debe llevar su correspondiente registro en `CHANGELOG.rst` respetando la estructura de *Keep a Changelog* y *Semantic Versioning*.
  * No se autoriza ninguna confirmación de Git sin su entrada correlativa en la Bitácora.

* **Evaluación y actualización obligatoria de `README.rst` y `CONTRIBUTING.rst`**:
  * Ante cualquier cambio que modifique dependencias del sistema, herramientas, comandos, objetivos de compilación, estructura de archivos o políticas editoriales, se debe evaluar y actualizar de manera coordinada `README.rst` y `CONTRIBUTING.rst`.
  * La documentación del repositorio y las instrucciones para colaboradores deben reflejar en todo momento el estado real y determinista de la base de código.
