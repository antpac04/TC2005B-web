# team4-web

## Instrucciones de configuración

1. Clonar el repositorio
2. Iniciar un servidor de MySQL
3. Crear una base de datos llamada Space_Adventures 
```
> CREATE DATABASE Space_Adventures;
```
4. Crear un entorno virtual
```
> python3 -m venv venv
> source venv/bin/activate
```

5. Instalar dependencias
```
> pip3 install -r requirements.txt
```

6. Crear un archivo .env, siguiendo el formato de .env.sample

7. Correr el comando 
```
> flask --app api init-db
```

8. Iniciar el servidor
```
> flask --app api run
```

## Deploy

Tanto la API como el frontend fueron subidos a la nube usando el servicio EC2 de AWS. Puede consultar el front desplegado en la siguiente url:
http://18.219.42.109:3000/
Para navegar a la sección de gráficas, use la URL:
http://18.219.42.109:3000/dashboard
