"""
Name : Kang Hong Bo
Student Id : 32684673
"""

def char_idx(ch: str):
    # ord(ch) - ord(' ') + 1 to accommodate '$' as termination char
    if ch == "$":
        return 0
    return ord(ch) - 31

class GlobalEnd:
    """
    The global end objects used for rapid leaf extension trick
    """
    def __init__(self):
        self.value = -1

    def increment(self):
        self.value += 1
    def __str__(self):
        return str(self.value)
class Node:
    def __init__(self, start=None, end=None, suffix_link=None, is_root=False, is_leaf=False):
        self.start = start
        self.end = end
        self.is_root = is_root
        self.is_leaf = is_leaf
        self.children = [None] * 128
        self.suffix_link = suffix_link
        self.suffix_id = None
    def get_edge(self, index):
        return self.children[index]

    def add_edge(self, index, node):
        self.children[index] = node

    def add_suffix(self, extension):
        self.suffix_id=extension
    def update_start(self, start):
        self.start = start
    def get_start(self):
        return self.start
    
    def get_end(self):
        # If ending node is leaf, return global end value
        if self.is_leaf:
            return self.end.value

        # Otherwise, just return self.end
        else:
            return self.end
    def  __str__(self):
        return f"({self.start},{self.end},{self.suffix_id},{self.is_leaf},{self.is_root})"
class SuffixTree:

    def __init__(self):
        self.root = Node(is_root=True)
        self.root.suffix_link=self.root

        self.active_node = self.root
        self.active_length = 0
    

    def traverse(self, txt, end):
        """
        Reffered from tutorial
        Traversal function using skip count trick
        - active node and length will be updated until last visited internal node where active_length > 0
        - returns node last discovered (node just after last visited edge)
        """

        def traverse_aux(current_node, current_length):
            """
            Steps
            1. Make sure current node is not a leaf and current length > 0 
               If not, stop here

            2. Update active node and active length

            3. Get current edge (at index corresponding to first character of remaining in node's chidren)
               if it doesn't exist, stop here

            4. Get edge's length
               If edge's length is longer than current length, stop here

            5. Update current node (next node) and current length (-= edge length) and go to step 1                
            """

            # If is leaf or current length is 0, end
            if current_node.is_leaf :
                return current_node

            # Else is internal node, update active node and length
            self.active_node = current_node
            self.active_length = current_length
            
            # Get active edge
            index = ord(txt[end - current_length])                  # Index corresponding to first character of remaining
            edge = current_node.get_edge(index)                     # edge should be at that index in current node's child array
            # If no active edge, end
            if edge is None: 
                return current_node

            # Else get active edge length
            edge_length = edge.get_end() - edge.get_start()  +1

            # If edge length > current_length, end
            if edge_length > current_length:
                return current_node

            # Else skip count down
            return traverse_aux(edge, current_length - edge_length)
        
        return traverse_aux(self.active_node, self.active_length)
    def ukkonen(self,txt):
        # Initialize variables
        phase = 0                         # represents phase
        extension = 0                         # represents extension 
        global_end = GlobalEnd()             # global end variable

        while phase <len(txt):
            global_end.increment()           # increment global end
            previous_node = None             # previous node
            #extension
            
            while extension <= phase:
                if self.active_node==self.root:
                    self.active_length=phase -extension
                self.traverse(txt,phase)
                
            
                index=ord(txt[phase-self.active_length])
                edge=self.active_node.get_edge(index)

                    
                #rule 1 add new edge
                if edge is None:
                    new_node=Node(start=global_end.value-self.active_length,end=global_end, is_leaf=True)
                    new_node.add_suffix(extension)
                    self.active_node.add_edge(index,new_node)
                
                #rule 2: split edge
                
                elif txt[edge.get_start() + self.active_length] != txt[phase]:
                    
                    new_node=Node(start=edge.get_start(),end=edge.get_start()+self.active_length-1)
                    n_n1=Node(start=global_end.value,end=global_end,is_leaf=True)
                    n_n1.add_suffix(extension)
                    pre_val=edge.get_start()
                    if edge.is_leaf:
                        n_n2=Node(start=edge.get_start()+self.active_length,end=global_end,is_leaf=edge.is_leaf)
                        n_n2.add_suffix(edge.suffix_id)
                    else:
                        edge.update_start(edge.get_start()+self.active_length)
                        n_n2=edge
                    


                    new_node.add_edge(ord(txt[pre_val+self.active_length]),n_n2)
                    new_node.add_edge(ord(txt[global_end.value]),n_n1)
                    new_node.suffix_link=self.root
                    self.active_node.add_edge(index,new_node)
                    if previous_node is not None:
                        previous_node.suffix_link=new_node
                    previous_node=new_node
                    # update active node and length
                    self.active_node=new_node.suffix_link
                    self.active_length=self.active_length-1
                
                #rule 3 : Do nothing
                else:
                    pass

                extension+=1
                self.active_node=self.active_node.suffix_link

            self.active_length+=1
            phase+=1
            extension=0
            
    def inorder(self,node):
        """
        Reffered from tutorial
        Performs inorder traversal from node
        Returns the payload containging (text_id, extension) tuples of all leaf nodes

        Note
        - Given that each node's children is implemented with an array, inorder traversal is inefficient if GST is sparse.
        - If each node's children was implemented with a list instead, inorder traversal would be efficient.
        - However, O(1) random access is more important for the whole project, so I had to make do with the inefficiency.
        """
        res = []
        def inorder_aux(node):
            # Node is leaf, return payload
            if node.is_leaf:
                res.append(node.suffix_id)
                

            # Node is not leaf, perform inorder traversal
            else:
                for e in node.children:
                    if e is not None:
                        inorder_aux(e)

        inorder_aux(node)

        return res 
    def preprocess(self, txt):
        """
        Inserts text strings in list texts into the GST
        """
        

        # Add terminal character to each text
        txt = txt + '$'
        self.ukkonen(txt)





