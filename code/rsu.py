# -*- coding: UTF-8 -*-
from PIL import Image
import numpy
from operator import mod


def RSU(fig):
    x = fig.size[0]
    y = fig.size[1]
    bufsize = x*y
    blocknum = 0
    blockcol = 2
    blockrow = 2
    blocksize = 4
    R = 0
    S = 0
    U = 0
    R1 = 0
    S1 = 0
    U1 = 0
    
    s = bufsize/blocksize
     
    tmp = [[[0 for i in range(2)]for j in range(2)]for k in range(s)]
     
    for i in range(0,x/blockrow):
        for j in range(0,y/blockcol):
             
            tmp[blocknum][0][0] = fig.getpixel((blockrow*i,blockcol*j))
  
            tmp[blocknum][0][1] = fig.getpixel((blockrow*i,blockcol*j+1))
  
            tmp[blocknum][1][0] = fig.getpixel((blockrow*i+1,blockcol*j))
  
            tmp[blocknum][1][1] = fig.getpixel((blockrow*i+1,blockcol*j+1))
 
            blocknum = blocknum+1

    for n in range(0,bufsize/blocksize):
        x = numpy.zeros(blocksize)
        g = numpy.zeros(blocksize)
        h = numpy.zeros(blocksize)
        m = 0
# ..........................................求fG  
        for i in range(0,blockrow):
            for j in range(0,blockcol):
                x[m] = tmp[n][i][j]
                m = m + 1
        sum1 = 0
        for i in range(0,3):
            sum1 = sum1 + abs(x[i+1]-x[i])
        fG = sum1
#............................................求FsG  
        M = [0,1,1,0]
        for i in range(0,blocksize):
            if M[i] == 0:
                g[i] = x[i]
            else:
                if mod(x[i],2) == 0:
                    g[i] = x[i] + 1
                else:
                    g[i] = x[i] - 1
        sum2 = 0
        for i in range(0,3):
            sum2 = sum2 + abs(g[i+1]-g[i])
        FsG = sum2
#..........................................求距离
        if FsG > fG:
            R = R + 1
        elif FsG < fG:
            S = S + 1
        else:
            U = U + 1
#.......................................... 求FsH
        M = [0,-1,-1,0]
        for i in range(0,blocksize):
            if M[i] == 0:
                h[i] = x[i]
            else:
                if mod(x[i],2) == 0:
                    h[i] = x[i] - 1
                else:
                    h[i] = x[i] + 1
                  
        sum3 = 0
        for i in range(0,3):
            sum3 = sum3 + abs(h[i+1]-h[i])
        FsH = sum3
#..............................求距离
        if FsH > fG:
            R1 =R1 + 1
        elif FsH < fG:
            S1 = S1 + 1
        else:
            U1 = U1 + 1   
                        
    res = [R,S,U,R1,S1,U1]
    return res