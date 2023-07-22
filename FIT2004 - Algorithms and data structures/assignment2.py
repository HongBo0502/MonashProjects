"""
Name: Kang Hong Bo
Student Id: 32684673
Email:hkan0015@student.monash.edu
Last Updated:17/09/2022
"""

from json.encoder import INFINITY


#%% Question 1



class MinHeap:
    """Reference:MinHeap class taken from FIT1008"""
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
            distance : A non-negative integer of distance of vertex from start
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






class RoadGraph:

    def __init__(self,roads,cafes):
        """
        Constructer of Road Graph. Initialize the memory for the vertices,and store the roads and cafe.

        Precondition: Roads will not have negative distance and cafes will not have negative waiting time.
        Postcondition: A RoadGraph object created

        Input:A list of roads which has a tuple of a place to a place and it distance , a list of cafe which 
              is the tuple of the position of the cafe and the waiting time of the cafe

        Time Complexity: O(V+C) where V is the total vertices and C is the total existing cafe
        Space Complexity: O(V+C) where V is the total vertices and C is the total existing cafe

        """
        max_vertex=0
        self.roads=[]
        for road in roads:
            u=road[0]
            v = road[1]
            max_vertex=max(max_vertex,max(u,v))
            self.roads.append(road)
        total_vertices=max_vertex+1
        self.vertices=[None]*(total_vertices)
        self.revVertices=[None]*(total_vertices)
        for i in range (total_vertices):
            self.vertices[i]=Vertex(i)
            self.revVertices[i]=Vertex(i)
        self.add_edges(roads)
        self.add_edges(roads,True)
        self.cafes=[]
        for cafe in cafes:
            self.cafes.append(cafe)
    
    def add_edges(self,argv_edges,rev=False):
        """
        Add edges in to vertices, rev = true will add edges in recverse direction to the vertices
        Precondition: argv_edges must be a list
        input:argv_edges: is a list of tuple which consist the starting point the ending point and the distance
              rev: a boolean
        Time complexity: O(E) where E is the total edges 
        Space complexity: O(1)
        """
        for edge in argv_edges:

            u=edge[0]
            v=edge[1]
            w=edge[2]
            if rev==False:
                current_edge = Edge(u,v,w) 
                current_vertex=self.vertices[u]
                current_vertex.add_edge(current_edge)
            else:
                current_edge = Edge(v,u,w) 
                current_vertex=self.revVertices[v]
                current_vertex.add_edge(current_edge)
    
    def update(self,start,vertices):
        """
        A function which will update the distance of the vertices 
        Precondition : the start integer must in the vertex list 
        Postcondition: the vertices that passed in will update with distance and previous 
        input:
            start: a integer which determine the vertex we will start to update from
            vertices: the vertices list that is going to update
        Time Complexity:O(ElogV)where E is the edges(roads) and V is the vertices(position)
        Space Complexity:O(1)
        """
        # path=[]
        
        #     path.append(start)
            
        #     return path
        if len(vertices)>1:
            start=vertices[start]
            start.distance=0
            discovered =MinHeap(len(vertices))
            discovered.add(start.id,start.distance)   
            while len(discovered)>0:
                u,u_distance=discovered.get_min()
                u=vertices[u]
                u.distance=u_distance
                u.visited = True
                for edge in u.edges:
                    v=edge.v
                    v=vertices[v]

                    if v.visited ==False and v.discovered ==False:
                        v.discovered=True
                        v.distance = u.distance+edge.w
                        v.previous=u
                        discovered.add(v.id,v.distance)
                    else :
                        if v.visited ==False:
                            if v.distance > u.distance + edge.w:
                                v.distance=u.distance +edge.w
                                v.previous=u
                                discovered.update(v.id,v.distance)
        else:
            return None
    def routing(self,start,end):
        """
        Return a route which has the shortest possible distance and time with passing a cafe  
        Precondition: start and end is a vertex.id in the vertices list
        Return: a list of the shortest path
        Time Complexity: O(ElogV) where E is the edges(roads) and V is the vertices(position)
        Space Complexity: O(P+R) where P is the visited vertices and R is the total route that is the minimum spending time route
        """
        compare_lst=[]
        starttocafe=[]
        cafetoend=[]
        update=self.update(start,self.vertices)
        ret=self.update(end,self.revVertices)
 
        
        for cafe in self.cafes:
            cafe_vertex,_=cafe
            u=self.vertices[cafe_vertex]

            v=self.revVertices[cafe_vertex]
            
            if( u.visited==True or u.discovered==True )and( v.visited==True or v.discovered==True ):
                

                x=u.distance+v.distance+_
                compare_lst.append((cafe_vertex,x))
        if len(compare_lst)>0:

            final_cafe_vertex,totaldistance=min(compare_lst, key=lambda x: x[1])
            currentToStart=self.vertices[final_cafe_vertex]
            currentToEnd=self.revVertices[final_cafe_vertex]
      
            
            while currentToStart.previous!=None:
                starttocafe.append(currentToStart.id)
                currentToStart=currentToStart.previous
            if currentToStart.id==start:
                    starttocafe.append(currentToStart.id)
            starttocafe=starttocafe[::-1]
            
            while currentToEnd.previous!= None:
                
                currentToEnd=currentToEnd.previous
                cafetoend.append(currentToEnd.id)
            
                
          
            return starttocafe+cafetoend  

        else:
            return None

