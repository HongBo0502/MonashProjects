"""
Name Kang Hong Bo
Student ID: 32684673

"""

def pow_mod(base:int,power:int,mod:int):
    temp_p=power
    length=power.bit_length()
    rep_lst=[None]*length
    rep_lst[0]=base%mod
    result=1
    if(temp_p&1)==1:
        result=(result*rep_lst[0])%mod
    temp_p>>=1
    for i in range(1,length):
        rep_lst[i]=(rep_lst[i-1]*rep_lst[i-1])%mod
        if(temp_p&1)==1:
            result=(result*rep_lst[i])%mod
        temp_p>>=1
    return result
import random
def miller_rabin(num,iterations):
    if num%2==0:
        return False
    s=0
    d=num-1
    while d%2==0:
        s+=1
        d//=2
    # print(s,d)
    for _ in range(iterations):
        
        a=random.randint(2,num-2)
        x=[None]*(s+1)
        x[0]=pow_mod(a,d,num)
        for i in range (1,s+1) :
            x[i]=(x[i-1]*x[i-1])%num
            if x[i]==1 and x[i-1]!=1 and x[i-1]!=-1 and x[i-1]!=num-1:
                return False
        if pow_mod(a,num-1,num)!=1:
            return False
        
    return True
def gcd(a,b):
    if a>b:
        l_num=a
        s_num=b
    else:
        l_num=b
        s_num=a
    while s_num!=0:
        l_num,s_num=s_num,l_num%s_num
    return l_num
def write_pq(p,q):
    text_file=open("secretprimes.txt","w")
    text_file.write("# p\n"+str(p)+"\n# q\n"+str(q))
    text_file.close()

import sys,math, time
if __name__ =='__main__':
    _,d=sys.argv
    d=int(d)
    a=None
    b=None
    num=(2**d)
    count=0
    
    while a==None or b==None  :
        # print(num)
        iterations=int(math.log(num-1))
        # print(iterations)
        if miller_rabin(num-1,iterations):
            if a is None:
                a=num-1
                
            else:
                b=num-1
        num<<=1
        count+=1
    write_pq(a,b)
    lam=((a-1)*(b-1)//gcd(a-1,b-1))
    e=random.randint(3,lam-1)
    while gcd(e,lam)!=1:
        e=random.randint(3,lam-1)
    text_file=open("publickeyinfo.txt","w")
    text_file.write("# modulos (n)\n"+str(a*b)+"\n# public exponent (e)\n"+str(e))
    text_file.close()
    
# d=10
# a=None
# b=None
# while a==None or b==None and d <=2000:
#     num=2**d-1
#     iterations=int(1/(1/math.log(num))+1)
#     if miller_rabin(num,iterations):
#         if a is None:
#             a=num
#         else:
#             b=num
#     d+=1
# print(a,b,d)