def num_to_bitsStr(num,elias:bool=False,bit:int=0):
    if elias==True:
        bit_arr = ""
        while num > 1:
            bit_arr = str(num % 2) + bit_arr
            num = num >> 1
        bit_arr = "0"+bit_arr
        return bit_arr
    else:
        bit_arr = ""
        while num > 0:
            bit_arr = str(num % 2) + bit_arr
            num = num >> 1
        if bit>0:
            while len(bit_arr)<bit:
                bit_arr="0"+bit_arr
        return bit_arr
def runlength(bwtstring):
    rl_string=[]
    
    for i in range (len(bwtstring)):
        
        if i==0:
            temp=(bwtstring[i],1)
        else:
            if bwtstring[i]==temp[0]:
                temp=(temp[0],temp[1]+1)
            else:
                rl_string.append(temp)
                temp=(bwtstring[i],1)
    rl_string.append(temp)
    return rl_string

def elias(num):
    """
    elias encoder
    """

    # convert number into bits
    bit_arr = num_to_bitsStr(num)
    
    # get length of string and decrement by 1 for elias
    length = len(bit_arr) - 1

    # loop until the length is 0
    while length > 0:
        tmp_bit_array = num_to_bitsStr(length,True)   # convert value to reversed bit array
        length = len(tmp_bit_array)-1             # update next length component
        bit_arr = tmp_bit_array +bit_arr                   # append bit value to output
                                 
    return bit_arr
