"""
Name: Kang Hong Bo
Student Id: 32684673
Email:hkan0015@student.monash.edu
Last Updated:21/10/2022
"""
#%% Q! 
class FlowGraph :
    def __init__(self):
        """
        Constructor for FlowGraph. Create a empty list

        Precondition: -
        Postcondition: -
        Input:
            None
        Time complexity: 
            O(1)
        Space complexity: 
            O(V) where V is the total vertices inputed
        """
        self.vertices=[]
    def add_vertices(self,id,day=None):
        """
        Method adding vertex to the list

        Precondition: id is an integer
        Postcondition: a vertex object created and added into list
        Input:
            id: An integer of vertex unique id
            day: An integer specify which day is the vertex is on
        Time complexity: 
            O(V) where V is the number of vertices in the network
        Space complexity: 
            O(V) where V is the number of vertices in the network
        """
        self.vertices.append(Vertex(id,day))



    def getPath_bfs(self,source, sink):
        """
        This function finds a path from source to sink by BFS

        Precondition: -
        Postcondition: -
        Input:
            source: An integer reperesenting the starting vertex
            sink: An integer reperesenting the destination vertex
        Return: 
            path_from_source : A list of vertices indicating the path from source to sink
        Time complexity: 
            O(V+E) where V is the number of vertices in the network and E is the number of edges in the network
        Space complexity: 
            O(V) where V is the number of vertices in the network
        """
        self.reset()
        path_from_source = []
        discovered = []
        source = self.find_vertex(source)
        discovered.append(source)
        while len(discovered)>0:
            u=discovered.pop(0)
            u.visited = True
            if u.id == sink:
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
                v=self.find_vertex(v)
                if not v.discovered and not v.visited and edge.w>0:
                    discovered.append(v)
                    v.discovered=True
                    v.previous = u
    def checkPath_bfs (self,source,sink):
        """
        Function checks if there is a path by using bfs

        Precondition: -
        Postcondition: -
        Input:
            source: An integer reperesenting the starting vertex
            sink: An integer reperesenting the destination vertex
        Return: 
            boolean : True if there is an augmenting path, else False
        Time complexity: 
            O(V+E) where V is the number of vertices in the network and E is the number of edges in the network
        Space complexity: 
             O(V) where V is the number of vertices in the network
        """
   
        self.reset()
        source=self.find_vertex(source)
        discovered =[]
        discovered.append(source)   # queue
        while len(discovered)>0:
            u=discovered.pop(0)  # pop same as serve
            u.visited = True
            for edge in u.edges:
                v=edge.v
                v=self.find_vertex(v)
                if v.discovered ==False and v.visited == False and edge.w>0:
                    discovered.append(v)
                    v.discovered=True
                    if v.id==sink:
                        return True
        return False

    def residual_cap(self,path):
        """
        This function finds the maximum flow through the given path

        Precondition: -
        Postcondition: -
        Input:
            path: A list of integers indicating the augmenting path
        Return: 
            max_path_flow : An integer of maximum flow through the augmenting path
        Time complexity: 
            O(V+E) where V is the number of vertices in the path and E is the number of edges in the network
        Space complexity: 
             O(1)
        """
        max_flow=float("Inf")
        for x in range (len(path)-1):
            flow=self.find_vertex(path[x]).get_edge(path[x+1])
            max_flow=min(max_flow,flow.w)
        return max_flow

    def find_vertex(self,id):
        """
        A fuction to find the vertex

        Precondition: Id must be an integer
        Postcondition: -
        Input:
            id: An integer of vertex unique id
        Return: 
            i: the specific vertex object
        Time complexity: 
            O(V): where V is the total number of vertices
        Space complexity: 
            O(1)
        """
        for i in self.vertices:
            if(i.id==id):
                return i

    def update_edge(self,v1,v2,flow):
        """
        This function updates residual capacity of the edge between
        two vertex .

        Precondition: -
        Postcondition: The edge capacity is updated with flow
        Input:
            v1: An integer of the first vertex
            v2: An integer of the second vertex
            flow: An integer of maximum path flow 
        Time complexity: 
            O(E) where E is the number of edges of the vertices
        Space complexity: 
            O(1)
        """
        forward_edge=self.find_vertex(v1).get_edge(v2)
        reverse_edge = self.find_vertex(v2).get_edge(v1)
        forward_edge.w -= flow
        reverse_edge.w += flow
    def path_flow(self,path,flow):
        """
        This function updates residual capacities of the edges along the path
        with the given weight.

        Precondition: -
        Postcondition: Augment the flow based on path 
        Input:
            path: A list of integers indicating the augmenting path
            flow: An integer of maximum path flow 
        Time complexity: 
            O(V+E) where V is the number of vertices in the path and E is the number of edges of the vertices
        Space complexity: 
            O(1)
        """
        for i in range (len(path)-1):
            self.update_edge(path[i], path[i+1], flow)
    def ford_fulkerson(self,source,sink,bf_list,din_list):
        """
        This function returns two list which indicate the person which in charge of the meal of that day e.g
        ([0,1],[2,0]) day 1 breakfast is prepared by person 0 and dinner prepared by person 2
        day 2 breakfast is prepared by person 2 and dinner prepared by person 0
        Precondition: -
        Postcondition: the tuple of list bf and din will be return
        Input:
            source: An integer reperesenting the starting vertex
            sink: An integer reperesenting the destination vertex
            bf_list: A list that indicate which vertex is breakfast duty
            din_lis: A list that indicate which vertex is dinner duty
        Return:
            (bf,din): bf : a list of the person in charge of breakfast in the orders of the days
                      din :a list of the person in charge of dinner in the orders of the days
        Time complexity: 
            worst:O(n^2) where n is the days which we need to schedule
        Space complexity: 
            Input: O(1)
            Aux: O(V+M) where V is the number of vertices in the network and M is total meals
        """
        flow = 0
        bf=[None]*len(bf_list)
        din=[None]*len(din_list)

        while self.checkPath_bfs(source, sink):
            path = self.getPath_bfs(source, sink)
            
            # flow from a selector of the person
            if 0 in path:
                # check if the meals is breakfast
                if path[-3] in bf_list: # since the third last item in the vertex will always be meals 
                    if (self.find_vertex(path[-3])).day != None:
                        bf[(self.find_vertex(path[-3])).day]=path[2]-1
                # check if the meals is breakfast        
                if path[-3] in din_list:
         
                    if (self.find_vertex(path[-3])).day != None:
                        din[(self.find_vertex(path[-3])).day]=path[2]-1
            else:# flow from source
                if path[-3] in bf_list:
                    if (self.find_vertex(path[-3])).day != None:
                        bf[(self.find_vertex(path[-3])).day]=path[1]-1
                if path[-3] in din_list:
                    if (self.find_vertex(path[-3])).day != None:
                        din[(self.find_vertex(path[-3])).day]=path[1]-1
            max_path_flow = self.residual_cap(path)
            flow += max_path_flow
            self.path_flow(path, max_path_flow)

        if flow!=len(bf_list)+len(din_list):
            return None
        return (bf,din)

    def __str__(self):
        return_string =""
        for vertex in self.vertices:
            return_string=return_string+"Vertex "+str(vertex)+"\n"
        return return_string
    def reset(self):
        """
        This function resets the vertices in the network
        
        Precondition: -
        Postcondition: -
        Time complexity: 
            O(V) where V is the number of vertices in the network
        Space complexity: 
            O(1)
        """
        for vertex in self.vertices:
            vertex.discovered= False
            vertex.visited=False
    def add_edges(self,argv_edges,argv_directed=True):
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

            current_edge = Edge(u,v,w) 
            current_vertex=self.find_vertex(u)
            current_vertex.add_edge(current_edge)
            if not argv_directed:
                current_edge = Edge(v, u, 0)
                current_vertex=self.find_vertex(v)
                current_vertex.add_edge(current_edge)
