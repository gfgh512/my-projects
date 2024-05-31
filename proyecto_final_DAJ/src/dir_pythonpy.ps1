# Este script se encarga de añadir el directorio actual al PYTHONPATH
$env:PYTHONPATH += ";$(Get-Location)"