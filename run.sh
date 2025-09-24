#!/bin/bash
# Script lanzador para un solo fichero Python

# Colores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # Sin color

# Añadir la raíz del proyecto al PYTHONPATH
export PYTHONPATH=$(pwd)

# Si no hay argumento, mostrar ayuda
if [ $# -eq 0 ]; then
  echo -e "${RED}Uso:${NC} $0 <ruta/al/fichero.py>"
  echo -e "${YELLOW}Ejemplo:${NC} $0 code-basketball-files/code/02-python/10_read_csv.py"
  exit 1
fi

script="$1"

# Comprobar si existe el fichero
if [ ! -f "$script" ]; then
  echo -e "${RED}Error:${NC} Fichero '$script' no encontrado"
  exit 1
fi

# Ejecutar el fichero
echo -e "${GREEN}>>> Ejecutando: $script${NC}"
python "$script"
echo -e "${GREEN}>>> Finalizado: $script${NC}"
