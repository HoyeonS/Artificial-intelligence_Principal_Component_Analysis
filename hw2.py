import sys
import math

def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X=dict()
    for i in range(26):
        X[chr(i + 65)] = 0
    with open (filename,encoding='utf-8') as f:
        # TODO: add your code here
        for line in f:
            line = line.upper()
            for s in line:
                if(X.get(s) != None):
                    X[s] = X.get(s) + 1
    f.close()

    return X

# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!
ret = shred("letter.txt")
e,s = get_parameter_vectors()
sum = 0
mult = 1
c = 0
eng = math.log(0.6)
sp = math.log(0.4)
print("Q1")
for i in range(26):
    print(chr(i+65) + " " + str(ret[chr(i+65)]))
    eng += math.log(e[i]) * ret[chr(i + 65)]
    sp += math.log(s[i]) * ret[chr(i + 65)]
print("Q2")
print("{:0.4f}".format(ret['A'] * math.log(e[0], math.e)))
print("{:0.4f}".format(round(ret['A'] * math.log(s[0], math.e), 4)))
print("Q3")  
print("{:0.4f}".format(eng))
print("{:0.4f}".format(sp))
print("Q4")
print("{:0.4f}".format(1/(1 + math.pow(math.e, sp - eng))))
