#!/usr/bin/env python
import sys

try:
    first_name = sys.argv[1]
except Exception as e:
    print("firstname was not passed -- defaulting to Alexa")
    first_name = "Alexa"

try:   
    last_name = sys.argv[2]
except Exception as e:
    print("lastname was not passed -- defaulting to Amazon")
    last_name = "Amazon"

try:
    location = sys.argv[3]
except Exception as e:
    print("location was not pased - defaulting to Seatlle")
    location = "seattle"

'''
print (f"ARG-1 - {sys.argv[1]}")
print (f"ARG-2 - {sys.argv[2]}")
print (f"ARG-3 - {sys.argv[3]}")
'''

print(f"\n\nhello {first_name} good morning, \n welcom Mr. {last_name}, how's weather in {location}\n\n")