class Vertex:
    def __init__(self,id):
        """
        Constuctor class for Vertex. This function initialize the properties 
        of a vertex
        Precondition: id is a non-negative integer
        Postcondition: a Vertex object is created
        Input:
            id: An integer of vertex unique id
        Time complexity: O(1)
        Space complexity:  O(E) where E is the number of edges of a particular vertex
        """
        self.id=id
        self.edges=[]
        self.discovered =False
        self.visited=False
        self.distance=0
        self.previous=None
        self.time=0
    def add_edge(self,edge):
        """
        This functions add an edge to a vertex

        Precondition: edge is in tuple form (u, v, w)
        Postcondition: a Vertex object is created
        Input:
            id: An integer of vertex unique id
        Time complexity: O(1)
        Space complexity:  O(1)
        """
        self.edges.append(edge)
    def __str__(self):
        """
        Return String of the vertex

        """
        return_string=str(self.id)
        for edge in self.edges:
            return_string=return_string+"\n with edge"+str(edge)+" Distance "+str(self.distance)+ " Visited "+str(self.visited) +" Discovered "+str(self.discovered)+"Previous"+str(self.previous)
        return return_string
class Edge:
    def __init__(self,u,v,w):
        """
        Constuctor class for Edge. This function initialize the properties 
        of an edge
        Postcondition: an Edge object is created
        Input:
            u:The starting location ID for a road, represented as a non-negative integer.
            v:The ending location ID for a road, represented as a non-negative integer
            w:The distance along that road, represented as a non-negative integer.
        Time complexity: O(1)
        Space complexity:  O(1)
        """
        self.u=u
        self.v=v
        self.w=w
    def __str__(self):
        """
        return the string of the edge
        """
        return_string = str(self.u)+","+str(self.v)+","+str(self.w)
        return return_string


#%% Question 2

def optimalRoute(routeScore,start,end):
    """
    return the route which give the highest score possible of the start to end 
    precondition:routeScore must be a list
    return: the route which give the highest possible to score from start to end
    Input: routeScore: a list of tuple which take in the starting point , ending point and score e.g.(start,end,score)
    Time Complexity:
    """
    max_IP=0
    routes=[]
    for route in routeScore:
        u=route[0]
        v = route[1]
        max_IP=max(max_IP,max(u,v))
        routes.append(route)
    total_intersects= max_IP+1
    intersects=[None]*(total_intersects)
    for i in range (total_intersects):
        intersects[i]=Vertex(i)
    add_edges(intersects,routeScore)
    return bellmanford(intersects,routeScore,start,end)
def add_edges(intersect_list,argv_edges):
        """
        Add edges in to vertices
        Precondition: argv_edges must be a list
        input:
            intersect_list: a list of the total intersection
            argv_edges: is a list of tuple which consist the starting point the ending point and the distance
        Time complexity: O(E) where E is the total edges 
        Space complexity: O(1)
        """
        for edge in argv_edges:
            u=edge[0]
            v=edge[1]
            w=edge[2]
            current_edge = Edge(u,v,w) 
   
            current_vertex=intersect_list[u]
         
            current_vertex.add_edge(current_edge)
def bellmanford(intersect_list,routes_list,start,end):
    """
    Function that take in the point and the routes with the start and end a list of routes which will get the maximum possible point 
    Precondition: intesect_list and routes_list must be a list
    Return : a list of routes which will get the maximum possible point
    Input: intersect_list : a list of the total intersection
           routes_list: a list of the edges which is in a tuple form
           start: a number which represent which intersect is starting at
           end: a number which represent which intersect is it ending
    Time complexity: O(DE) where D is the total intersection and E is the routes
    Space complexity:O(N) where N is the length of the return routes
    """
    for i in intersect_list:
        if i.id == start:
            
            i.distance=0
        else:
            i.distance=INFINITY
            i.previous=None
    for i in range (1,len(intersect_list)):
        for routes in routes_list:
            if intersect_list[routes[1]].distance==INFINITY or intersect_list[routes[0]].distance==INFINITY:

                if intersect_list[routes[0]].distance +routes[2]<intersect_list[routes[1]].distance:

                    intersect_list[routes[1]].distance =intersect_list[routes[0]].distance +routes[2]

                    intersect_list[routes[1]].previous=intersect_list[routes[0]].id
            else:
                if intersect_list[routes[0]].distance +routes[2]>intersect_list[routes[1]].distance:
                    intersect_list[routes[1]].distance =intersect_list[routes[0]].distance +routes[2]

                    intersect_list[routes[1]].previous=intersect_list[routes[0]].id

    res=[]
    res.append(end)
    current=intersect_list[end]
    while(current.previous!=None):

        current=intersect_list[current.previous]

        res.append(current.id)
    if len(res)==1 and res[0]!=start:
        return None
    return res[::-1]


