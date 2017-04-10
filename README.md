# Parliament Database Scripts
This repo contains python and bash to modify all publicly avaliable Canadian parliament transcripts in English and French from http://www.parl.gc.ca/

The end data was used in a program which used Google's Word2Vec algorithm to train vectors based on both the English and French translations. Statistical tests were used to determine deviation of position (among other tests) for each word and its translation inside their repsective vectors. The end goal was to test for linguistic effects and machine translation effectiveness. All transcripts were downloaded in their HTML/XML formats.

## Cleaning scripts
### messyCanadaNeedsToBeNotSo.py
### XMLCleaner.py

These scripts cleans downloaded HTML and XML files. They expand contractions convert numerals to typed out words, removes unwanted unicode characters, expands honorific titles like Hon and Mlle, and removes HTML and XML tagging

## deleteChaoticData.py

Removes unwanted files under 500 lines long

## iWouldCleanACanadaThough.sh

Clean all files

## findUncleaned bash and python files

Ensures no uncleaned files remains. Sort and clean any files found with remaining markup tags

## runDelete.sh 

Begin chain of script operations. Deletes short files and begin cleanings

## conderser.sh

Condense all cleaned files into one file for each language (en.txt & fr.txt). Then run the Word2Vec trainer to output vector files
