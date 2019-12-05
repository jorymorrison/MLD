#!/bin/bash
depth=1
input="/home/matthew/MLD/urls.txt"
regex='*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html'
echo 'https://www.cnn.com/' > urls.txt
COUNTER=0
while [  $COUNTER -lt $depth ]; do
	echo $COUNTER
	while IFS= read -r line
	do
		echo "$line"
		echo "$line" | xargs -n1 curl | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0'>>temp.txt
	done < $input
	while IFS= read -r line
	do
		echo "$line" >>urls.txt
	done < temp.txt
	let COUNTER=COUNTER+1
done
sort urls.txt | uniq -u > sorted.txt

while read a
do
	echo $a
	python3 Main.py $a
done < sorted.txt
