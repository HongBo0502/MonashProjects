#%%
class MinHeap:
    MIN_CAPACITY = 1

    def __init__(self, max_size) :
        """
        Constuctor class for MinHeap. This function initialize the properties 
        of a MinHeap , i.e an array that represents the heap and a mapping
        array that stores the index which points to the position in the heap
        
        Precondition: max_size is a positive integer
        Postcondition: a MinHeap object is created
        Input:
            max_size: An integer that represents the max size of the heap
        Time complexity: 
            Best: O(1)
            Worst:O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(N) where N is the max size of array
        """
        self.length = 0
        self.the_array = [None]* (max(self.MIN_CAPACITY,max_size)+1)
        self.map = [None]* max_size

    def __len__(self):
        """
        Return the length of the array/heap
        """
        return self.length

    def is_full(self):
        """
        Return true if the array is full , else false
        """
        return self.length + 1 == len(self.the_array)
    
    def swap(self,i,j):
        """
        Swap the position of two elements in a heap based on their corresponding index.
        The map array is also updated accordingly.
        
        Precondition: 1 <= i <= self.length
                    1 <= j <= self.length
        Postcondition: the position of two elements in the heap are swapped
        Input:
            i: An index of the first item being swapped
            j: An index of the second item being swapped
        Time complexity: 
            Best: O(1)
            Worst:O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        self.map[self.the_array[i][0]]=j
        self.map[self.the_array[j][0]]=i
        self.the_array[i],self.the_array[j]=self.the_array[j],self.the_array[i]
        
    def rise(self, k) :
        """
        Rise element at index k to its correct position
        
        Precondition: 1 <= k <= self.length
        Postcondition : The element at index k is rised to its correct position
        Input:
            k: An index of the element to be rised
        Time complexity: 
            Best: O(1) when the element is already at its correct position
            Worst:O(log N) where N is the max size of heap
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        item = self.the_array[k][1]
        while k > 1 and item < self.the_array[k // 2][1]:
            self.swap(k,k//2)
            k = k // 2

    def add(self, vertex_id,distance):
        """
        Inserts a tuple (vertex_id,distance) into the minheap and
        perform rise operation.
        
        Precondition: vertex_id >=0
        Postcondition : A tuple (vertex_id,distance) is added to the heap
        Input:
            vertex_id: A non-negative integer that represents a vertex
            distance : A non-negative integer of distance of vertex from source
        Time complexity: 
            Best: O(1) when the element is already at its correct position
            Worst:O(log N) where N is the max size of heap
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        if self.is_full():
            raise IndexError

        self.length += 1
        self.the_array[self.length] = vertex_id,distance
        self.map[vertex_id]=self.length
        self.rise(self.length)

    def smallest_child(self, k):
        """
        Returns the index of k's child with smallest value.
        
        Precondition: 1 <= k <= self.length // 2
        Postcondition : The index of k's child with smallest value is returned
        Input:
            k: An index of a parent in the heap
        Time complexity: 
            Best: O(1) 
            Worst:O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        
        if 2 * k == self.length or \
                self.the_array[2 * k][1] < self.the_array[2 * k + 1][1]:
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k):
        """ 
        Make the element at index k sink to the correct position.
        
        Precondition: 1 <= k <= self.length
        Postcondition: The element at index k sink to the correct position
        Input:
            k: An index of an element to be sink
        Time complexity: 
            Best: O(1) when the element is already at its correct position
            Worst:O(log N) where N is the max size of heap
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        item = self.the_array[k][1]

        while 2 * k <= self.length:
            min_child = self.smallest_child(k)
            if self.the_array[min_child][1] >= item:
                break
            self.swap(k,min_child)
            k = min_child

        
    def get_min(self):
        """ 
        Remove (and return) the minimum element from the heap. 
        
        Precondition: the heap is not empty
        Postcondition: the minimum element is retrieved
        Time complexity: 
            Best: O(1) when the element is already at its correct position
            Worst:O(log N) where N is the max size of heap
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        if self.length == 0:
            raise IndexError

        min_item = self.the_array[1]
        self.length -= 1
        self.swap(1,self.length+1)
        self.sink(1)
        return min_item

    def update(self,vertex_id,smaller_distance):
        """
        Find an element in the heap and update it with the a new smaller distance.
        
        Precondition: This function only works with updating the current element with 
                        a smaller value (decrease key)
        Postcondition: The element in the heap is updated with smaller value
        Time complexity: 
            Best: O(1) when the element is already at its correct position
            Worst:O(log N) where N is the max size of heap
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        current_index=self.map[vertex_id]
        self.the_array[current_index]=vertex_id,smaller_distance
        self.rise(current_index)
#%% Graph class

class Graph :
    def __init__(self,argv_vertices_count):
        self.vertices=[None]*argv_vertices_count 
        for i in range (argv_vertices_count):
            self.vertices[i]=vertex(i)
        
    def __str__(self):
        return_string =""
        for vertex in self.vertices:
            return_string=return_string+"Vertex "+str(vertex)+"\n"
        return return_string
    def reset(self):
        for vertex in self.vertices:
            vertex.discovered= False
            vertex.visited=False
    def add_edges(self,argv_edges,argv_directed=True):
        for edge in argv_edges:
            u=edge[0]
            v=edge[1]
            w=edge[2]

            current_edge = Edge(u,v,w) 
            current_vertex=self.vertices[u]
            current_vertex.add_edge(current_edge)
            if not argv_directed:
                current_edge = Edge(v,u,w) 
                current_vertex=self.vertices[v]
                current_vertex.add_edge(current_edge)

    def bfs (self,source):
        """
        Function for BFS, starting from source

        """
        #self.matrix=[None]*len(v)
        #for i in range(len(v)):
            #self.matrix[i]=[None]*len(v)
        self.reset()
        source=self.vertices[source]
        source.color="Black"
        return_bfs=[]
        discovered =[]
        discovered.append(source)   # queue
        while len(discovered)>0:
            u=discovered.pop(0)  # pop same as serve
            u.visited = True
            return_bfs.append(u)
            for edge in u.edges:
                v=edge.v
                v=self.vertices[v]
                if v.discovered == True:
                    print("Found cycle")
                if v.discovered ==False and v.visited == False:
                    discovered.append(v)
                    v.discovered=True
        return return_bfs

    def bfs_distance (self,source):
        """
        Function for BFS, starting from source

        """
        discovered =[]
        discovered.append(source)   # queue
        while len(discovered)>0:
            u=discovered.serve()  # pop sasme as serve
            u.visited = True
           
            for edge in v.edges:
                v=edge.v
                if v.discovered ==False:
                    discovered.append(v)
                    v.discovered=True
                    v.distance = u.distance+1
                    v.previous=u
        #implement the backtracking on ur own
    def dijkstra (self,source,destination):
        """
        Function for BFS, starting from source

        """
        # self.reset()
        # source=self.vertices[source]
        # source.distance=0
        # discovered =MinHeap(len(self.vertices))
        # discovered.add(source.id,source.distance)   
        # while len(discovered)>0:
        #     u=discovered.get_min()
        #     u.visited = True
        #     for edge in u.edges:
        #         v=edge.v
        #         if v.discovered ==False:
        #             v.discovered=True
        #             v.distance = u.distance+edge.w
        #             v.previous=u
        #             discovered.add([v.id,v.distance])
        #         else :
        #             v.visited ==False
        #             if v.distance > u.distance + edge.W:
        #                 v.distance=u.distance +edge.w
        #                 v.previous=u
        #                 discovered.update(v.id,v.distance)
        path_from_source = []
        if source == destination:
            path_from_source.append(source)
            return path_from_source
        discovered = MinHeap(len(self.vertices))
        discovered.add(source,0)

        while len(discovered)>0:
            u,distance_u = discovered.get_min()
            print(u,distance_u)
            u = self.vertices[u]
            u.distance = distance_u
            u.visited = True
            if u.id == destination:
                path_from_source.append(u.id)
                current = u
                while current.previous!= None:
                    current = current.previous
                    path_from_source.append(current.id)
                    if current.id == source:
                        break
                return path_from_source[::-1]
            for edge in u.edges:
                v=edge.v
                v=self.vertices[v]
                current_distance = u.distance+edge.w
                if not v.discovered:
                    v.discovered=True
                    v.distance = current_distance
                    v.previous = u
                    discovered.add(v.id,v.distance)
                else: #has discovered
                    if not v.visited:
                        if v.distance> current_distance:
                            v.distance = current_distance
                            v.previous = u
                            discovered.update(v.id,v.distance)
        #implement the backtracking on ur own
    def dfs (self,source):
        """
        Function for DFS, starting from source

        """
        return_bfs=[]
        discovered =[]  #discovered is a stack, LIFO
        discovered.push(source)
        while len(discovered)>0:
            u=discovered.pop() 
            u.visited = True
            return_bfs.append(u)
            for edge in v.edges:
                v=edge.v
                if v.discovered ==False:
                    discovered.push(v)
                    v.discovered=True
        return return_bfs
class vertex:
    def __init__(self,id):
        self.id=id
        self.edges=[]
        self.discovered =False
        self.visited=False
        self.distance=0
        self.previous=None
    def add_edge(self,edge):
        self.edges.append(edge)
    def __str__(self):
        return_string=str(self.id)
        for edge in self.edges:
            return_string=return_string+"\n with edge"+str(edge)
        return return_string
    def added_to_queue(self):
        self.discovered=True
    def visit_node(self):
        self.visited=True
class Edge:
    def __init__(self,u,v,w):
        self.u=u
        self.v=v
        self.w=w
    def __str__(self):
        return_string = str(self.u)+","+str(self.v)+","+str(self.w)
        return return_string


#%% create a graph with 5 vertices

if __name__=="__main__":
    total_vertices=6
    
    my_graph=Graph(total_vertices)

   
    edges=[]
    edges.append((3,1,5))
    edges.append((1,2,1))
    edges.append((2,5,33))
    edges.append((3,2,10))
    # print (my_graph)
    my_graph.add_edges(edges,True)
    # for Vertex in range (total_vertices):
    #     print(str(Vertex)+" infected"+str(len(my_graph.bfs(Vertex))))
    # print(my_graph.bfs(3))
    # for i in (my_graph.bfs(3)):
    #     print(i)
    bla= my_graph.dijkstra(3,2)
    print(bla)
    # for ver in bla:
    #     print(ver)
# %%

    
    # total_vertices=6
    
    # my_graph=Graph(total_vertices)

   
    # edges=[]
    # edges.append((3,1,5))
    # edges.append((1,2,1))
    # edges.append((2,5,6))
    # edges.append((3,2,7))
    
    # my_graph.add_edges(edges,True)
    # heap = Heap(total_vertices)
    # for i in range(total_vertices):
    #     heap.add([i,my_graph.vertices[i].distance])

    
    # while(len(heap) > 0):
    #     print(heap.get_min())

