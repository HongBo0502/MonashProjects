"""
Name: Kang Hong Bo
Student Id: 32684673
Email:hkan0015@student.monash.edu
Last Updated:16/08/2022
"""
#%% counting sort for a list of list which sort integer

from bdb import effective


def sort_counting_stable(lol_list,column):
    """
    The function will take in a list of list and the postion of the integer element inside the list of list 
    to sort in descending order.
    Precondition : lol_list have at least 1 item and must be a list of list 
    Input :
        lol_list:a list of matches which is in a sequence[[Team 1, Team2 ,score],[...]]
        column : the column of the elements of the list of list.
    Return : a list of list which is sorted by the integer in descending order
    
    Time complexity: O(n+m) where n is the length of the list and the m is the max value of the elements

    Aux space complexity:  O(n+m) where m is the maximum item in the list and n is the total item in the list
    """ 
    # find maximum
    max_item=lol_list[0][column]
    
    for item in lol_list:
        if item[column]>max_item:
            max_item=item[column]
    # print(max_item)
    # print(max_item)
    # initialize count array
    count_array=[None]*(max_item+1)
    for i in range(len(count_array)):
        count_array[i]=[]
    # print(len(count_array))
    # update count array
    for item in lol_list:
        count_array[item[column]].append(item)
    # print(count_array)
    # print(count_array)
    #remove the element inside lol_list to reassign
    lol_list=[] 
    # update input array descending
    i=max_item
    
    while i!=-1:
        lol_list+=count_array[i]
        
        i-=1
    
    # new_list will be sorted
    return lol_list
#%% counting sort for a list of list which sort integer
def sort_counting_stable_alpha(new_list,roster,column=0,str_col=0):
    """
    The function can take in a string , list of string  or list of list to sort according to the argument is given 
    Precondition : new_list have at least 1 item
    Input:
        new_list: a string input or a list of string
        roster: a integer which specified the max possible of the alphabet that can control the count array
        column: a integer which state which column of the item we are looking eg(for team 1 the column(index) will be 0 and team2 will be 1)
        str_col: a integer which specified the string column which we are sorting with
    Postcondition : a string or a list of list which is sorted by string in ascending order 

    Time complexity :O(n) n is the length of the new_list

    Aux space complexity : O(n) n is the total item in the list
    
    """
    # find maximum
    
    
    

    # initialize count array
    count_array=[None]*(roster)
    for i in range(roster):
        count_array[i]=[]
    
    # update count array

    for item in new_list:

        count_array[ord(item[column][str_col])-65].append(item)



    # update input array
    i=0
    for list in count_array:
        for item in list:
            new_list[i]=item
            i+=1
    
    # new_list will be sorted
    return new_list
#%% Radix Sort
def Radix_sort(a_list,roster):
    """
    The function will take in a list of list and a rosters to perform multiple counting sorts in a specific order.

    Precondition : a_list must have at least 1 item roster must be a number between 1 until 26
    Input :
        a_list:a list of matches which is in a sequence[[Team 1, Team2 ,score],[...]]
        roster : a integer which will be pass in the counting sorts
    Return : a list of list which is sorted firstly with descending order of score then ascending order of team 1 and team 2
    
    Time complexity: O(M) where M is the length of the teams

    Aux space complexity: O(0)
    """ 
    #take the second team to sort first then first team and finally the score (index 1,0,-1)
    x=1
    while x!=-2:
            if type(a_list[0][x])==str:
                for y in range(len(a_list[0][x])-1,-1,-1):
                    a_list=sort_counting_stable_alpha(a_list,roster,x,y)
            else :
                a_list=sort_counting_stable(a_list,x)
            x-=1
    return a_list


# %% result in both ways
def reversed_team_score(match):
    """
    The function will take in a list of list and add the reversed team record.

    Precondition : match must have at least 1 item 
    Input :
        match :a list of matches which is in a sequence[[Team 1, Team2 ,score],[...]]
    Return : a list of list which added a reversed match records
    
    Time complexity: O(n) where n is the length of list of matches

    Aux space complexity: O(2N) where N is the total item in list
    """ 
    new_res=[]
    for i in match :
        new_res+=[i]
        x=[i[1],i[0],100-i[2]]
        new_res+=[x]
    return new_res

# %% ascending lexicographical  order
def sorting_team(matches,roster):
    """
    The function will take in a list of list and a rosters to sort the team in lexicographical order .

    Precondition : matches must have at least 1 item roster must be a number between 1 until 26
    Input :
        matches:a list of matches which is in a sequence[[Team 1, Team2 ,score],[...]]
        roster : a integer which will be pass in the counting sorts
    Return : a list of list which is the team is sorted
    
    Time complexity: O(nm) where m is the total match in the list ,n is the time complexity of calling sort function

    Aux space complexity: O(0)
    """ 
    for i in matches:
        i[0]="".join(sort_counting_stable_alpha(list(i[0]),roster))
        i[1]="".join(sort_counting_stable_alpha(list(i[1]),roster))
    return matches

#%% remove same 

def remove_duplicate(matches):
    """
    The function will take in a list of list and remove the same matches record.

    Precondition : matches must have at least 1 item
    Input :
        matches:a list of matches which is in a sequence[[Team 1, Team2 ,score],[...]]
    Return : a list of list which do not have same list
    
    Time complexity:O(n) where n is the length of the matches

    Aux space complexity: O(n) where n is the total matches which is recorded
    """ 
    lst=[]
    for i in matches:
        if i not in lst:
            lst.append(i)
    return lst
