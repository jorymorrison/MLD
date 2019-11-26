#!/bin/bash
declare -a Array
curl https://www.cnn.com/ | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0' | mapfile -t Array

#curl https://www.cnn.com/ | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0' | xargs -n1 curl | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0' > map file -t Array

#curl https://www.cnn.com/ | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0' | xargs -n1 curl | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0' | xargs curl | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0' > map file -t Array

echo Array | xargs -n1 python3 Main.py

#curl https://www.cnn.com/ | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0' | xargs -n1 python3 Main.py
#curl https://www.cnn.com/ | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0' | xargs -n1 curl | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0' | xargs -n1 python3 Main.py
#curl https://www.cnn.com/ | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0' | xargs -n1 curl | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0' | xargs curl | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0' | xargs -n1 -n1 python3 Main.py
