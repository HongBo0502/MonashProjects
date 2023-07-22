"""
Name: Kang Hong Bo
Student ID: 32684673

Quetion 1 Assignment 1 FIT3155

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
            while cur_ptr>=0 and the_pattern_ptr>=0 and the_str[cur_ptr]==the_str[the_pattern_ptr]:
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
                while cur_ptr>=0 and the_pattern_ptr>=0 and the_str[cur_ptr]==the_str[the_pattern_ptr]:
                    cur_ptr-=1
                    the_pattern_ptr-=1
                    z+=1
                z_suffix_arr[cur_index]=z_suffix_arr[k]+z
                if z>0:
                    left=cur_index+1
                    right=cur_index
        cur_index-=1
    

    return z_suffix_arr
 
def transposition_z(the_suffix_z_arr,the_str,pattern):
    """
    An algorithm having a time complexity of O(n) to find the transposition of the pattern in the string
    Input: the reverse z array, the string and the pattern
    Output: A string value with the total found matches and the index of the matches with the index of the transposition if there is any
    Time Complexity: O(2n)
    Space Complexity: O(n)
    """
    #initialise the z array 
    len_pattern=len(pattern)
    TheZArray = [0]*(len_pattern+1) + the_suffix_z_arr
    # print(TheZArray)
    # print(len(TheZArray))
    the_res=""

    #initialise the box
    left,right = 0,0

    #loop through the string
    i=0
    the_total=0
    while i<len(the_str)-len_pattern+1:  
        if i == 0:
            TheZArray[i] = len(the_str)
            
        if i<right:
            mirror_ptr = i-left
            remaining = right-i
            if TheZArray[mirror_ptr] < remaining:
                TheZArray[i] = TheZArray[mirror_ptr]
            elif TheZArray[mirror_ptr] > remaining:
                TheZArray[i] = remaining
            elif TheZArray[mirror_ptr] == remaining:
                ptr = i
                count = TheZArray[mirror_ptr]
                while ptr<len(the_str) and the_str[ptr] == the_str[count]:
                    ptr+=1
                    count+=1
                if count>0:
                    left=i
                    right=i+count
                    TheZArray[i]=count
        elif i>right:
            ptr = i
            count = 0
            while ptr<len(the_str) and the_str[ptr] == the_str[count]:
                ptr+=1
                count+=1
            TheZArray[i]=count
        # print(TheZArray)
        
        if i>len_pattern:
            # print(i,len_pattern)
            if TheZArray[i] == len_pattern :
                the_res+=str(i-len_pattern)+"\n"
                the_total+=1
                # print(i-len_pattern)
                
            else:
                if TheZArray[i] +TheZArray[i+len_pattern-1]==len_pattern-2:
                    # print(i-len_pattern,[the_str[i+TheZArray[i]+1],pattern[TheZArray[i]]],[the_str[i+TheZArray[i]],pattern[TheZArray[i]+1]])
                    if the_str[i+TheZArray[i]+1]==pattern[TheZArray[i]] and the_str[i+TheZArray[i]]==pattern[TheZArray[i]+1]:
                        the_res+=(str(i-len_pattern)+" "+str(i+TheZArray[i]-len_pattern)+"\n")
                        the_total+=1
                        # print(i-len_pattern,i+TheZArray[i]-len_pattern)
                    
        i+=1
    # print(TheZArray)
    return str(the_total)+"\n"+the_res

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
    outputFile = open("output_q1.txt","w")
    outputFile.write(result)
    outputFile.close()

# print(z_suffix_algorithm("babbababaabbaba$abba"))
# print(transposition_z(z_suffix_algorithm("babbababaabbaba$abba"),"abba$babbababaabbaba",'abba'))
import sys
if __name__ == '__main__':
    _,textfile,patfile = sys.argv
    txt,pat = readInput(textfile,patfile)
    the_str_for_z = pat+"$"+txt
    the_str_for_suffix = txt+"$"+pat
    
    
    result = transposition_z(z_suffix_algorithm(the_str_for_suffix),the_str_for_z,pat)
    writeOutput(result)



