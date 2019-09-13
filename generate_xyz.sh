#!/bin/bash


#for i in [1..1031]
#do
#    name=`awk '{if (NR==${i}) print$0 }' PAH_data.txt`
#    echo $name
#done

while read p; do
      echo "$p"

  wget -O PAH_database/${p}.xyz https://cactus.nci.nih.gov/chemical/structure/${p}/file?format=xyz
  done <PAH_data.txt
