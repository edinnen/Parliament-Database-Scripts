#!/bin/bash

#cd ./en
numFiles=$(ls | wc -l)
let "i=0"

for file in **; do
  #echo "Finding uncleaned (XML): $(bc -l <<< $i/$numFiles*100)"
  echo "scale=3; $i/$numFiles*100" | bc
  python ../findUncleaned.py $file
  let "i += 1"
done

cd ../unclean
numFiles=$(ls | wc -l)
let "i=0"

for file in **; do
  #echo "Cleaning the uncleaned (XML): $(bc -l <<< $i/$numFiles*100)"
  echo "scale=3; $i/$numFiles*100" | bc
  python ../XMLCleaner.py $file
  let "i += 1"
done

mv * ../fr

cd ../
/bin/bash condenser.sh


# cd ../fr
# numFiles=$(ls | wc -l)
# let "i=0"
#
# for file in **; do
#   echo $(bc -l <<< $i/$numFiles*100)
#   python ../findUncleaned.py $file
#   let "i += 1"
# done
