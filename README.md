# Optimización de la interfaz digital: 
*Estudio A/B de interfaz digital en Vanguard*

**Constanza Segovia Aspee**  
**Carmen Ríos Rodríguez** 

## Objetivo del proyecto
El objetivo de este proyecto es evaluar si la implementación de una nueva interfaz de usuario más intuitiva y con asistencia contextual aumenta la tasa de finalización del proceso de inversión en línea. A través de un análisis de datos exhaustivo, buscamos determinar si los cambios de diseño impactan de manera positiva y significativa en el comportamiento del cliente.


## Contexto del negocio
Se puso en marcha una prueba A/B desde el día 15/3/2017 al 20/6/2017

Teniendo dos grupos de estudio: Test y Control.

-El grupo de control correspondía a los clientes que interactuaron con el proceso en línea tradicional de Vanguard.

-El grupo de test correspondía a los clientes que experimentaron la nueva interfaz digital mejorada.

Ambos grupos navegaron a través de una secuencia de proceso idéntica: una página inicial, tres pasos subsiguientes y, finalmente, una página de confirmación que señalaba la finalización del proceso.

El desafío consiste en decidir, basándose en evidencia estadística, si se debe implementar globalmente la nueva interfaz o mantener el sistema tradicional.


## Dataset
**Fuentes**

- El primero (df_final_demo) recoge los registros de datos demográficos de los clientes de Vanguard que poseen una cuenta. 
- Hay dos data set (df_final_web_data_pt_1 y df_final_web_data_pt_2) los cuales unimos y contienen los registros detallados de las visitas en linea de los clientes. 
- Un último dataset (df_final_experiment_clients) que recoge los clientes que fueron parte del estudio de Vanguard.

**Diccionario breve (dataset final)**

`client_id`: identificador único del cliente.

`años_fidelizacion`: antigüedad del cliente en la empresa (en años).

`meses_fidelizacion`: antigüedad del cliente en la empresa (en meses).

`edad`: edad del cliente (con valores imputados).

`sexo`: género del cliente (M, F, U).

`cuentas`: número total de cuentas que posee el cliente.

`saldo_total_distribuido`: saldo total acumulado en las cuentas (EUR/USD).

`logins_ultimos_6meses`: frecuencia de inicios de sesión en los últimos 6 meses.

`tipo`: grupo asignado en el experimento (Test o Control).

`confirmacion`: indicador de si el cliente finalizó el proceso (True / False).

`paso`: la posición del cliente en el proceso de la prueba. 

`segundos_visita`: la cantidad de segundos de visita de un cliente en la plataforma. 



## Notas sobre la calidad del dato
El dataset presenta problemas de datos faltantes que han requerido procesos de limpieza y agregar columnas:

- Valores nulos en algunas filas y columnas.
- Datos duplicados.
- Separación de la información para obtener diferentes columnas.
- Problemas en los tipos de datos
- Variables continuas que llevamos a discretas agrupandolas en intervalos.

Se han tomado decisiones de limpieza y estandarización para garantizar la coherencia del análisis y la cantidad de datos de estudio por lo que nos hemos centrado en dos grupos de estudio: Test y Control. Además, se unificaron formatos de nombres de columnas para facilitar la manipulación y se validó la ausencia de duplicados que pudieran alterar los resultados de la prueba A/B.


---


## Preguntas clave / Hipótesis
Para iniciar con el estudio antes de observar los clientes de Test y/o Control nos hicimos las siguientes preguntas: 
- ¿Cuál es el perfil general del cliente de Vanguard? 
- ¿Cuál es la hora en la que más se realizan las visitas en linea? 
- ¿Existe una diferencia estadísticamente significativa en la tasa de finalización entre el grupo de Control y el de Prueba?
- ¿Cómo afecta el nuevo diseño al tiempo que los usuarios pasan en cada paso del proceso?
- ¿Mejora la interfaz la experiencia del cliente? 
- ¿Se han cumplido los objetivos?


