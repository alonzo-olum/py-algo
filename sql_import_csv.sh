#!/bin/env bash

mysql_import {
  mysqlimport --local --fields-terminated-by=',' --lines-terminated-by='\r\n' $1 $2
}

# main block
local db = ""
while true\
do
  touch default_sql.csv
  for file in `find . -cnewer default_sql.csv | sed '$d'`
  do
     epoch_time = stat -c'%Z' $file
     touch $epoch_time default_sql.csv
     mysql_import $db  $file
     if [ $? ]; then
       echo ": an error occured "
   done;
