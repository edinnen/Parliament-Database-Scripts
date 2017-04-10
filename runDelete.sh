#!/bin/bash

#cd en
#numFiles=$(ls | wc -l)
#let "i=0"

#for file in **; do
#  echo "scale=3; $i/$numFiles*100" | bc
#  python ../deleteChaoticData.py $file
#  let "i += 1"
#done

 cd fr
 numFiles=$(ls | wc -l)
 let "i=0"

 for file in **; do
   echo $(bc -l <<< $i/$numFiles*100)
   python ../deleteChaoticData.py $file
   let "i += 1"
 done

/bin/bash ../iWouldCleanACanadaThough.sh
