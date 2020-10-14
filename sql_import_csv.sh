#!/bin/env bash


function mysql_import {
  mysqlimport --local --fields-terminated-by=',' --lines-terminated-by='\r\n' $1 $2
}

# main block

database=""
while true; do
  touch default_sql.csv
  for file in `find . -cnewer default_sql.csv | sed '$d'`
  do
     epoch_time = `stat -c'%Z' $file`
     touch $epoch_time default_sql.csv
     mysql_import $database  $file
     if [ $? ]; then
       echo ": an error occured"
     fi
   done
 done
