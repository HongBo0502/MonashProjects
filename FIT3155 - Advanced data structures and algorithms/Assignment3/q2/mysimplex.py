"""
Name Kang Hong Bo
Student ID: 32684673

"""

import numpy as np
def lin_pro(Cj,matrix,init_coef,decision_var):
    Cj=np.array(Cj)
    np_matrix=np.array(matrix,dtype=float)
    # print(np_matrix)
    Zj=np.matmul(init_coef,np_matrix)
    Cj_Zj=Cj-Zj[:len(Cj)]
    find_max_index=np.argmax(Cj_Zj)
    decision_lst=[None]*decision_var
    with np.errstate(divide='ignore'):
        theta=np_matrix[:,-1]/np_matrix[:,find_max_index]
    theta[theta<=0]=np.inf
    positive_min_theta_index=np.argmin(theta)
    
    
    
    # print(find_max_index)
    # print(theta)
    # print(Cj_Zj)
    # print(positive_min_theta_index)
    while Cj_Zj[find_max_index]>0:
        
        divisor=np_matrix[positive_min_theta_index,find_max_index]
        # print(divisor)
        np_matrix[positive_min_theta_index]=np_matrix[positive_min_theta_index]/divisor
        init_coef[positive_min_theta_index]=Cj[find_max_index]
        # init_coef[positive_min_theta_index]=init_coef[positive_min_theta_index]/divisor
        
                    
        for i in range(len(np_matrix)):
            if i!=positive_min_theta_index:
                np_matrix[i]=np_matrix[i]-np_matrix[i,find_max_index]*np_matrix[positive_min_theta_index]
        if find_max_index in range(decision_var):
            decision_lst[find_max_index]=(np_matrix[positive_min_theta_index,-1],positive_min_theta_index)
            for i in range (len(decision_lst)):
                if decision_lst[i] is not None:
                    decision_lst[i]=(np_matrix[decision_lst[i][1],-1],decision_lst[i][1])
        else :
            for i in range (len(decision_lst)):
                    decision_lst[i]=(np_matrix[decision_lst[i][1],-1],decision_lst[i][1])
        # print(np_matrix)      
        Zj=np.matmul(init_coef,np_matrix)
        Cj_Zj=Cj-Zj[:len(Cj)]
        find_max_index=np.argmax(Cj_Zj)
        # print(find_max_index)
        with np.errstate(divide='ignore'):
            theta=np_matrix[:,-1]/np_matrix[:,find_max_index]
        theta[theta<=0]=np.inf
        positive_min_theta_index=np.argmin(theta)
        
        # print("Theta"+str(theta))
        # print(init_coef)
        
        # print(positive_min_theta_index,theta[positive_min_theta_index])
        # print(Zj)
        # print(Cj_Zj)
        # print(decision_lst)
        # print("\n")
    decision=[]
    for i in range(len(decision_lst)):
        if decision_lst[i] is not None:
            decision.append(decision_lst[i][0])
        else:
            decision.append(0)
    Z=Zj[-1]
    # print(decision)
    # print(Z)
    return decision,Z
import sys
if __name__=='__main__':
    _,info_file=sys.argv
    text_file=open(info_file,"r")
    lines=text_file.readlines()
    # print(lines)
    text_file.close()
    numDecVac=int(lines[1].split()[0])
    numConstraints=int(lines[3].split()[0])
    free=[0]*(numConstraints)
    Cj=[int(i) for i in lines[5].split(',')]+free
    matrix=[[None]]*(numConstraints)
    init_coef=np.zeros(numConstraints)
    for i in range(numConstraints):
        matrix[i]=[int(i) for i in lines[7+i].split(',')]+free
        matrix[i][i+numDecVac]=1
        matrix[i].append(int(lines[7+numConstraints+1+i].split()[0]))

    # print(matrix)
    resD,resO=lin_pro(Cj,matrix,init_coef,numDecVac)
    text_file=open("lpsolution.txt","w")
    text_file.write("# optimalDecisions\n")
    for i in range(len(resD)):
        if i != len(resD)-1:
            text_file.write(str(resD[i])+", ")
        else:
            text_file.write(str(resD[i])+"\n")
    text_file.write("# optimalObjective\n")
    text_file.write(str(resO)+"\n")
    text_file.close()
    