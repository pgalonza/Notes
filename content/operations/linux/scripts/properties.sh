#! /bin/nash

function read_properties {
  grep "${1}" <file_name>.properties|cut -d'=' -f2|tr -d '[:space:]'
}

WORK_DIR="$(dirname "$0")"
cd $WORK_DIR

export <variable_name> = $(read_properties <'parameter_name'>)
