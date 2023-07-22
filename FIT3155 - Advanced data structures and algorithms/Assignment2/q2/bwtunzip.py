"""
Name : Kang Hong Bo
Student Id: 32684673
"""


def bit_to_int(bit_arr):
    val = 0
    for bit in bit_arr:
        val = (val << 1) | int(bit)
    return val
def num_to_bitsStr(num,elias:bool=False,bit:int=0):
    if elias==True:
        bit_arr = ""
        while num > 1:
            # print(num)
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
def runlen_to_string(s):
    res=""
    for _ in range(s[1]):
        res+=s[0]
    return res

def char_idx(ch: str):
    # ord(ch) - ord(' ') + 1 to accommodate '$' as termination char
    if ch == "$":
        return 0
    return ord(ch) - 32
def recover_text_from_BWT(length,F: list[str], L: list[str]):
    """ Recover original string from last column of BWT Matrix
    Args:
        List[str] F: First column of BWT Matrix
        List[str] L: Last column of BWT Matrix

    Returns:
        str: Original string
    """
    n = length
    
    ranks = [None]*95
    freq = [0]*95
    nOccurrences = [0]*n
    for i in range(n):
        # construct rank array to record index of first occurrence of a char in F
        cf = F[i]
        if ranks[char_idx(cf)] is None:
            ranks[char_idx(cf)] = i

        # count number of occurrence of a char in Last column before position i
        cl = L[i]
        # print(cl)
        # print(char_idx(cl))
        # print(freq[char_idx(cl)])
        nOccurrences[i] = freq[char_idx(cl)]      ######## See This Line ########
        
        freq[char_idx(cl)] += 1

    i = 0 # start from first row of matrix
    S = [None] * n # why n*spaces instead of empty string?
    S[n-1] = F[0] # last char of original string is always first char of F column '$'
    S[n-2] =L[0] # second last char is the first char of L column preceeding '$'
    ctr = n-3 # count the remaining char to be reconstructed 
    while ctr >= 0:
        ch = L[i]
        i = ranks[char_idx(ch)] + nOccurrences[i]
        S[ctr] = L[i]  # reconstruct next char using char from first column in row i
        ctr -= 1 # decrement remaining char count

    return ''.join(S)
def read_bin_file(binfile):
    with open(binfile, "rb") as f:
        bit_string = ""
        byte = f.read(1)
        while byte:
            # print(byte[0])    
            # print(chr(byte[0]))
            # print(int(chr(byte[0]),2))
            byte = ord(byte)

            # print(byte)
            bitstr=num_to_bitsStr(byte)
            while len(bitstr)<8:
                bitstr="0"+bitstr
            bit_string+=bitstr
            # print(bin(byte))                                                             
            # bits = bin(byte)[2:].rjust(8, '0')
            # bit_string += bits
            # print(bit_string)
            byte = f.read(1)
    return bit_string
def read_bin_file(binfile):
    mybinfile=open(binfile,"rb")
    mybytes=mybinfile.read()
    return mybytes
class Node:
    def __init__(self, val=None):
        self.val = val              # val = bit value otherwise string char
        self.childs = [None] * 2    # 0 = left, 1 = right
    
    def insertChild(self, child, pos=0):
        assert pos == 0 or pos == 1
        self.childs[pos] = child

    def hasChild(self, val: int):
        assert val == 0 or val == 1
        return self.childs[val] is not None

    def isLeaf(self):
        return self.childs[0] is None and self.childs[1] is None
