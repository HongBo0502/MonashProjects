"""
Name: Kang Hong Bo
Student ID: 32684673
"""


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
                        # print("end"+str(edge.end))
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

def read_input(textfile):
    textFile=open(textfile,"r")
    txt=textFile.read()
    textFile.close()
    return txt

import sys
if __name__ == '__main__':
    _,textfile=sys.argv
    txt=read_input(textfile)
    output_file=open("output_sa.txt","w")
    T=SuffixTree()
    T.preprocess(txt)
    suff_arr=T.inorder(T.root)
    for i in suff_arr:
        output_file.write(str(i+1)+"\n")

    output_file.close()