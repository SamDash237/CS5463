#!/usr/bin/python
#Homework 1
#Sam Dash
#eeo072
#CS 5463
#May 28 2020
#Run with: python ./hw1.py

def signed(val):
    return -(val & 0x80000000) ^ (val & 0x7fffffff)

hexDigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
hexDigitsNve = ["0x8000000" + i for i in hexDigits]
hexDigits8 = ["0xFFFFFF8" + i for i in hexDigits]
hexDigits9 = ["0xFFFFFF9" + i for i in hexDigits]
hexDigitsA = ["0xFFFFFFA" + i for i in hexDigits]
hexDigitsB = ["0xFFFFFFB" + i for i in hexDigits]
hexDigitsC = ["0xFFFFFFC" + i for i in hexDigits]
hexDigitsD = ["0xFFFFFFD" + i for i in hexDigits]
hexDigitsE = ["0xFFFFFFE" + i for i in hexDigits]
hexDigitsF = ["0xFFFFFFF" + i for i in hexDigits]
hexDigits0 = ["0x0000000" + i for i in hexDigits]
hexDigits1 = ["0x0000001" + i for i in hexDigits]
hexDigits2 = ["0x0000002" + i for i in hexDigits]
hexDigits3 = ["0x0000003" + i for i in hexDigits]
hexDigits4 = ["0x0000004" + i for i in hexDigits]
hexDigits5 = ["0x0000005" + i for i in hexDigits]
hexDigits6 = ["0x0000006" + i for i in hexDigits]
hexDigits7 = ["0x0000007" + i for i in hexDigits]
hexDigitsPve = ["0x7FFFFFF" + i for i in hexDigits]
hexVal = hexDigitsNve + hexDigits8 + hexDigits9 + hexDigitsA + hexDigitsB + hexDigitsC + hexDigitsD + hexDigitsE + hexDigitsF +hexDigits0 + hexDigits1 + hexDigits2 + hexDigits3 + hexDigits4 + hexDigits5 + hexDigits6  + hexDigits7 + hexDigitsPve

for i in hexVal:
  print(hexVal, signed(int(str(hexVal), 16)))