class Decode:
    def __init__(self,binfile) -> None:
            self.bytes= read_bin_file(binfile)
            # print(self.bytes)
            self.bit_string=self.read_byte(2)
            # print(self.bit_string)
    def read_byte(self,num_bytes:int=1):
        bit_arr=""
        byte=self.bytes[:num_bytes]
        self.bytes=self.bytes[num_bytes:]
        # print(byte)
        bitsstr=num_to_bitsStr(int.from_bytes(byte, byteorder='big'))
        while len(bitsstr)<8*num_bytes:
            bitsstr="0"+bitsstr
        bit_arr+=bitsstr
        return bit_arr
    def elias_decode_rec(self,val:int=1):
        results=None
        rv=val
        buffer=[]
        payload=False
        for i in range(val):
            buffer.append(int(self.bit_string[i]))
            rv-=1
            if rv==0:
                payload=buffer[0]==1
                buffer[0]=1
                rv=bit_to_int(buffer)+1
                self.bit_string=self.bit_string[val:]
                if payload:
                    results=rv-1
                    # print(results)
                    return results
                if len(self.bit_string)<rv+val:
                    if rv//8>0:
                        self.bit_string+=self.read_byte(rv//8)
                    else:
                        self.bit_string+=self.read_byte()
                    return self.elias_decode_rec(rv)
                else:   
                    return self.elias_decode_rec(rv)
    def binary_to_string(self):
        res=""
        for i in range(7):
            res+=self.bit_string[i]
        self.bit_string=self.bit_string[7:]
        return ''.join([chr(int(res, 2))])

    def huffman_tree_builder(self,tree:Node,char,code_length):
        code=""
        if len(self.bit_string)<code_length:
            self.bit_string+=self.read_byte(code_length//8+1)
        for i in range(code_length):
            code+=self.bit_string[i]
        active_node=tree
        for bit in code:
            bit=int(bit)
            if not active_node.hasChild(bit):
                active_node.insertChild(Node(bit),bit)
            active_node=active_node.childs[bit]
        active_node.val=char
        self.bit_string=self.bit_string[code_length:]
        return tree
    def huffman_decode_rec(self,tree):
        # print(s)
        res=""
        active_node=tree
        if len(self.bit_string)<1:
            self.bit_string+=self.read_byte()
        bit=self.bit_string[0]
        
        bit=int(bit)
        if active_node.hasChild(bit):
            active_node=active_node.childs[bit]
            self.bit_string=self.bit_string[1:]
            return self.huffman_decode_rec(active_node)
        if active_node.isLeaf():
            res+=active_node.val
            active_node=tree  
            return res
    def test(self):
        length=self.elias_decode_rec()
        no_unique=self.elias_decode_rec()
        # print(length,no_unique)
        # print(self.bit_string)
        unq_char=[]
        huffman_tree=Node()
        for _ in range(no_unique):
            if len(self.bit_string)<7:
                self.bit_string+=self.read_byte()
            unq_char.append(self.binary_to_string())
            # print(unq_char)
            # print(cur_ind,unq_char)
            if len(self.bit_string)<1:
                self.bit_string+=self.read_byte()
            code_length=self.elias_decode_rec()
            # print(code_length)
            # print(cur_ind,code_length)
            huffman_tree=self.huffman_tree_builder(huffman_tree,unq_char[-1],code_length)
        res=[]
        count=0
        while count<length:
            # print(self.bit_string)
            decoded_char=self.huffman_decode_rec(huffman_tree)
            # print(decoded_char)
            # print(self.bit_string)
            # print(cur_ind,decoded_char)
            
            cont_str=self.elias_decode_rec()
            # print(cont_str)
            # print(self.bit_string)
            count+=cont_str
            res.append((decoded_char,cont_str))
            # print(res)
        doom="".join([runlen_to_string(s) for s in res])
        # print(doom)
        decoded_txt= recover_text_from_BWT(length,sorted(doom), doom)
        # print(decoded_txt)
        return decoded_txt[:-1]
# t=Decode("bwtencoded.bin")
# t.test()


import sys
if __name__ == '__main__':
    _,encoded_bin_file=sys.argv
    d=Decode(encoded_bin_file)
    decoded_str=d.test()
    the_file=open("recovered.txt", "w")
    the_file.write(decoded_str)
    the_file.close()
# for i in range(600):
#     encoded_bin_file="bwtencoded"+str(i)+".bin"
#     text_file=open("recovered"+str(i)+".txt")
#     text=text_file.read()
#     d=Decode(encoded_bin_file)
#     recover=d.test()
#     if recover==text:
#         print("success")
#     else:
#         print(i,"Fail")

#         break