import heapq
def Huffman(s):
    fr_table=[None]*90
    unq_char=[]
    # loop for each char of string
    for char in s:

        # if this char wasnt present in frequency table then set its frequency to 1 at position freq_table[ord(char)]
        if fr_table[ord(char)-37] is None:
            fr_table[ord(char)-37] = 1
            unq_char.append(char)

        # increment the frequency of the char at position freq_table[ord(char)]
        else:
            fr_table[ord(char)-37] += 1
    # creating the heap array
    freq_table_for_heap = []
    # loop for the number of distinct chars in string
    for index in range(len(unq_char)):

        # get the distinct char
        char = unq_char[index]

        # get frequency of the char
        freq = fr_table[ord(char)-37]
        
        # heap table will contain the following (length of char + frequency of char, frequency of char, char)for each distinct char
        freq_table_for_heap.append((freq+1, freq, char))
        # heapify the char according to the key which is length of char + frequency of char
    heapq.heapify(freq_table_for_heap)
    # set the frequency none so it can be use for codeword for each distinct char
    n_fr_table = [None] * 89

    # this will loop until we merge all the strings into one
    while len(freq_table_for_heap) > 1:

        # pop the smallest element in the heap according to key
        item1 = heapq.heappop(freq_table_for_heap)

        # pop the smallest element in the heap according to key
        item2 = heapq.heappop(freq_table_for_heap)
        # accumulate the frequency+length of both strings getting combined
        total_sum = item1[0] + item2[0]
        # append both strings together
        new_str = item1[2] + item2[2]
        # push this new element in the heap
        heapq.heappush(freq_table_for_heap, (total_sum, total_sum-len(new_str), new_str))

        # the first pop string chars codeword will have 0 appended to it
        for char in item1[2]:
            if n_fr_table[ord(char)-37] is None:
                n_fr_table[ord(char)-37] = ""
            n_fr_table[ord(char)-37]="0"+n_fr_table[ord(char)-37]

        # the second pop string chars codeword will have 1 appended to it
        for char in item2[2]:
            if n_fr_table[ord(char)-37] is None:
                n_fr_table[ord(char)-37] = ""
            n_fr_table[ord(char)-37]="1"+n_fr_table[ord(char)-37]

    # if we only have 1 distinct char then we will only have one element in our heap
    if len(unq_char) == 1:
        n_fr_table[ord(unq_char[0])-37] = ""
        n_fr_table[ord(unq_char[0])-37]+= "0"

    # we will reverse the codeword for each distinct char as we stored codeword in reverse order for each distinct char
    

    return unq_char, fr_table ,n_fr_table
def check_bit_str(bitfile, mybitstring,last : bool = False):
    if last:
        mybitstring = mybitstring + "0" * (8 - len(mybitstring))
    while len(mybitstring) >= 8:
        # Extract the first 8 bits from the bit string
        mybitstring_towrite = mybitstring[:8]
        
        # Remove the first 8 bits from the bit string
        mybitstring = mybitstring[8:]
        
        # Convert the 8-bit substring to an integer
        mynumber = int(mybitstring_towrite, 2)
        
        # Write the integer to the binary file as a single byte
        bitfile.write(mynumber.to_bytes(1, byteorder='big'))
    return mybitstring

def encode(s):
    mybinfile=open("bwtencoded.bin","wb")
    T=SuffixTree()
    T.ukkonen(s)
    suff_arr=T.inorder(T.root)
    bwt=""
    for i in suff_arr:
        bwt+=s[i-1]
    res=""
    res+=elias(len(bwt))
    res=check_bit_str(mybinfile,res)
    check,freq,code=Huffman(bwt)
    count=len(check)
    res+=elias(count)
    res=check_bit_str(mybinfile,res)
    rl_encoded=runlength(bwt)

    unq=[]
    for i in range (len(freq)-1):
        if freq[i] is not None:
            unq.append(chr(i+37))
    if freq[-1] is not None:
        unq.append("$")
    for alpha in unq:
        res+=num_to_bitsStr(ord(alpha),None,7)
        res+=elias(len(code[ord(alpha)-37]))
        
        res+=code[ord(alpha)-37]
        res=check_bit_str(mybinfile,res)
    for rl in rl_encoded:
        res+=code[ord(rl[0])-37]
        res+=elias(rl[1])
        res=check_bit_str(mybinfile,res)
    res=check_bit_str(mybinfile,res,True)
    
    mybinfile.close()
    return res
def read_input(textfile):
    textFile=open(textfile,"r")
    txt=textFile.read()
    textFile.close()
    return txt

import sys
if __name__ == '__main__':
    _,textfile=sys.argv
    txt=read_input(textfile)
    txt+="$"
    encode(txt)

