
#%% Starting the python kernel



print("Hello world!")
#%% Function counting sort
def sort_counting(new_list):
    """
    Precondition : new_list have at least 1 item
    """
    # find maximum
    max_item=new_list[0]
    for item in new_list:
        if item>max_item:
            max_item=item
    # initialize count array
    count_array=[0]*(max_item+1)
    # update count array
    for item in new_list:
        count_array[item]=count_array[item]+1
    # update input array
    index=0
    for i in range (len(count_array)):
        item=i
        frequency=count_array[i]
        for i in range(frequency):
            new_list[index]=item
            index+=1
    
    # new_list will be sorted
    return new_list\
#%% Function Alpha
def sort_counting_alpha(new_list):
    """
    Precondition : new_list have at least 1 item
    """
    # find maximum
    max_item=new_list[0]
    for item in new_list:
        if item>max_item:
            max_item=item
    print(max_item)
    # initialize count array
    count_array=[0]*(max_item+1)
    print(count_array)
    # update count array
    for item in new_list:
        count_array[ord(item)-97]=count_array[ord(item)-97]+1
    print(count_array)
    # update input array
    index=0
    for i in range (len(count_array)):
        item=i
        frequency=count_array[i]
        for i in range(frequency):
            new_list[index]=chr(item+97)
            index+=1
    
    # new_list will be sorted
    return new_list

#%% Function Stable
def sort_counting_stable(new_list):
    """
    Precondition : new_list have at least 1 item
    """
    # find maximum
    max_item=new_list[0]
    for item in new_list:
        if ord(item)-97>max_item:
            max_item=ord(item)-97
    print(max_item)
    # initialize count array
    count_array=[None]*(max_item+1)
    for i in range(len(count_array)):
        count_array[i]=[]
    print(count_array)
    # update count array
    for item in new_list:
        count_array[item].append(item)
    print(count_array)

    # update input array
    new_list=[]
    i=0
    while i!=max_item:
        new_list+=count_array[i]
        i+=1
    
    # new_list will be sorted
    return new_list
#%% Function Stable alpha
def sort_counting_stable_alpha(new_list,column):
    """
    Sorting the alphabet without changing the sequence of the list
    Precondition : new_list have at least 1 item
    :Input:
        new_list
        
    
    
    """
    # find maximum
    
    max_item=ord(new_list[0][column])
    for item in new_list:
        if ord(item[column])>max_item:
            max_item=ord(item[column])
    # print(max_item)

        # print(max_item)
    # initialize count array
    count_array=[None]*(max_item+1)
    for i in range(len(count_array)):
        count_array[i]=[]
    # print(count_array)
    # update count array

    for item in new_list:
        count_array[ord(item[column])].append(item)

    # print(count_array)

    # update input array
    new_list=[]
    i=0
    while i!=max_item+1:
        new_list+=count_array[i]
        i+=1
    
    # new_list will be sorted
    return new_list
#%% Radix Sort
def Radix_sort(a_list):
    """
    
    """
    #process counting sort by column
    for i in range (len(a_list[0])):
        a_list=sort_counting_stable_alpha(a_list,len(a_list[0])-i-1)
        # print(a_list)
    return a_list

# %% Driver
# list_a =[200,151,291,981,369,421,671]
# list_a=["a","c","a","s","r","w","z","e"]
list_a=["AB","GS","EA","QC","ZA","EZ","EL","RN","ZM","AQ","PS"]
# list_a=["A","V","Q","A","C","E","Z"]

print(list_a)
list_a = Radix_sort(list_a)

print(list_a)







# %% test
test="123"

print(bool(None))


#%%
list_a=["ba","ab","abc","aaaa"]
sorted(list_a)

# %%
