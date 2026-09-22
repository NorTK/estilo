===========================================
Mensajería del sistema y gestión de errores
===========================================

Cuando un sistema de producción falla, la documentación debe ofrecer diagnósticos inmediatos y caminos de remediación inequívocos. Este módulo establece el estándar formal para catalogar mensajes del sistema como errores, advertencias e información, adoptado de las directrices de estilo de IBM, así como las normas para la anticipación de trampas operativas provenientes de la guía de estilo de GNU Press.


La anatomía canónica de cuatro partes
=====================================
Todo mensaje de error o evento crítico documentado en manuales de resolución de problemas debe descomponerse en cuatro elementos obligatorios:

.. code-block:: text

   NTK-STR-0402E: No se pudo montar el sistema de archivos /dev/mapper/data-vol en /data.
   Explicación: La etiqueta del sistema de archivos o el UUID no coinciden con la entrada
   configurada en /etc/fstab, o el volumen contiene inconsistencias de metadatos XFS tras
   un reinicio abrupto.
   Respuesta del operador: Ejecute 'xfs_repair -n /dev/mapper/data-vol' para inspeccionar
   el volumen en modo de solo lectura. Si el volumen está limpio, verifique el UUID actual
   con 'blkid /dev/mapper/data-vol' y actualice la línea correspondiente en /etc/fstab.


Componente 1: identificador de mensaje
======================================
Un código alfanumérico unívoco que permite al operador buscar el error en catálogos y motores de búsqueda corporativos:

* Formato estándar: ``<PREFIJO_SUBSISTEMA>-<SUBSISTEMA>-<NUMERO><TIPO>``
* Sufijo de severidad: ``E`` para error, ``W`` para advertencia e ``I`` para información.


Componente 2: texto del mensaje
===============================
Descripción concisa y objetiva de la anomalía observada:

* **Enfoque en el hecho**: No use frases genéricas como "Ocurrió un error inesperado".
* **No culpar al operador**: Describa el estado del sistema, no una supuesta negligencia del operador. Por ejemplo, documente "No se proporcionó un certificado válido" en lugar de "Usted ingresó un certificado inválido".


Componente 3: explicación técnica
=================================
Detalla las condiciones subyacentes que provocaron la emisión del mensaje:

* Expone las causas raíz más probables, tales como permisos insuficientes en SELinux, saturación de inodos, agotamiento de conexiones en el pool de base de datos o latencia excesiva en el almacenamiento.
* No repite de forma redundante el texto del mensaje.


Componente 4: respuesta del operador
====================================
Indica las acciones correctivas inmediatas que el operador debe emprender:

* Redactada en modo imperativo y voz activa: "Ejecute", "Verifique", "Restaure".
* Si no se requiere acción por parte del operador, declare explícitamente: "No se requiere ninguna acción."


Tipos y niveles de severidad de mensajes
========================================

* **Error**: Identificado con el sufijo ``E``. Evento que impide la continuación de un proceso, servicio o transacción. Requiere intervención inmediata.
* **Advertencia**: Identificado con el sufijo ``W``. Condición degradada o configuración subóptima que no interrumpe el servicio inmediatamente, pero puede derivar en un fallo o degradación de rendimiento.
* **Información**: Identificado con el sufijo ``I``. Notificación de operaciones estándar, transiciones de estado programadas o hitos del ciclo de vida del clúster.


Uso disciplinado de admoniciones en Sphinx
==========================================
Para mantener el impacto pedagógico y no saturar al lector, las admoniciones deben usarse con estricta moderación:

* ``.. note::``: Información contextual relevante que complementa el texto principal sin representar una condición de riesgo.
* ``.. tip::``: Recomendaciones de optimización de rendimiento o métodos abreviados que ahorran tiempo al operador.
* ``.. important::``: Requisitos indispensables o directivas que deben cumplirse estrictamente para que el procedimiento funcione.
* ``.. warning::``: Acciones que conllevan riesgo potencial de interrupción del servicio o pérdida de disponibilidad.
* ``.. caution::``: Operaciones críticas de alto riesgo, tales como formateo de discos, destrucción de particiones o reinicio forzado de nodos de quórum, que pueden ocasionar pérdida permanente de datos.


Catálogo de trampas comunes
===========================
Siguiendo los lineamientos de la guía de estilo de GNU Press, los manuales de NorTK deben documentar proactivamente:

* **Divergencias entre versiones**: Comportamientos que cambiaron silenciosamente entre versiones de software, tales como cambios de sintaxis en ``nftables`` frente a ``iptables`` o la transición de ``cgroup v1`` a ``cgroup v2``.
* **Bloqueos y contenciones invisibles**: Bloqueos a nivel de base de datos o contenciones en almacenamiento compartido que congelan servicios sin emitir trazas de error evidentes.
* **Efectos secundarios de variables de entorno**: Variables que alteran la salida o la configuración regional de los comandos, como ``LC_ALL=C`` frente a ``es_MX.UTF-8``.
