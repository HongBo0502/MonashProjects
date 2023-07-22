"""
Name: Kang Hong Bo
Student ID: 32684673

Assignment 1 FIT3155 Question 2
"""



def z_suffix_algorithm(the_str):
    """
    Uses Z-algoritm to find the z array of the string
    Input: the string
    Output: the reverse z array
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    len_of_the_str=len(the_str)

    #initialise the z array
    z_suffix_arr=[0]*len_of_the_str
    z_suffix_arr[-1]=len_of_the_str

    cur_index=len_of_the_str-2
    #the box
    right=len_of_the_str-1
    left=len_of_the_str-1

    while cur_index>=0:
        #case 1 not in the box
        if cur_index<left:
            the_pattern_ptr=len_of_the_str-1
            
            cur_ptr=cur_index
            z=0
            while cur_ptr>=0 and the_pattern_ptr>=0 and (the_str[cur_ptr]==the_str[the_pattern_ptr] or the_str[cur_ptr]=="." or the_str[the_pattern_ptr]=="."):
                cur_ptr-=1
                the_pattern_ptr-=1
                z+=1
            if z>0:
                z_suffix_arr[cur_index]=z
                left=cur_index
                right=cur_index+z
        #case 2 in the box
        else:
            k=(len_of_the_str-1)-(right-cur_index)
            remaining=cur_index-left+1
            #case 2a: z[k]<remaining    
            if z_suffix_arr[k]<remaining:
                z_suffix_arr[cur_index]=z_suffix_arr[k]
            #case 2b: z[k]>remaining
            elif z_suffix_arr[k]>remaining:
                z_suffix_arr[cur_index]=remaining

            #case 2c: z[k]==remaining
            else:
                the_pattern_ptr=len_of_the_str-1-z_suffix_arr[k]
                cur_ptr=left-1
                z=0
                while cur_ptr>=0 and the_pattern_ptr>=0 and (the_str[cur_ptr]==the_str[the_pattern_ptr] or the_str[cur_ptr]=="." or the_str[the_pattern_ptr]=="."):
                    cur_ptr-=1
                    the_pattern_ptr-=1
                    z+=1
                z_suffix_arr[cur_index]=z_suffix_arr[k]+z
                if z>0:
                    left=cur_index+1
                    right=cur_index
        cur_index-=1
    

    return z_suffix_arr


def bad_char(pat):
    """
    Create a bad character table
    Input: the pattern
    Output: the bad character table and the index of the wildcard
    Time Complexity: O(n) where n is the length of the pattern
    Space Complexity: O(n*j) where n is the length of the pattern and j is the number of special characters
    """
    R=[None]*27
    for i in range(len(pat)):
        if ord(pat[i])-97<0:
            wild=i+1
            continue
        if   (ord(pat[i])-97)>=0  and  R[ord(pat[i])-97]==None:
            R[ord(pat[i])-97]=[0]*len(pat)
        # print(R)
        for j in R:
           
            if j!=None  and j[i]<j[i-1]:
                
                j[i]=j[i-1]
        
        
        if i<len(pat)-1:
            # print(i,R[ord(pat[i])-97])
            R[ord(pat[i])-97][i+1]=i+1
        
            
        # print(R)
    return R,wild


# print(bad_char("axxccfdf"))


def good_suffix(z_suffix):
    """
    Create a good suffix table
    Input: the z array of the pattern
    Output: the good suffix table
    Time Complexity: O(n) where n is the length of the pattern
    Space Complexity: O(n) where n is the length of the pattern
    """
    len_pat=len(z_suffix)
    GS=[0]*(len_pat+1)
    for i in range (1,len_pat-1):
        val=len_pat-z_suffix[i]
        
        GS[val]=i+1
    return GS
# print(z_suffix_algorithm("acababacaba"))
# print(good_suffix(z_suffix_algorithm("acababacaba")))


def matched_prefix(z_suffix):
    """
    Create a matched prefix table
    Input: the z array of the pattern
    Output: the matched prefix table
    Time Complexity: O(n) where n is the length of the pattern
    Space Complexity: O(n) where n is the length of the pattern
    """
    len_pat=len(z_suffix)
    mp=[0]*(len_pat+1)
    
    for i in range(0,len_pat):
        
        j=len_pat-i-1
        z=z_suffix[i]

        if i-z == -1 and z >mp[j+1]:
            mp[j] = z
        else:
            mp[j] = mp[j+1]
    return mp



def boyer_morre_wild(text,pat):
    """
    A function that implements the Boyer-Morre algorithm with a wildcard in pattern
    Input: the text and the pattern
    Output: the index every match is found
    Time Complexity: O(n/m) where n is the length of the text and m is the length of the pattern
    Space Complexity: O(n + m*j +m + m) where n is the length of the text, m is the length of the pattern and j is the number of special characters     
    """
    P=len(pat)
    T=len(text)

    match_index=""
    
    if P==0 or T==0 or P>T:
        return match_index
    

    z_suffix=z_suffix_algorithm(pat)
    BCS,wild_card=bad_char(pat)
    GSS=good_suffix(z_suffix)
    MPS=matched_prefix(z_suffix)

    i=0
    stop= -1
    resume=-1
    count=0
    while i< T-P+1:
        # print(i)
        j=P-1
        matched=False
        avail_w=1
        while j>=0:
            # print(j)
            if j==stop:
                j=resume
                stop, resume = -1, -1


            if j == 0 and (text[i+j] == pat[j] or pat[j]=='.') :
                # print("matched")
                matched=True
                break
            elif pat[j]=='.':
                if avail_w==0:
                    stop, resume = -1, -1
                    break
                else:
                    avail_w-=1
                    j-=1
            elif text[i+j] == pat[j]:
                j-=1
            else:
                stop, resume = -1, -1
                break

        shift=1

        if matched:
            # print("matched")
            match_index+=str(i+1)+"\n"
            
            shift=P - MPS[1]
            stop=MPS[1]-i-1
            resume=0
        else:
            if BCS[ord(text[i+j])-97]!=None and avail_w>0:
                # print("here")
                # print(BCS[ord(text[i+j])-97][j],wild_card)
                check_wild=max(BCS[ord(text[i+j])-97][j],wild_card)
                shift=max(P-GSS[j+1],j-check_wild+1)
                stop = shift -1
                resume=stop-(P-j-1)
                # print(stop,resume)
            elif BCS[ord(text[i+j])-97]==None and avail_w>0:
                # print("here1")
                # print(wild_card)
                shift=j-wild_card+1
                stop = shift -1
                resume=stop
                # print(stop,resume)
                

            elif  BCS[ord(text[i+j])-97]!=None and avail_w==0:
                # print("here2")
                shift=max(P-GSS[j+1],P-BCS[ord(text[i+j])-97][j])
        
                stop=shift-1
                resume=stop-(P-j-1)
                
                
            else:
                # print("here3")
                # print(avail_w)
                mp=P-MPS[j+1]
                if avail_w>0:
                    if mp>shift :
                        shift=mp
                        stop=MPS[j+1]-1
                        resume=0
                else:
                    if mp>shift:
                        shift=mp
                        stop=-1
                        resume=-1
                # print(stop,resume)
        # print("before",i,"shift",shift)
        i+=shift
        # print(i,stop,resume,"\n")
    return match_index

def readInput(textfile,patfile):
    """
    A function to read the input from the text file
    Input: The text file and the pattern file
    Output: The text and the pattern
    """
    textFile=open(textfile,"r")
    txt=textFile.read()

    patFile=open(patfile,"r")
    pat=patFile.read()

    textFile.close()
    patFile.close()

    return txt,pat

def writeOutput(result):
    """
    A function to write the output to the output file
    Input: The result string
    Output: None
    
    """
    outputFile = open("output_q2.txt","w")
    outputFile.write(result)
    outputFile.close()

import sys
if __name__ == '__main__':
    _,textfile,patfile = sys.argv
    txt,pat = readInput(textfile,patfile)
    
    
    result = boyer_morre_wild(txt,pat)
    writeOutput(result)




