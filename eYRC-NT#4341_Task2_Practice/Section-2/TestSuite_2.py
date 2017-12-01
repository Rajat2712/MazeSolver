import os
import numpy as np
import cv2
import hashlib
import time
from section2 import *
start_time = time.time()

def parseData(data):
    a = data.split("\n")
    a.pop()
    output_final = []
    for i in range(len(a)):
        b = a[i].split("]")
        b.pop(); b.pop();
        output = []
        for j in range(len(b)):
            c = b[j].split(",")
            if j != 0:
                c = c[1:]
            num = []
            for k in range(len(c)):
                d = c[k]
                temp = ""
                for x in d:
                    if (ord(x) >= 48 and ord(x) <= 57):
                        temp = temp + x
                num.append(int(temp))
            n_stack = []
            for t in range(len(num)/2):
                n_stack.append((num[2*t],num[2*t+1]))
            output.append(n_stack)
        output_final.append(output)
    return output_final
    
if __name__ == "__main__":
    fo = open("section2.txt","rb")
    string = fo.read()
    array_1 = parseData(string)
    array_2 = []
    for m in range(10):
        array_2.append(main("image_0" + str(m) + ".jpg"))
    flag = 0
    print "================================================="
    for m in range(10):
        try:
            print "Testing solution for image_0" + str(m) + ".jpg"
            assert array_1[m] == array_2[m]
            print "Solution passed for image_0" + str(m) + ".jpg\n"
        except AssertionError:
            print "Solution failed for test image image_0" + str(m) + ".jpg\n"
            flag = flag + 1
    print "\n\n"
    if flag == 0:
        print "Script is OK. Way to go !!"
    else:
        print "Script is not OK. Solution passed " + str(10-flag) + " test cases. Try again !!"
    print "================================================="
    print time.time() - start_time
    hasher = hashlib.md5()
    with open('TestSuite_2.py', 'rb') as afile:
         buf = afile.read()
         hasher.update(buf)
    fo = open("hash.txt", "wb")
    fo.write((hasher.hexdigest()))
    fo.write("\t" + str(10-flag))
    fo.close()
