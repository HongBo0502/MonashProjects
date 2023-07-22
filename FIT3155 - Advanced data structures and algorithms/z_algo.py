
def zalgorithm(string):
    #initialize zarray to return
    return_zarray= [0]* len(string) #O(N) Space
    
    # initialize the zbox (left and right)
    #z_box right is exclusive
    l, r = 0,0


    # loop through string
    i=0
    while i<len(string):
        # print(i)
        if i==0:
            return_zarray[i]=len(string)
        
        if i<r:

            # k is the i mirror in the left box
            k= i-l
            # remaining gap between right box and i
            remaining = r-i
            # print(i,k,remaining)
            # the three case is imoprtant
            if return_zarray[k] < remaining:
                # print("case2a")
                return_zarray[i]=return_zarray[k]
            elif return_zarray[k]>remaining:
                # print("case2b")
                return_zarray[i]=remaining
            elif return_zarray[k]==remaining:
                # print("case2c")
            
                #explicit
                ptr=i
                count=return_zarray[k]
                # print(ptr)
                while ptr<len(string) and string[ptr]==string[count]:
                    ptr+=1
                    count+=1
                if count>0:
                    l=i
                    r=i+count
                    return_zarray[i]=count
                # print(count)
        elif i>r:
            #explicit
            ptr=i
            count=0
            while ptr<len(string) and string[ptr]==string[count]:
                ptr+=1
                count+=1
            return_zarray[i]=count

        i+=1
        
    return return_zarray

def z_suffix_algorithm(pattern):
    """
    Returns a reversed Z-array (substring matches suffix)
    """
    M = len(pattern)

    # Initializing Z array
    z_array = [0] * (M)
    z_array[-1] = M                             # Z[-1] = length of string
    
    #Initialize variables
    i = M-2                                     # current index
    r = M-1                                     # first index inside Z-box
    l = M-1                                     # last index inside Z-box

    # Loop through string
    while i >= 0:
        # Case 1: i is outside Z box
        if i < l:
            # compare outside box
            x = M-1                              # pointer at the suffix
            j = i                               # pointer at the current substring
            z = 0                               # z-value
            while x >= 0 and j >= 0 and pattern[x] == pattern[j]:
                x -= 1
                j -= 1
                z += 1

            # Update variables if there are matches
            if z > 0:
                z_array[i] = z
                l = j+1
                r = i

        # Case 2: i is inside Z box
        else:
            k = (M-1)-(r-i)                 # index of character corresponding to i in matching suffix
            remaining = i-l+1               # size of remaining (i to end of z-box)
            # Case 2a: Z[k] < remaining
            if z_array[k] < remaining:
                z_array[i] = z_array[k]
            
            # Case 2b: Z[k] > remaining
            elif z_array[k] > remaining:
                z_array[i] = remaining

            # Case 2c: Z[k] == remaining
            else:
                # Compare outside box
                x = M-1-z_array[k]           # pointer outside suffix
                j = l-1                        # pointer outside Z-box of current substring
                z = 0                            # additional z-value
                while x >= 0 and j >= 0 and pattern[x] == pattern[j]:
                    x -= 1
                    j -= 1
                    z += 1

                z_array[i] = z_array[k] + z
                # If has matches outside
                if z > 0:
                    l = j+1 #z
                    r = i  #z

        # Decrement
        i -= 1

    return z_array
def explcit_comparison():
    #compare
    pass
# print(zalgorithm("aabcaabx"))
# print(zalgorithm("aaaabaaae"))
# print(zalgorithm("aabcaabxaabcaabc"))
# print(zalgorithm("abba$babbababaabbaba"))
# print(zalgorithm("abba$ababbaabababbab"))
# print(z_suffix_algorithm("ababa"))

# print(zalgorithm("abcdcaa$acbabccdaabcdacabdccaa"))
# print(z_suffix_algorithm("acbabccdaabcdacabdccaa$abcdcaa"))

print(z_suffix_algorithm("ababbaba"))