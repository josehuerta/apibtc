## API BTC a MXN

#### Introducción
Esta api te permitira conocer un listado de precios del bitcoin en pesos mexicanos a lo largos de las ultimas 24 horas, la ultima semana, el ultimo mes, el ultimo año o en un rango de fechas especifico.

Se contiene precios del bitcoin desde el 24/12/2019 hasta el 25/02/2021 , obtienendo registros del 24/12/2019 al 17/02/2021 en un intervalo de 24 hrs y del 18/02/2021 al 25/02/21 en un intervalo de 2 horas, en espefico las horas pares. 

#### Sugerencia: antes del clonar el proyecto, se recomienta que utilices un entorno virtual (env) para aislar las dependencias de este con las de tus otros proyectos, en este caso se recomienta utilizar virtualenv
**Entorno virtual en windows**

`$ pip install virtualenv`

`$ virtualenv <tu-env>`

`$ cd <tu-env>\Scripts`

`$ Scripts>activate`

**Entorno virtual en linux/mac**

`$ pip install virtualenv`

`$ virtualenv <tu-env>`

`$ source <tu-env>/bin/activate`

Una vez instalado virtualenv, creado tu entornovirtual y activandolo, puedes continuar con los siguientes pasos.

#### Clonar el proyecto
Para clonar el proyecto ejecuta los siguientes comandos en tu terminal de comandos (en el orden que se mencionan):

`$ git clone https://github.com/josehuerta/apibtc.git `

`$ cd apibtc`

#### Instalación de dependencias
Para instalar las dependencias debes ubicarte dentro de tu carpeta apibtc y ejecutar el siguiente comando:

`$ pip install -r requirements.txt`

requirements.txt es el archivo donde se encuentra la lista de dependencias de este proyecto.

#### Ejecutar el proyecto
Para ejecutar el proyecto deberas estar ubicado dentro de tu carpeta apibtc y ejecutar el siguiente comando:

`$ python manage.py runserver`

#### Documentación 
La documentacion podras encontrarla en el siguiente enlace:

`https://josehuerta.github.io/documentacionApiBtc/`

#### Version de python utilizada 
3.7.5
