## Proyecto 5
Proyecto de la semana 5 y 6 bootcamp Data

## TÍTULO 


## Objetivo del proyecto

El objetivo es ver si el nuevo diseño conduce a una mejor experiencia de usuario y mayores tasas de finalización del proceso.






## Contexto del negocio
Se puso en marcha una prueba A/B desde el día 15/3/2017 al 20/6/2017

Teniendo dos grupos de estudio: Test y Control.

-El grupo de control correspondía a los clientes que interactuaron con el proceso en línea tradicional de Vanguard.

-El grupo de test correspondía a los clientes que experimentaron la nueva interfaz digital mejorada.

Ambos grupos navegaron a través de una secuencia de proceso idéntica: una página inicial, tres pasos subsiguientes y, finalmente, una página de confirmación que señalaba la finalización del proceso.





----


## Dataset
Los datasets utilizados son tres:

- El primero (df_final_demo) recoge los registros de datos demográficos de los clientes de Vanguard que poseen una cuenta. 
- Hay dos data set (df_final_web_data_pt_1 y df_final_web_data_pt_2) los cuales unimos y contienen los registros detallados de las visitas en linea de los clientes. 
- Un último dataset (df_final_experiment_clients) que recoge los clientes que fueron parte del estudio de Vanguard.

Las variables principales utilizadas en el análisis son:  
"edad", "sexo", "pasos","tiempo", "años de fidelización", "tipo (test o control)"


## Notas sobre la calidad del dato
El dataset presenta problemas de datos faltantes que han requerido procesos de limpieza y agregar columnas:

- Valores nulos en algunas filas y columnas.
- Datos duplicados.
- Separación de la información para obtener diferentes columnas.
- Problemas en los tipos de datos
- Variables continuas que llevamos a discretas agrupandolas en intervalos.

Se han tomado decisiones de limpieza y estandarización para garantizar la coherencia del análisis y la cantidad de datos de estudio por lo que nos hemos centrado en dos grupos de estudio: Test y Control.


---


## Preguntas clave / Hipótesis
- Para iniciar con el estudio antes de observar los clientes de Test y/o Control nos hicimos las siguientes preguntas ¿Cómo es el perfil general del cliente de Vanguard? ¿Cuál es la hora en la que más se realizan las visitas en linea? 
- 


## Proceso de análisis
El análisis incluye:
- Exploración inicial del dataset (EDA).
- Limpieza y estandarización de variables.
- Creación de nuevas variables/columnas.
- Análisis descriptivo y comparativo mediante tablas y gráficos.
- Análisis de correlación entre variables.
- Análisis de KPIs
- Creación de hipótesis 
- Comprobación de la validez de las hipótesis con tests estadísticos.


## Resultados / Insights
-


---


## Recomendaciones de negocio
- 


## Limitaciones
- 



## Próximos pasos
- 



---


## Cómo replicar el proyecto
1. Clonar el repositorio.
2. Instalar las librerías necesarias (`pandas`,`numpy`,`matplotlib`,`seaborn`,`functions`,`statsmodels.api`,`scipy.stats.contingency`,`scipy.stats.mannwhitneyu`,`scipy`).
3. Ejecutar el notebook a través de github.

