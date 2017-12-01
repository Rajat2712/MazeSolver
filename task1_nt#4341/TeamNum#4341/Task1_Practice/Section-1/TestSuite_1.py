import os
import numpy as np
import cv2
import hashlib
import time
from section1 import *
start_time = time.time()

## Function parses data recieved from file.
def parseData(data):
    a = data.split("\n")
    a.pop()
    output = []
    for m in range(len(a)):
        b = a[m].split(",")
        num = []
        for k in range(len(b)):
            for j in b[k]:
                if (ord(j) >= 48 and ord(j) <=57):
                    num.append(int(j))
        n_stack = []
        for k in range(len(num)/2):
            n_stack.append((num[2*k],num[2*k+1]))
        output.append(n_stack)
    return output
    
## Main part of the code.
if __name__ == "__main__":
    fo = open("section1.txt", "rb")                   
    string = fo.read()
    str_isolated = ""
    str_array = []
    for x in string:
        if x != "\t":
            str_isolated = str_isolated + x
        else:
            str_array.append(str_isolated)
            str_isolated = ""
    fo.close()
    array_1 = []         ## Array from txt file
    for x in range(10):
        array_1.append(parseData(str_array[x]))
    string = []
    for i in range(10):
        string.append(main("maze0" + str(i) + ".jpg"))
    array_2 = []         ## Array from user modified file.
    for i in range(10):
        array_2.append(parseData(string[i]))
    flag = 0
    print "================================================="
    for i in range(len(array_1)):
        assert len(array_1[i]) == len(array_2[i]), "Length of subarrays does not match"
    print "Length of sub-arrays is OK"
    for i in range(len(array_1)):
        try:
            print "Testing solution for maze0" + str(i) + ".jpg"
            for j in range(len(array_1[i])):
                temp_1 = array_1[i][j]
                temp_2 = array_2[i][j]
                for k in temp_1:
                    assert k in temp_2
            print "Solution passed for maze0" + str(i) + ".jpg\n"
        except AssertionError:
            print "Solution failed for test image maze0" + str(i) + ".jpg\n"
            flag = flag + 1
    print "\n\n"
    if flag == 0:
        print "Script is OK. Way to go !!"
    else:
        print "Script is not OK. Solution passed " + str(10-flag) + " test cases. Try again !!"
    print "================================================="
    print time.time() - start_time
    hasher = hashlib.md5()
    with open('TestSuite_1.py', 'rb') as afile:
         buf = afile.read()
         hasher.update(buf)
    fo = open("hash.txt", "wb")
    fo.write((hasher.hexdigest()))
    fo.write("\t" + str(10-flag))
    fo.close()