class Vertex:
    def __init__(self,id,days=None):
        """
        Constuctor class for Vertex. This function initialize the properties 
        of a vertex
        Precondition: id is a non-negative integer
        Postcondition: a Vertex object is created
        Input:
            id: An integer of vertex unique id
            days: Indicate the days of the vertex 
        Time complexity: O(1)
        Space complexity:  O(E) where E is the number of edges of a particular vertex
        """
        self.id=id
        self.edges=[]
        self.discovered =False
        self.visited=False
        self.day=days
        self.previous=None
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
    
    def get_edge(self,target_vertex):
        """
        This functions gets the edge between current vertex
        and target vertex .

        Precondition: -
        Postcondition: an Edge between current vertex and target vertex is returned
        Input:
            target: An integer representing the destination vertex of the current edge
        Return:
            edge: An Edge object between current vertex and target vertex if there is one,else None

        Time complexity: 
            O(E) where E is the number of edges of a vertex
        Space complexity: 
            O(1)
        """
        for edge in self.edges:
            if edge.v==target_vertex:
                return edge
        return None
    def __str__(self):
        """
        return the string of the edge
        """
        return_string=str(self.id)
        for edge in self.edges:
            return_string=return_string+"\n with edge"+str(edge)
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


from math import ceil, floor
def allocate(availability):
    """
    A function which initialize a NetworkFlow and proceed ford fulkerson by having a input of the person availability.

    Precondition: A list of list which indicates the days and person and its availability the element in side the list of list is an integer 
                 between 0 to 3
    Postcondition: return the returned valued from the method ford fulkerson
    Input:
        availability: a list of list which its length of the outer list indicates the total days and the inner list indicates each person availability
    Return:
        (bf,din): bf : a list of the person in charge of breakfast in the orders of the days
                      din :a list of the person in charge of dinner in the orders of the days
    Time complexity: 
        O(n^2): where n is the days we need to schedule
    Space complexity: 
        O(V) where V is the number of vertices in the network
    """
    graph =  FlowGraph()
    graph.add_vertices(-1) # source
    graph.add_vertices(0) # the total demand needed days*2 (meals)
    graph.add_vertices(1) # first person
    graph.add_vertices(2) # second person
    graph.add_vertices(3) # third
    graph.add_vertices(4) # fourth
    graph.add_vertices(5) # fifth
    graph.add_vertices(6) # restaurant
    currentId=7
    edges=[]
    days=len(availability)
    bf_list=[]
    din_list=[]
    for i in range (len(availability)):
        bf=currentId
        bf_list.append(bf)
        din=currentId+1
        din_list.append(din)
        graph.add_vertices(bf,i)
        graph.add_vertices(din,i)
        currentId+=2
        
        for wl in range (len(availability[i])):
            if availability[i][wl]>0:
                graph.add_vertices(currentId,i)
                u=wl+1
                v=currentId
                w=1
                edges.append((u,v,w))
                
                if availability[i][wl]==1:
                    u=currentId
                    v=bf
                    w=1
                    edges.append((u,v,w))
                if availability[i][wl]==2:
                    u=currentId
                    v=din
                    w=1
                    edges.append((u,v,w))
                if availability[i][wl]==3:
                    u=currentId
                    v=bf
                    w=1
                    edges.append((u,v,w))
                    u=currentId
                    v=din
                    w=1
                    edges.append((u,v,w))
                currentId+=1
        # adding edges to each meals for the reastaurant   
        u=6 
        v=bf
        w=1
        edges.append((u,v,w)) 
        u=6 
        v=din
        w=1
        edges.append((u,v,w))
    # add selector edges for the person
    for i in range (5):
        u=0
        v=i+1
        w=ceil(0.44*days)-floor(0.36*days)
        edges.append((u,v,w))
    #add selector edges for the restaurant
    u=0
    v=6
    w=(0.1*days)//1
    edges.append((u,v,w))

    

    # adding flow for each meal to verify vertex 
    for bf in bf_list:
        edges.append((bf,currentId,1))
    for din in din_list:
        edges.append((din,currentId,1))
    graph.add_vertices(currentId) # creating the verify vertex to see if each meal is allocated
    currentId+=1
    

    graph.add_vertices(currentId) # creating the sink vertex
    edges.append((-1,0,days*2-floor(0.36*days)*5))
    edges.append((currentId-1,currentId,days*2))#adding the edge from verify vertex to sink
    #adding flow for the person for the demand of the person 
    for test in range (5):
        edges.append((-1,test+1,floor(0.36*days)))
    graph.add_edges(edges,False)
    flow=graph.ford_fulkerson(-1,currentId,bf_list,din_list)
    return flow