#%% top10matches
def top10matches(matches):
    """
    The function will take in a list of list and return a list of the top 10 matches 

    Precondition : matches must have at least 1 item
    Input :
        matches:a list of matches which is in a sequence[[Team 1, Team2 ,score],[...]]
    Return : a list of list of top 10 matches
    
    Time complexity: O(n) where n is the length of the matches

    Aux space complexity: O(1) where they will be only 10 records will be save 
    """ 
    lst=[]
    i=0
    while len(lst)!=10 and i<len(matches) :
        lst.append(matches[i])
        i+=1
    
    return lst

#%% search mathches
def searchMatches(matches,score):
    """
    The function will take in a list of list and search for the specific matches record.

    Precondition : matches must have at least 1 item
    Input :
        matches:a list of matches which is in a sequence[[Team 1, Team2 ,score],[...]]
        score :  a integer which we want to search
    Return : a list of list of records which we want to search
    
    Time complexity: O(n) where n is the length of the matches

    Aux space complexity: O(1)
    """ 
    boundary1=0
    j=0
    boundary2 = len(matches)-1
    while (j <=boundary2):
        if matches[j][2] >score:
            matches[boundary1], matches[j] = matches[j],matches[boundary1]
            boundary1 += 1
            j += 1
        elif matches[j][2] <score:
            matches[j], matches[boundary2]=matches[boundary2],matches[j]
            boundary2 -= 1
        else:         
            j += 1

    if boundary1==j and boundary1!=0:
        
        return searchMatches(matches,matches[boundary2][2]) 
    else:
        return matches[boundary1:boundary2+1]

result=[["EAE", "BCA", 85], ["EEE", "BDB", 17], ["EAD", "ECD", 21],
["ECA", "CDE", 13], ["CDA", "ABA", 76], ["BEA", "CEC", 79],
["EAE", "CED", 8], ["CBE", "CEA", 68], ["CDA", "CEA", 58],
["ACE", "DEE", 24], ["DDC", "DCA", 61], ["CDE", "BDE", 67],
["DED", "EDD", 83], ["ABC", "CAB", 54], ["AAB", "BDB", 15],
["BBE", "EAD", 28], ["ACD", "DCD", 50], ["DEB", "CAA", 21],
["EBE", "AAC", 24], ["EBD", "BCD", 48]]
results1=[['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42],
['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36],
['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49],
['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46],
['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30],
['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]
results2=[['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42],
['AAA', 'AAA', 38]]
# %% Analyse
results = [['ENQDPRQCDGDC', 'OAHFHJMQDMNK', 14], ['IOIHNOFMBKDC', 'FFJBMKOGLNCM', 56],
                    ['QARKJGHQCCML', 'QBRLNNQNGAJP', 69], ['HOQPACDCKAQA', 'CEALGJBPINPK', 56],
                    ['OCGFKPJOCGDD', 'EREFDMNKGPRC', 60], ['ROFMGDDFRDKE', 'BAORMIJBJQQI', 60],
                    ['RINJLINLGJMB', 'OBLDPNJFFCAF', 42], ['HHCAGBEFFMNI', 'IHJCOJKHDIPM', 24],
                    ['ELQRCQGRPIRG', 'GRKQMQEKBQLA', 26], ['BCLBFGCBLJBL', 'FCMRLQRNDGBJ', 82],
                    ['HRJLFMFPIIAL', 'BAFJGEFQJBQC', 73], ['PRFCCDRHINCJ', 'KNMKDJENOHER', 0],
                    ['ALELOKOHEHEM', 'OEPACQLRDRQA', 44], ['JMEABDMNMILB', 'ARGIDJQHNPFQ', 22],
                    ['KRIOJEMQCEMI', 'OBACEORJRJBR', 35], ['ENOLNADNDCDM', 'GRELKMLIJBDK', 3],
                    ['QKKONBPGJMRP', 'HCOIGPJBHAJN', 57], ['GLNBKRKGCBHN', 'PFIIRJDGHRBB', 71],
                    ['PJHNRRDOFOBI', 'HBCFFILPEBBJ', 85], ['FAGBCJCHFRAD', 'HCHFNHQFRMIF', 2],
                    ['ONORMENEMRRQ', 'EENKBIJQKMKI', 17], ['ROMNJANBIDRE', 'AJGGRIIJFMCE', 90],
                    ['IPPJNKKEPLKL', 'RNHDQIJJIEAF', 59], ['LJQRPNFPDODK', 'AKGBFPRDJBPQ', 7],
                    ['POCJCRNJAHQP', 'BPBDMRDNQEHC', 6], ['FGRFRPFPJMQC', 'RPIRHOJCMKIQ', 92],
                    ['EDLQMJLEPDEI', 'CQNRMMOBHEER', 16]]

def analyze(results,roster,score):
    """
    The function will take in a list of list the roster and the score and will search for top 10 matches and search for the score which is taken in.
    Precondition :results must have at least one item and roster must in range 1 to 26 and score is a integer in th range of 1 to 100
    Input :
        results: a list of results which is in a sequence[[Team 1, Team2 ,score],[...]]
        roster: a integer that will be passed to the function
        score :  a integer which we want to search
    Return : a list of list of records which we want to search
    
    Time complexity: O(nm)= where m is the total match in the list ,n is the time complexity of calling sort function 

    Aux space complexity: O(n) total space complexity of the function call.
    """ 
    res=Radix_sort(remove_duplicate(reversed_team_score(sorting_team(results,roster))),roster)
    
    return [top10matches(res),searchMatches(res,score)]