## Proceso de análisis
El análisis incluye:
- Exploración inicial del dataset (EDA)
- Limpieza y estandarización de variables
- Creación de nuevas variables/columnas
- Análisis descriptivo y comparativo mediante tablas y gráficos
- Análisis de correlación entre variables
- Análisis de KPIs
- Creación de hipótesis 
- Comprobación de la validez de las hipótesis con tests estadísticos
- Preparación de visualizaciones en Tableau


#### Resultados clave y comportamiento del cliente 

**Perfil**
    
    Los principales usuarios del sistema tienen una edad promedio de 46.4 años y una antigüedad de 12 años en la empresa. Los grupos de género masculino y femenino son los más veteranos, con una mediana de fidelización de 14 años, mientras que el grupo desconocido es más reciente, con una mediana de 6 años.

**Engagement**
    
    Los hombres mostraron una actividad ligeramente superior con una mediana de 6 inicios de sesión en los últimos 6 meses, frente a los 5 inicios de sesión de las mujeres y el grupo de género desconocido. Los grupos femenino y desconocido mantienen una actividad constante con una mediana de 5 inicios de sesión en el mismo periodo.

**Promedios**
    
    El promedio de cuentas por cliente es de 2.25, con un saldo total distribuido medio significativo, lo que indica que el proceso en línea es crítico para usuarios con activos considerables.


**Diferencia entre grupos**
    
    El análisis concluye que hay una diferencia significativa entre las muestras del grupo de Control y Test, lo que indica que el cambio de diseño sí impactó de forma medible el comportamiento de los usuarios, pero no respecto a la expectativa de Vanguard.



## Recomendaciones de negocio
- Implementación estratégica: Dado que el impacto es medible pero no necesariamente cumplió con todas las expectativas iniciales de Vanguard, se recomienda una implementación por fases enfocada en los segmentos que mostraron mayor receptividad. Valorándose también una implementación híbrida entre aquellos usuarios que elijan la parte digital frente a aquellos que elijan la analógica.  

- Optimización para nuevos usuarios: El diseño parece atraer a un perfil más joven o nuevo. Se sugiere optimizar los mensajes contextuales específicamente para facilitar el "onboarding" de este segmento. 

- En relación con los logins y la cantidad de llamadas relacionadas con el proceso en línea, para optimizar tiempos, resultados y espperas, podría ser interesante instauurar una herramienta digital (por ejemplo, un chatbot) para que aquellos usuarios tengan una primera línea de ayuda sin tener que recurrir al método tradicional. 


## Limitaciones
- Ausencia de datos cualitativos: El análisis se basa puramente en el comportamiento transaccional y logs de navegación. No disponemos de datos sobre el nivel de satisfacción subjetiva del usuario (como encuestas) que expliquen el sentimiento detrás de su comportamiento dentro de la plataforma.

- Aunque conocemos el éxito final, el dataset actual dificulta identificar con precisión los patrones de abandono específicos en cada transición de paso. No podemos determinar si el abandono se debe a fallos técnicos en la interfaz, falta de claridad en las instrucciones o factores externos al diseño.

- El análisis se limita a un periodo específico de tiempo (marzo a junio de 2017), lo que podría no capturar variaciones estacionales en el comportamiento de inversión.



## Próximos pasos
- Análisis de embudos (Funnels): Desglosar la tasa de abandono paso a paso para identificar cuellos de botella específicos en la nueva interfaz.

- Segmentación avanzada: Realizar un análisis RFM (Recencia, Frecuencia, Valor Monetario) para entender si los clientes de alto patrimonio prefieren la interfaz tradicional o la moderna.

- Nuevos estudios y análisis que incorporen las herramientas o procedimientos descritos en las limitaciones. 




## Cómo replicar el proyecto
Instrucciones exactas (entorno, dependencias, y orden recomendado):

1. Clonar el repositorio.
2. Descarga de archivos csv.
3. Instalar las librerías necesarias (`pandas`,`numpy`,`matplotlib`,`seaborn`,`functions`,`statsmodels.api`,`scipy.stats.contingency`,`scipy.stats.mannwhitneyu`,`scipy`).
4. Ejecutar el notebook Análisis.
5. Visualizar los datos en enlace de Tableau: 