#%% Q2
class Node:
    def __init__(self,data=None,level=None,size=27+2):
        """
        Constuctor class for Node. This function initialize the properties 
        of a node
        Precondition: -
        Postcondition: a Node object is created
        Input:
            data: An integer indicate which string is inputed  
            size: An integer represeting the number of links the node has
            level: An integer represeting the level of the node
        Time complexity: 
            O(1) since size is fixed in our case
        Space complexity: 
            O(1) since size is fixed in our case
        """
        # terminal $ at index 0
        self.link =[None] *size
        self.data=data
        self.level=level
class Trie:
    def __init__(self) -> None:
        """
        Constuctor of trie initialize properties of the trie
        Precondition:-
        Postcondition: a Trie object is created
        Input:
           None
        Time complexity: 
            O(1)
        Space complexity: 
            O(1)
        """
        self.root=Node(level=0)
        self.longest_sub=""
        self.temp=""
    def insert_recur(self,key,data=None):
        """
        Insert a key into the trie .
        
        Precondition: -
        Postcondition: a key is inserted into the trie.
        Input:
            key : A string that represents the submission
            data: The indicator of the submission
        Time complexity: 
            O(M) where M is the length of the string
        Space complexity: 
             O(M) where M is the length of the string
        """
        current = self.root
        self.temp=""

        self.insert_recur_aux(current,key,data)
    def insert_recur_aux(self,current, key,data):
        """
        An auxillary function to insert a key into the trie .
        
        Precondition: -
        Postcondition: a key is inserted into the trie.
        Input:
            current: current node in the trie
            key : A string that represents the submission
            data: The indicator of the submission
        Time complexity: 
            O(M) where M is the length of the string
        Space complexity: 
            O(M) where M is the length of the string
        """
        current_level=current.level
        if len(key) == 0:
            # what happen when i go through all of my alpha in key
            if current.link[0]is not None:
                current = current.link[0]
            else:
                current.link[0]=Node()
                current=current.link[0]
                current.level=current_level+1
            if(len(self.temp)>len(self.longest_sub)):
                self.longest_sub=self.temp
            return self.longest_sub
            
        #recur
        else:
             #if path exist
            #convert ascii to index
            if key[0]==" ":
                index=28
            else:
                index=ord(key[0]) - 97 + 1
            if current.link[index]is not None:
                current=current.link[index]
                if current.data==1 and data==2 :
                    self.temp+=key[0]
                
            else:
                current.link[index]=Node()
                current=current.link[index]
                current.data=data
                current.level=current_level+1
            self.insert_recur_aux(current,key[1:],data)


    



