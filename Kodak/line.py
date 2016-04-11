from __future__ import division
import random
import matplotlib.pyplot as plt
import numpy

def x_coeff(eqa):
    st=''
    for i in range(0,len(eqa)):
        if eqa[i] == 'x':
            if (i==0):
                return 1
                pass
            else:   
                for i1 in range (0,i):
                    st=st+eqa[i1]
                if (int(st)==0):
                    return 0
                else:
                    return st
    

def y_coeff(eq):
    cof_y=''
    ls=[]
    if(eq[0] != '-'):
        for i in range(0,len(eq)):
              if (eq[i]== '+') or (eq[i] == '-'): 
                  ls.append(i)
              
              if (eq[i]== '='):
                  equal= i
        start = ls[0]    
        end = ls[1]-1
        if (eq[start] == '-'):
            for i in range(start,end):
                cof_y=cof_y+eq[i]        
        else:
            for i in range(start+1,end):
                cof_y=cof_y+eq[i]
        if ((cof_y)== '-'):
            return -1
        else:
            return cof_y
                  
    else:
        for i in range(1,len(eq)):
            if (eq[i]== '+') or (eq[i] == '-'): 
                ls.append(i)
            if (eq[i]== '='):
                equal= i
        start = ls[0]    
        end = ls[1]-1
        if (eq[start] == '-'):
           for i in range(start,end):
               cof_y=cof_y+eq[i]        
        else:
           for i in range(start+1,end):
               cof_y=cof_y+eq[i]
        if ((cof_y)=='-'):
            return -1
        else:
            return cof_y                      
                  
def const(eq):
    con=''
    ls=[]
    for i in range(0,len(eq)):
        if(eq[i] == 'y'):
            strt=i
        if(eq[i] == '='):
            end=i
    if(strt == (end -1)):
        print "No constant part"
        pass
    else:
        if (eq[strt+1] == "+"):
            for i in range(strt+2,end):
                con=con+eq[i]
        elif (eq[strt+1] == '-'):
            for i in range(strt+1,end):
               con=con+eq[i]
        else:
            print "Error"
            exit()
        if (int(con)==0):
            return 0
        else:
            return con                        

def check_cons(a1,b1,c1,a2,b2,c2):
    try:
        a=float(a1/a2)
    except ZeroDivisionError:
        a=0
    try:
         b=float(b1/b2)
    except ZeroDivisionError:
        b=0
    try:
        c=float(c1/c2)
    except ZeroDivisionError:
        c=0
    if (a == b == c):
        return 0
    elif(a != b ):
        return 1
    elif(a == b) and (b != c):
        return 2
    else:
        print "\nError"

def point_gen(a,b,c):
    p1=[]
    p2=[]
    cord=[]
    try:
        m = -(float(a/b))
    except ZeroDivisionError:
        m = 0
    try:
        c = -(float(c/b))
    except ZeroDivisionError:
        c=0
    x = random.randint(-50,50)
    y = (m*x) + (c)
    cord.append(x)
    cord.append(y)
    x = random.randint(-70,70)
    y = (m*x) + (c)
    cord.append(x)
    cord.append(y)
    return cord
    
def intersect_generator(a1,b1,c1,a2,b2,c2):
    try:
        ab1=float(a1/b1)
    except ZeroDivisionError:
        ab1=0
    try:
        ab2=float(a2/b2)
    except ZeroDivisionError:
        ab2=0
    try:
        cb1=float(c1/b1)
    except ZeroDivisionError:
        cb1=0
    try:
        cb2=float(c2/b2)
    except ZeroDivisionError:
        cb2=0
    try:
        x=(cb1-cb2)/(ab2-ab1)
    except:
        x=random.randint(-50,50)
    try:
        m = -(float(a1/b1))
    except ZeroDivisionError:
        m = 0
    try:
        c = -(float(c1/b1))
    except ZeroDivisionError:
        c=0
    y = (m*x) + (c)
    res=[]
    res.append(x)
    res.append(y)
    return res        

if __name__ == '__main__':
    points1=[]
    points2=[]
    print "Enter the equations of line in (  Ax + By + C  = 0) :"
    print "\n****INCASE IF THERE IS NO COEFFICIENT OF X/Y/CONSTANT,PUT THEM 0 (for ex. 1x+1y-23=0)/(0x+0y-21=0)****"
    n_eq=int
    eqa1=str(raw_input("\nEnter Equation 1\n"))
    eqa2=str(raw_input("\nEnter Equation 2\n"))
    A1=float(x_coeff(eqa1))
    B1=float(y_coeff(eqa1))
    C1=float(const(eqa1))
    A2=float(x_coeff(eqa2))
    B2=float(y_coeff(eqa2))
    C2=float(const(eqa2))
    res=check_cons(A1,B1,C1,A2,B2,C2)
    if (res == 0):
        intersect_pt=[]
        print "\nEQUATIONS ARE CONSISTENT WITH INFINITE SOLUTIONS\n"
        intersect_pt=intersect_generator(A1,B1,C1,A2,B2,C2)
        print "\nONE OF THE POINTS OF INTERSECTIONS ARE:"
        print intersect_pt
    elif (res == 1):
        print "EQUATIONS ARE CONSISTENT WITH A UNIQUE SOLUTION"
        intersect_pt=intersect_generator(A1,B1,C1,A2,B2,C2)
        print "\nTHE POINT OF INTERSECTION IS:"
        print intersect_pt
    elif (res == 2):
        print "EQUATIONS ARE INCONSISTENT WITH NO SOLUTION"
    print "\nFOR VISUALISATION LOOK AT THE GRAPH\n"""
    points1=point_gen(A1,B1,C1)
    points2=point_gen(A2,B2,C2)
    x_pts1=numpy.array([points1[0],points1[2]])
    y_pts1=numpy.array([points1[1],points1[3]])
    x_pts2=numpy.array([points2[0],points2[2]])
    y_pts2=numpy.array([points2[1],points2[3]])
    plt.plot(x_pts1,y_pts1)
    plt.plot(x_pts2,y_pts2)
    plt.show()    
      
