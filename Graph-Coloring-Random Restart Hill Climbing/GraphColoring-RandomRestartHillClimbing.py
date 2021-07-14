import numpy as np



def _evaluate(AdjacencyMatrix,coloring):

    well_colored = 1
    result = 0
    for i in range(0,coloring.shape[1]):
        neighbors  = AdjacencyMatrix[i,:]
        for j in range (0,len(neighbors)):
            if neighbors[j] == 1 and coloring[0][i] == coloring[0][j]:
                well_colored = 0
    
    if well_colored == 0:
        result= np.Inf
    else:
        result=len(np.unique(coloring))
    
    return result

def _bestNeighbor(AdjacencyMatrix,coloring,vertexCnt):
    best_neighbor = np.zeros((1,vertexCnt))
    best_val = np.Inf

    for i in range(0,coloring.shape[1]):
        for j in range (1,vertexCnt+1):
            cur_neighbor = np.zeros((1,vertexCnt))
            cur_val = np.Inf
            cur_neighbor[0,:i]=coloring[0,:i]
            cur_neighbor[0,i]=j
            cur_neighbor[0,i+1:]=coloring[0,i+1:]
            cur_val = _evaluate(AdjacencyMatrix,cur_neighbor)
            if cur_val < best_val:
                best_val = cur_val
                best_neighbor[:,:]=cur_neighbor[:,:]
    
            
    return best_neighbor,best_val

def random_restart_hill_climbing(AdjacencyMatrix,vertexCnt,edgeCnt,r):
    random_restart = 30#12
    max_nonimproving = 8#8#15
    current_best   = np.zeros((1,vertexCnt))
    best_successor =  np.zeros((1,vertexCnt))
    solution =  np.zeros((1,vertexCnt))
    for i in range(vertexCnt):
        # current_best[0,i]=i+1
        # best_successor[0,i]=i+1
        solution[0,i]=i+1

    solution_val   = vertexCnt
    cur_best_val   = vertexCnt
    best_sucsr_val = vertexCnt
    start = 0
    step = 0
    while start < random_restart :
        step = 0
        current_best = np.random.randint(1,vertexCnt+1,(1,vertexCnt))
        cur_best_val = _evaluate(AdjacencyMatrix,current_best)
        
        while step < max_nonimproving:
            best_successor,best_sucsr_val=_bestNeighbor(AdjacencyMatrix,current_best,vertexCnt)
            if best_sucsr_val < cur_best_val:
                cur_best_val = best_sucsr_val
                current_best[:,:]=best_successor[:,:]
                step = 0
            else:
                step = step + 1
       
        start = start + 1
        
        if best_sucsr_val < solution_val:
            solution[:,:]=best_successor[:,:]
            solution_val = best_sucsr_val
        
        # print('restart:',start,'val=',best_sucsr_val,'=>',solution_val)

    return solution , solution_val

def main():

    vertexCnt = 0
    edgeCnt = 0

   
    wordNo = 0  
    path = input("Enter File Path >>  ")
    with open(path,'r') as file: 
        for line in file:   
            for word in line.split():
                if wordNo == 0: 
                    vertexCnt = int(word)
                    wordNo = wordNo + 1
                elif wordNo == 1:
                    edgeCnt = int(word)
                    wordNo = wordNo + 1
        
     
    AdjacencyMatrix =np.zeros((vertexCnt,vertexCnt))        
    clauseNo = -1
    with open('testCase.txt','r') as file: 
        for line in file:   
            if(clauseNo == -1):
                pass
            else:
                temp=[]
                for word in line.split():
                    if word != 'e':
                        temp.append(word)   
                AdjacencyMatrix[int(temp[0])-1,int(temp[1])-1]=1
                AdjacencyMatrix[int(temp[1])-1,int(temp[0])-1]=1
            clauseNo = clauseNo + 1
  
    bestColoring , minColors=random_restart_hill_climbing(AdjacencyMatrix,vertexCnt,edgeCnt,10)

    print(minColors)
    
    u = np.unique(bestColoring)
    
    for i in range(0,bestColoring.shape[1]):
        for j in range (0,u.shape[0]):
            if bestColoring[0,i] == u[j]:
                bestColoring[0,i]=j+1
                # print(i+1,' ', bestColoring[0,i])
    
    for i in range(0,bestColoring.shape[1]):
        print(i+1,' ', int(bestColoring[0,i]))


main()