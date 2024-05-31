#!/bin/bash

# Solicitar al usuario que ingrese su nombre de usuario
echo "Por favor, ingresa tu nombre de usuario de PostgreSQL:"
read USER

# Solicitar al usuario que ingrese su contraseña
echo "Por favor, ingresa tu contraseña de PostgreSQL:"
read -s PASSWORD

#Solicitar al usuario que ingrese el nombre del host
echo "Por favor, ingresa el nombre del host:"
read HOST_

# Solicitar al usuario que ingrese el puerto
echo "Por favor, ingresa el puerto:"
read PORT_

# Solicitar al usuario que ingrese el nombre de la base de datos
echo "Por favor, ingresa el nombre de la base de datos a crear:"
read DB_NAME

# Solicitar al usuario que ingrese el nombre del esquema
echo "Por favor, ingresa el nombre del esquema a crear:"
read SCHEMA_NAME

# Comando para crear la base de datos
PGPASSWORD=$PASSWORD psql -U $USER -h $HOST_ -p $PORT_ -c "CREATE DATABASE $DB_NAME;"

# Comando para crear el esquema
PGPASSWORD=$PASSWORD psql -U $USER -h $HOST_ -p $PORT_ -d $DB_NAME -c "CREATE SCHEMA $SCHEMA_NAME;"

# Preguntar al usuario si desea otorgar privilegios a otro usuario
echo "¿Deseas otorgar privilegios de lectura y escritura a otro usuario? (s/n)"
read GRANT_PRIVILEGES

if [ "$GRANT_PRIVILEGES" = "s" ]; then
    echo "Por favor, ingresa el nombre del usuario al que deseas otorgar privilegios:"
    read OTHER_USER
    PGPASSWORD=$PASSWORD psql -U $USER -h $HOST_ -p $PORT_ -d $DB_NAME -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $OTHER_USER;"
    PGPASSWORD=$PASSWORD psql -U $USER -h $HOST_ -p $PORT_ -d $DB_NAME -c "GRANT ALL PRIVILEGES ON SCHEMA $SCHEMA_NAME TO $OTHER_USER;"
fi