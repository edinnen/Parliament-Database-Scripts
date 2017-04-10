#!/bin/bash

#cp messyCanadaNeedsToBeNotSo.py en
#cp messyCanadaNeedsToBeNotSo.py fr

#cd ../en
numFiles=$(ls | wc -l)
let "i=0"

for file in *;
do
		python ../messyCanadaNeedsToBeNotSo.py $file
		echo "scale=3; $i/$numFiles*100" | bc
		let "i += 1"
done

mkdir ../unclean
/bin/bash ../findUncleaned.sh

#cd ../fr
#numFiles=$(ls | wc -l)
#let "i=0"

#for file in *;
#do
		#python ../messyCanadaNeedsToBeNotSo.py $file
		#echo "Done: $file -- $(bc -l <<< $i/$numFiles*100)"
		#let "i += 1"
#done