def compare_subs(submission1, submission2):
    """
    A function to search for the longest same substring.
    
    Precondition: submission1 and 2 must be a string with character in between a to z or spaces
    Postcondition: -
    Input:
        submission1: A string which has only character in between a to z or spaces
        submission2: A string which has only character in between a to z or spaces
    Return:
        return a string that represents the longest substring and the followwing percentage of the 
        substring in the submission string.
    Time complexity: 
        O(N^2+M^2): inserting the substring of both submission which N is the len of the string submission1 and 
                M is the len of the string submission2 and 
    Space complexity: 
        Input: O(1)
        Aux: O(1)
    """
    trie=Trie()
    per1=0
    per2=0
    
    for i in range (len(submission1)):
        trie.insert_recur(submission1[i:],1)
    for i in range(len(submission2)):
        trie.insert_recur(submission2[i:],2)

    if len(submission1)==0 or len(submission2)==0:
        return [trie.longest_sub,per1,per2]
    else:
        
        if ((len(trie.longest_sub)/len(submission1))*100)%1>=0.5:
            per1=int((len(trie.longest_sub)/len(submission1))*100)+1
        else:
            per1=int((len(trie.longest_sub)/len(submission1))*100)
        if ((len(trie.longest_sub)/len(submission2))*100)%1>=0.5:
            per2=int((len(trie.longest_sub)/len(submission2))*100)+1
        else:
            per2=int((len(trie.longest_sub)/len(submission2))*100)
        return [trie.longest_sub,per1,per2]











