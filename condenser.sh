#!/bin/bash

touch fr.txt
cd fr
numFiles=$(ls | wc -l)
let "i=0"

for file in **; do
	echo "scale=3; $i/$numFiles*100" | bc
	cat $file >> ../fr.txt
	let "i+=1"
done

mv ../fr.txt ../../../
cd ../../../
/bin/bash pokevecTrainer.sh
