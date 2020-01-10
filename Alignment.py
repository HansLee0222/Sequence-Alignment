import numpy as np
import sys
#Global variable for match, mismatch, and gaps
match = 2
mismatch = -1
gap = -2
def matchScore(x, y):
    if x == y:

        return match
    else:

        return mismatch
def needlemen(x,y):
    count = 0
    seq1=""
    seq2=""
    num_rows = len(x)
    num_cols = len(y)
    #create an numpy array with corresponding length and width
    data = np.zeros(shape = (num_rows, num_cols), dtype = np.int)
    #fill row with gap penelty
    for i in range(0,num_rows):
        data[i][0] = gap*i
    #fill col with gap penelty
    for j in range(0, num_cols):
        data[0][j] = gap*j
    #calculating matches
    for i in range(1, num_rows):
        for j in range(1, num_cols):
            #Diagonal score for match and mismatches
            Dia = data[i-1][j-1] + matchScore(x[i-1],y[j-1])
            #Gap coming from above
            Up = data[i-1][j] + gap
            #Gap coming from the side
            Side= data[i][j-1] +gap
            #Find maximum score, fill the slot with the returned value
            data[i][j] = max(Dia,Up,Side)
    score = optimalScore(data)



    #row for tracing back
    RT = len(x)-1
    #Colum for tracing back
    CT = len(y)-1
    #The loop ends when we hit either the first row and column
    while RT >=1 and CT>=1:
        #the current score
        curr = data[RT][CT]
        #diagonal score
        Dia = data[RT-1][CT-1]
        #Gap from up
        Up = data[RT-1][CT]
        #Gap from side
        Side = data[RT][CT-1]

        if Dia + matchScore(x[RT-1],y[CT-1]) == (Up + gap) == (Side +gap) or (Up+gap)==(Side+gap) or Dia + matchScore(x[RT-1],y[CT-1]) == (Up + gap) or Dia + matchScore(x[RT-1],y[CT-1]) == (Side + gap):
            count+=1
        #check diagonal
        if curr == Dia + matchScore(x[RT-1],y[CT-1]):
            seq1 += x[RT-1]
            seq2 += y[CT-1]
            RT = RT-1
            CT = CT-1
        #check up
        elif curr == Up + gap:
            seq1 += x[RT-1]
            seq2 += '-'
            RT = RT -1
        #otherwise
        else:
            seq1 = seq1 + '-'
            seq2 = seq2 + y[CT-1]
            CT=CT-1
    #finish the row
    while RT > 0:
        seq1 += x[RT-1]
        seq2 += '-'
        RT -= 1
    #finish the colum
    while CT > 0:
        seq1 += '-'
        seq2 += seq2[CT-1]
        CT -= 1
    #reverse the output because it was done in the opssite way
    seq1 = seq1[::-1]
    seq2 = seq2[::-1]



    return seq1, seq2, data

def optimalScore(data):
    return np.amax(data)
def main():
    x = input("First Sequence: ")
    y = input("Second Sequence: ")

    a,b,g= needlemen(x,y)
    print(a,b,g, sep = '\n')


main()
