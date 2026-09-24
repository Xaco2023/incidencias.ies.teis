# Manual de Instalación de la Aplicación Web
## Decisiones de Proyecto
|Elemento|Decisión|Versión|Justificación|
|--------|--------|-------------|-------|
|Sistema operativo|Ubuntu 26 LTS||Entorno Linux real|
|Servidor Web|Apache|2|Sencillo de Usar|
|Base de Datos|MySQL|8|Experiencia Previa|
|Lenguaje Servidor|Python|3|Interesante y uso extendido|
|Framework|Flask|3|Sencillo de usar, pensado para web|
|Control de versiones|Git|2|Muy extendido|
|Documentación|Markdown|-|Muy usado con Github|

## Proceso de instalación
1. Actualizar el sistema
```
sudo apt update
sudo apt upgrade
```
2. Instalar Git
```
sudo apt install git
```
3. Instalar VSCode + plugins
```
Instalamos Markdown
```
4. Instalamos Apache2
```
sudo apt install apache2
```
5. Cambiar permisos
```
sudo chown -R $USER:$USER /var/www/html
sudo chmod -R u=rwX,go=rX /var/www/html
```
6.  Cambiar pagina por defecto
```
sudo gedit /etc/apache2/sites-available/incidencias.ies.teis
```
```
    <VirtualHost *:80>
    ServerAdmin admin@reservas.xac
    ServerName reservas.xac
    DocumentRoot /var/www/reservas.xac

    <Directory /var/www/reservas.xac>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/reservas.xac_error.log
    CustomLog ${APACHE_LOG_DIR}/reservas.xac_access.log combined
</VirtualHost>
```
```
sudo a2dissite 000-default.conf
sudo a2ensite incidencias.ies.teis.conf
systemctl reload apache2
```
7. En /etc/hosts añadimos 127.0.0.1 incidencias.ies.teis
```
sudo nano /etc/hosts
```
8. Añadir a git
```
git init
git add .
git commit -m "Commit inicial con readme y pagina principal con formulario web"
```
9. Añadir a Github
```
En Github seleccionamos New y luego usamos los comandos indicados para añadir desde la máquina virtual a Github

```
10. Instalar MySQL Server
```bash
sudo apt install mysql-server
```
11. Configuramos MySQL
```
sudo mysql
create database incidencias;
create user 'incidencias'@'localhost' identified by 'incidencias';
grant all privileges on incidencias.* to 'incidencias'@'localhost';
flush privileges;
```
12. Crear tabla en incidencias
```
use incidencias
create table registro(
    id int auto_increment primary key,
    usuario varchar(30),
    aula varchar(30),
    descripcion text,
    extado varchar(30)
    );
```
13. Insertart datos
```
insert into registro (,,,) values ('','','')
```

## Configuracion de Git/Github
1. Crear repositorio local, añadir archivos y commit
```

```



# Manual instalación aplicación web
```bash
pip install flask
pip install mysql-connector-python
pip list
pip freeze > requirements.txt
```

# Rutina de trabajo con Flask 
```bash
cd /var/www/incidencias.ies.teis
source venv/bin/activate
python app.py # Lanzar app
```
```bash
ctrl-c
deactivate
```

```python
import mysql.connector
```


source venv/bin/activate


sudo a2enmod proxy
sudo a2enmod proxy_http
sudo systemctl restart apache2