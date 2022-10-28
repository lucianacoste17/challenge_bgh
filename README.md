# Transformar un archivo xslx a csv 

### Pre-requisitos 📋

_La transformacion la hacemos con librerias externas por lo tanto debemos 
comprimirlas , subirlas al cubo s3 y configurar en lambda layers la importacion de las librerias comprimidas en zip.
instalamos los paquetes en una instancia de ec2 ya que es el mismo S.O en donde se ejecuta lambda para evitar que falle por error de dependencias_

_Creamos un directorio_
```
$ mkdir –p build/python/lib/python3.7/site-packages 

```
_Descargamos los paquetes que vamos a utilizar_

```
$ cd  

$ sudo yum install gcc-c++  


$ pip install --target build/python/lib/python3.7/site-packages pandas xlrd fsspec sfs3 openpyxl  

```
_comprimimos la carpeta_

```
$ cd build
  
$ zip -r pandas_layer.zip .
```

_Movemos a s3 _
```
$ aws s3 cp pandas_layer.zip s3://bucket/xslx/input/pandas_layer.zip 

```
_configuracion en lambda --> lambda layers --> selecc. cargar file desde s3 ---> lambda ---> crear funcion 
                          -->capas--> agregar una capa -->capa personalizada_