# -*- coding: utf-8 -*-

import math

def zeroPad(numberString, zeros, left = True):
    """Return the string with zeros added to the left or right."""

    for i in range(zeros):
        if left:
            numberString = '0' + numberString
        else:
            numberString = numberString + '0'
    return numberString

def RecursiveMultiplication(A, B):
    """ Function to compute multiplication using divide and conquer algorithm """

    A = str(A)
    B = str(B)
    
    if len(A) == 1 and len(B) == 1:
        return int(A) * int(B)
    if len(A) < len(B):
        A = zeroPad(A, len(B) - len(A))
    elif len(B) < len(A):
        B = zeroPad(B, len(A) - len(B))

    max_len = max(len(A), len(B))

    split_position = math.ceil(max_len/2)

    #Split numbers in high and low order of digits for both the numbers
    A1 = (A[:-split_position]) 
    A2 = (A[-split_position:])
    B1 = (B[:-split_position])
    B2 = (B[-split_position:])
    
    f.write("\n--------------------------------")
    f.write("\nIntermediate Values of A1, B1 after partition:")
    f.write("\n--------------------------------")
    f.write("\nA : "+ A + "  A1 : "+ A1 + " A2 : " + A2) # A:223245 A1: 223 A2: 245
    f.write("\nB : "+ B + "  B1 : "+ B1 + " B2 : " + B2) # B:123456 B1: 123 B2: 456
    
    #Steps for sub quadratic calculation with 3 multiplications
    A1_B1 = RecursiveMultiplication(A1, B1)
    A2_B2 = RecursiveMultiplication(A2, B2)

    P = RecursiveMultiplication(int(A1) + int(A2), int(B1) + int(B2))

    return (A1_B1*10**(2*split_position)) + ((P - A1_B1 - A2_B2)*10**(split_position)) + A2_B2

if __name__ == '__main__':
    filename = 'inputPS2.txt'
    x, y = "", ""
    outfile = 'outputPS2.txt'
    f = open(outfile, 'w')

    with open (filename, 'r') as infile:
       for line in infile:
           if line.startswith("1st"):
               idx = line.find(":")
               if idx != -1:
                   # First Number is present
                   x = (line[idx+1:]).strip()
                   if  not x.isdigit():
                       f.write("\nNot a valid number")
                       x = ""
           if line.startswith("2nd"):
               idx = line.find(":")
               if idx != -1:
                   # Second Number is present
                   y = (line[idx+1:]).strip()
                   if  not y.isdigit():
                       f.write("\nNot a valid number")
                       y = ""
    if len(x) > 1 and len(y) > 1:
        f.write("--------------------------------")
        f.write("\nResult: > " + x + "  x " + y + "  = " + str(RecursiveMultiplication(x, y)))
        f.write("\n--------------------------------")
        f.write("\n x*y  directly " + str(int(x) * int(y)))
    else:
        f.write("\nEither x or y is invalid")
    f.close()