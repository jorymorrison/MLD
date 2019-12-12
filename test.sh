#!/bin/bash
depth=5
regex='*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html'
echo 'https://www.cnn.com/' > urls.txt
count=0
while [ $count -lt $depth ]
do
	let "count++"
	while read f
	do
		echo f > grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0'>>urls.txt
	done < urls.txt
done
sort urls.txt | uniq -u > sorted.txt

while read a
do
	python3 Main.py $a
done < sorted.txt
