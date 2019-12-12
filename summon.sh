#!/bin/bash
start=$1
depth=$2
input="$HOME/MLD/urls.txt"
regex='*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html'
echo $1 > urls.txt
echo "filler" > scan.txt
echo "" > temp.txt
COUNTER=0
while [  $COUNTER -lt $depth ]; do
	echo $COUNTER
	while IFS= read -r line
	do
		if grep -Fxq "$line" scan.txt
		then
			continue
		else
			echo "$line" >> scan.txt
			echo "$line" | xargs -n1 curl | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0'>>temp.txt
		fi
	done < $input
	while IFS= read -r line
	do
		echo "$line" >>urls.txt
	done < temp.txt
	echo "" > temp.txt
	let COUNTER=COUNTER+1
done
sort urls.txt | uniq -u > sorted.txt

while read a
do
	echo $a
	python3 Main.py $a
done < sorted.txt







