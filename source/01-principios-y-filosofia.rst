==================================
Principios editoriales y filosofía
==================================

La documentación técnica en NorTK es tratada con el mismo rigor metodológico, cobertura de pruebas y control de versiones que el código de producción. Este módulo define la postura ética, el tono discursivo y las normas pedagógicas aplicables a toda publicación técnica.


Propósito y audiencia objetivo
==============================
Nuestros lectores son administradores de sistemas, arquitectos de infraestructura, ingenieros de operaciones y desarrolladores que operan entornos críticos de misión continua.

* **Nivel de competencia asumido**: Se asume competencia técnica sólida en sistemas operativos tipo UNIX/Linux, redes TCP/IP y administración de terminal. No se incluyen explicaciones sobre comandos básicos de shell como ``cd``, ``ls`` o ``mkdir``, a menos que involucren parámetros especializados o comportamientos no evidentes.

* **Foco operativo**: Cada documento debe resolver una necesidad real: comprender la arquitectura de un subsistema, desplegar un servicio, solucionar un incidente o consultar especificaciones precisas.


Didáctica basada en hechos
==========================
Inspirado directamente en la directriz fundamental de la guía de estilo de GNU Press:

* **Prohibición de abstracciones sin anclaje**: Nunca describa una arquitectura, algoritmo o mecanismo sin presentar de inmediato un ejemplo real, funcional y comprobable.

* **Ejemplos autosuficientes y reproducibles**: Los fragmentos de configuración y comandos deben poder copiarse y ejecutarse en un entorno limpio sin requerir suposiciones no declaradas.

* **Evitar ejemplos abstractos**: En lugar de usar identificadores abstractos como ``foo``, ``bar`` o ``temp``, utilice nombres de host, interfaces y rutas realistas como ``kvm-node01.infra.nortk.com``, ``vlan100`` o ``/var/lib/pgsql/16/data``.


Gestión de la carga cognitiva
=============================
El aprendizaje y la asimilación técnica exigen una progresión deliberada:

* **De lo simple a lo complejo**: Estructure las secciones avanzando desde los conceptos base y configuraciones estándar hacia topologías distribuidas, clustering y alta disponibilidad.

* **Regla de suficiencia exhaustiva**: Si un tema no puede cubrirse con la profundidad técnica necesaria para que el lector tome decisiones informadas, debe omitirse por completo. Las explicaciones superficiales o a medias generan falsa sensación de seguridad e inducen fallos operativos.

* **Tratamiento de estructuras recursivas y anidadas**: Al explicar subsistemas complejos, como tablas de enrutamiento con múltiples saltos, árboles de grupos en IdM o políticas RBAC en Kubernetes, divida la explicación en capas lógicas claras para no perder al lector en laberintos conceptuales.


Fundamentación empírica de juicios de valor
===========================================
En la ingeniería de infraestructura crítica, las afirmaciones deben respaldarse con datos:

* **Prohibido el dogmatismo**: Nunca declare que una herramienta, protocolo o método es útil, mejor, inseguro u óptimo sin explicar las razones técnicas subyacentes.

* **Criterios de fundamentación**: Especifique métricas cuantitativas o cualitativas concretas: impacto en latencia, consumo de memoria, aislamiento de fallos, compatibilidad POSIX o resistencia frente a condiciones de red adversas.


Voz activa y persona gramatical
===============================
Conforme a las normas editoriales canónicas:

* **Voz activa obligatoria**: El sujeto gramatical realiza la acción. Evite de forma tajante la voz pasiva.

   * *Incorrecto*: "El archivo de configuración debe ser modificado por el administrador."
   * *Correcto*: "Modifique el archivo de configuración."

* **Modo imperativo directo en procedimientos**: Redacte los pasos procedimentales utilizando verbos en modo imperativo dirigidos al operador.

   * *Correcto*: "Inicie el daemon", "Verifique el estado del clúster", "Genere los certificados X.509".

* **Consistencia de tratamiento**: Diríjase al operador de manera sobria y directa, manteniendo un registro formal y profesional.


Normas ortográficas de capitalización en títulos
================================================
Conforme a las normas académicas del español y la identidad de NorTK:

* **Prohibición estricta de mayúsculas sostenidas**: Queda tajantemente prohibido escribir títulos, encabezados o etiquetas en mayúsculas completas. Escribir en mayúsculas continuas es una falta ortográfica, perjudica el escaneo visual del operador y satura visualmente la interfaz.

* **Prohibición del estilo de titular en inglés**: En idioma español, los títulos llevan mayúscula únicamente en la letra inicial y en los nombres propios o acrónimos normalizados. Nunca aplique mayúscula a cada palabra del título.

   * *Incorrecto*: "Principios Editoriales Y Filosofía", "ARQUITECTURA MODULAR DE DOCUMENTOS".
   * *Correcto*: "Principios editoriales y filosofía", "Arquitectura modular de documentos".

* **Acrónimos normalizados**: Se mantienen en mayúsculas las siglas y acrónimos consolidados de la industria: LACP, POSIX, SELinux, KVM, CPU, RAM, DNS.


Erradicación del antropomorfismo
================================
Los componentes de cómputo, procesos y núcleos de software carecen de emociones, conciencia o voluntad:

* **Prohibición estricta**: No atribuya cualidades humanas al software o al hardware.

   * *Incorrecto*: "El kernel decide inteligentemente enviar el tráfico por la ruta secundaria."
   * *Correcto*: "El kernel enruta el tráfico a través de la puerta de enlace secundaria según la métrica configurada."

   * *Incorrecto*: "El servicio piensa que el clúster está degradado y pide ayuda."
   * *Correcto*: "El servicio detecta la pérdida de quórum y registra una alerta en el registro del sistema."


Identificación proactiva de trampas operativas
==============================================
Un manual de excelencia se distingue por advertir de los problemas antes de que sucedan:

* **Visibilizar aristas filosas**: Documente explícitamente discrepancias sutiles de comportamiento, condiciones de carrera, bloqueos de archivos o diferencias entre versiones de paquetes.

* **Uso disciplinado de advertencias**: Reserve las directivas ``.. warning::`` y ``.. caution::`` exclusivamente para situaciones que involucren riesgo de pérdida de datos, interrupción de servicios o vulnerabilidades de seguridad.


Accesibilidad estructural y coherencia auditiva
===============================================
La claridad técnica debe trascender el medio de visualización:

* **Disciplina del lector de pantalla**: El texto debe poseer una estructura lógica tan robusta que resulte plenamente comprensible al ser procesado secuencialmente por sintetizadores de voz, como Orca, Festival o Emacspeak.

* **Marcado lógico sobre tipográfico**: Emplee marcado semántico: referencias cruzadas, directivas formales y roles de dominio en lugar de recursos puramente gráficos. No dependa de elementos visuales aislados para comunicar información esencial.
