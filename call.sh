#!/bin/bash
curl https://www.cnn.com/ | grep -Eo '*\/[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[a-z/-]+.html' | awk '$0="https://www.cnn.com"$0' | xargs -n1 python3 Main.py
