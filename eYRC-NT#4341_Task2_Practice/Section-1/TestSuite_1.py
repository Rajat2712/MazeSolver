import os
import numpy as np
import cv2
import hashlib
import time
from section1 import *
start_time = time.time()

def parseData(data):
    a = data.split("\n")
    a.pop()
    output = []
    for m in range(len(a)):
        b =  a[m].split(",")
        num = []
        for k in range(len(b)):
            temp = ""
            for j in b[k]:
                if (ord(j) >= 48 and ord(j) <=57):
                    temp = temp + j
            num.append(int(temp))
        n_stack = []
        for t in range(len(num)/2):
            n_stack.append((num[2*t],num[2*t+1]))
        output.append(n_stack)
    return output



if __name__ == "__main__":
    fo = open("section1.txt", "rb")
    string = fo.read()
    array_1 = parseData(string)   ## from txt file
    string = ""
    for i in range(10):
        string = string + main("image_0" + str(i) + ".jpg")
    array_2 = parseData(string)
    flag = 0
    print "================================================="
    for i in range(10):
        try:
            print "Testing solution for image_0" + str(i) + ".jpg"
            assert array_1[i] == array_2[i], "Output does not match for test case image_0" + str(i) + ".jpg"
            print "Solution passed for image_0" + str(i) + ".jpg\n"
        except AssertionError:
            print "Solution failed for test image image_0" + str(i) + ".jpg\n"
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
    
