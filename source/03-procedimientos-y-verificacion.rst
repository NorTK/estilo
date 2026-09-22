========================================
Procedimientos operativos y verificación
========================================

En los entornos de infraestructura crítica de NorTK, un error en una receta de despliegue puede provocar la caída de un clúster o la corrupción de datos. Todo módulo de procedimiento debe cumplir de forma inexcusable con el contrato de cinco bloques adoptado del modelo de ingeniería de Red Hat Enterprise Linux 10.


El contrato de cinco bloques
============================
Cada procedimiento técnico se redacta como una unidad atómica y secuencial integrada por:

#. Propósito y contexto operativo
#. Prerrequisitos
#. Procedimiento paso a paso
#. Verificación determinista
#. Recursos adicionales


Bloque 1: propósito y contexto operativo
========================================
Una o dos oraciones introductorias que establecen claramente qué se va a lograr, en qué nodo o componente se realiza la acción y el perfil del operador.

* **Ejemplo canónico**: "Como administrador de sistemas, configure un enlace de red agregado en modo LACP bajo la norma 802.3ad para proporcionar alta disponibilidad y balanceo de carga en los nodos de cómputo KVM."


Bloque 2: prerrequisitos
========================
Lista exhaustiva y comprobable de todas las condiciones que el sistema debe cumplir antes de que el operador ejecute el primer comando:

* Permisos requeridos: acceso como superusuario ``root`` o privilegios mediante ``sudo``.
* Paquetes de software instalados con sus nombres de paquete exactos en los repositorios corporativos.
* Servicios en ejecución o dependencias de red activas: puertos de red abiertos y resolución DNS funcional.
* Estado previo de almacenamiento o conectividad, como dos interfaces físicas de 10 GbE sin configuración IP previa.


Bloque 3: procedimiento paso a paso
===================================
Secuencia cronológica y determinista de pasos numerados con la directiva ``#.``:

* **Verbos en imperativo**: Cada paso inicia con una orden directa: Inicie, Cree, Edite, Aplique.
* **Comandos exactos en bloques de código**: Se presentan en bloques ``.. code-block:: bash`` limpios y sin la opción ``:caption:``.
* **Desglose de parámetros**: Inmediatamente después del comando, se desglosan las banderas y parámetros no evidentes.


Bloque 4: verificación determinista
===================================
Mandatorio en la totalidad de los procedimientos. Ninguna tarea se considera finalizada sin validación empírica.

* **Comando de auditoría**: El comando exacto para inspeccionar el estado, como ``systemctl status``, ``ip addr show``, ``podman ps``, ``lsblk -f`` o ``zpool status``.
* **Salida esperada**: Bloque literal de terminal que muestra exactamente lo que el operador debe ver en su pantalla para confirmar el éxito de la operación.
* **Criterios de validación**: Indicación explícita de qué campos o cadenas de texto indican conformidad, como verificar que el estado sea UP y que el modo reporte 802.3ad.


Bloque 5: recursos adicionales
==============================
Enlaces puntuales y referencias formales para profundizar o solucionar anomalías:

* Páginas man del sistema con su sección correspondiente.
* Módulos de concepto o referencia complementarios dentro del catálogo NorTK.
* Documentación oficial upstream o RFCs pertinentes.


Manejo de privilegios y prompts de terminal
===========================================
Para prevenir ejecuciones accidentales con privilegios incorrectos:

* **Prompt de superusuario**: Se utiliza el caracter almohadilla ``#`` exclusivamente cuando el comando debe ejecutarse como ``root`` o con ``sudo``.
* **Prompt de usuario ordinario**: Se utiliza el caracter dólar ``$`` cuando el comando debe ejecutarse bajo una cuenta de servicio sin privilegios o en el espacio de usuario.
* **Prohibición de mezcla**: No combine comandos de usuario y de superusuario en el mismo bloque de terminal sin indicar claramente la transición de privilegios.


Plantilla canónica de procedimiento
===================================
Estructura de referencia en reStructuredText para redactar procedimientos en NorTK:

.. code-block:: rst

   =======================================
   Configuración de enlaces de red bonding
   =======================================

   Como administrador de infraestructura, configure una interfaz de enlace
   agregado en modo LACP para garantizar redundancia y tolerancia a fallos
   en el tráfico de red de almacenamiento.


   Prerrequisitos
   ==============
   * Acceso administrativo como usuario ``root``.
   * Paquete ``NetworkManager`` instalado y en ejecución.
   * Dos interfaces físicas de red conectadas a un switch con soporte LACP.


   Procedimiento
   =============
   #. Cree la conexión maestra de tipo bond:

      .. code-block:: bash

         # nmcli connection add type bond con-name bond0 ifname bond0 bond.mode 802.3ad

   #. Asigne los puertos físicos como subordinados del enlace:

      .. code-block:: bash

         # nmcli connection add type ethernet con-name bond0-port1 ifname enp3s0f0 master bond0
         # nmcli connection add type ethernet con-name bond0-port2 ifname enp3s0f1 master bond0

   #. Configure la dirección IP estática y la puerta de enlace:

      .. code-block:: bash

         # nmcli connection modify bond0 ipv4.addresses 192.168.10.50/24 ipv4.method manual

   #. Active el enlace bond0:

      .. code-block:: bash

         # nmcli connection up bond0


   Verificación
   ============
   #. Inspeccione el estado del enlace bonding en el kernel:

      .. code-block:: bash

         # cat /proc/net/bonding/bond0

      Salida esperada:

      .. code-block:: text

         Ethernet Channel Bonding Driver: v6.6.0

         Bonding Mode: IEEE 802.3ad Dynamic link aggregation
         Transmit Hash Policy: layer2 (0)
         MII Status: up
         MII Polling Interval (ms): 100
         Up Delay (ms): 0
         Down Delay (ms): 0

         Slave Interface: enp3s0f0
         MII Status: up
         Speed: 10000 Mbps
         Duplex: full

         Slave Interface: enp3s0f1
         MII Status: up
         Speed: 10000 Mbps
         Duplex: full

   #. Compruebe que ambos puertos subordinados reportan estado activo y
      que la velocidad agregada corresponde a la negociación del switch.


   Recursos adicionales
   ====================
   * Página man de nmcli en la sección 1.
   * Archivo bonding.txt en la documentación del kernel Linux.
