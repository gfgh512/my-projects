# Solicitar al usuario que ingrese su nombre de usuario
$USER = Read-Host "Por favor, ingresa tu nombre de usuario de PostgreSQL:"

# Solicitar al usuario que ingrese su contraseña
$PASSWORD = Read-Host "Por favor, ingresa tu contraseña de PostgreSQL:" -AsSecureString

# Solicitar al usuario que ingrese el nombre del host
$SERVER_ = Read-Host "Por favor, ingresa el nombre del host de PostgreSQL:"

# Solicitar al usuario que ingrese el puerto
$PORT_ = Read-Host "Por favor, ingresa el puerto de PostgreSQL:"

# Solicitar al usuario que ingrese el nombre de la base de datos
$DB_NAME = Read-Host "Por favor, ingresa el nombre de la base de datos a crear:"

# Solicitar al usuario que ingrese el nombre del esquema
$SCHEMA_NAME = Read-Host "Por favor, ingresa el nombre del esquema a crear:"

# Comando para crear la base de datos
$env:PGPASSWORD = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($PASSWORD))
psql -U $USER -h $SERVER_ -p $PORT_ -c "CREATE DATABASE $DB_NAME;"

# Comando para crear el esquema
psql -U $USER -h $SERVER_ -p $PORT_ -d $DB_NAME -c "CREATE SCHEMA $SCHEMA_NAME;"

# Preguntar al usuario si desea otorgar privilegios a otro usuario
$GRANT_PRIVILEGES = Read-Host "¿Deseas otorgar privilegios de lectura y escritura a otro usuario? (s/n)"

if ($GRANT_PRIVILEGES -eq "s") {
    $OTHER_USER = Read-Host "Por favor, ingresa el nombre del usuario al que deseas otorgar privilegios:"
    psql -U $USER -h $SERVER_ -p $PORT_ -d $DB_NAME -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $OTHER_USER;"
    psql -U $USER -h $SERVER_ -p $PORT_ -d $DB_NAME -c "GRANT ALL PRIVILEGES ON SCHEMA $SCHEMA_NAME TO $OTHER_USER;"
}