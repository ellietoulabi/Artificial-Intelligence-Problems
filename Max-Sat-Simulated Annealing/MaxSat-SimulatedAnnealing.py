import numpy as np
from random import SystemRandom
import numpy.random as rn
import matplotlib.pyplot as plt  # to plot
import matplotlib as mpl

# costs= []


def _evaluate(state,clauses,clauseCnt,variableCnt):
    
    satisfiedCnt = 0
    for i in range(0,clauseCnt):
        value = bool(0) 
        for j in range (0,variableCnt):
            if clauses[i,j] == 0:
                value = value
            elif clauses[i,j] == 1:
                value = value | bool(state[0,j])
            elif clauses[i,j] == -1:
                value = value | bool(~ state[0,j])

        satisfiedCnt = satisfiedCnt + int(value)
    return satisfiedCnt

def _neighborGenetaror(state,variableCnt):
    neighbor = np.zeros((1,variableCnt))
    neighbor[0,0:variableCnt] = state[0,0:variableCnt]
    position = np.random.randint (variableCnt)
    if neighbor[0,position] == True:
        neighbor[0,position]  = False
    else:
        neighbor[0,position] =True

    return neighbor

def _probablity(deltaE,temperature):
    # print('p:',np.exp(-deltaE / temperature))
    return np.exp(-deltaE / temperature)
               
def _temperatureScheduler(temperature):
    # return max(0.01, min(1, 1 - fraction))
    return temperature * 0.85
    

def _SA_Solver(clauses,clauseCnt,variableCnt):
   
    rnd = SystemRandom()
    temperature = 100
    max_step = 100
    step = 1
    current_state = np.random.choice([0,1], size=(1,variableCnt))
    next_state = np.zeros((1,variableCnt))
    A = _evaluate(current_state,clauses,clauseCnt,variableCnt)
    A_prim = 0
    while (step <= max_step) and (A != clauseCnt) and (temperature > 0.001):
        
        temperature = _temperatureScheduler(temperature) 
        next_state  = _neighborGenetaror(current_state,variableCnt)
        A_prim      = _evaluate(next_state,clauses,clauseCnt,variableCnt)
        deltaE      = A - A_prim
        # print('step(',step,') A=',A,' Aprim=',A_prim,' T=',temperature)
        if deltaE < 0 :
            current_state = next_state
            A = A_prim
            # costs.append(A)
        else:
            x = rn.random() 
            # print('x:',x)
            if x  < _probablity(deltaE,temperature):
                current_state = next_state
                A = A_prim
                # costs.append(A)

        step = step + 1

    return current_state , A



def main():
    
    variableCnt = 0
    clauseCnt = 0
    
    
    wordNo = 0  
    path = input('Enter File Path >>  ')
    with open(path,'r') as file: 
        for line in file:   
            for word in line.split():
                if wordNo == 0: 
                    variableCnt = int(word)
                    wordNo = wordNo + 1
                elif wordNo == 1:
                    clauseCnt = int(word)
                    wordNo = wordNo + 1
        
        
    clauses =np.zeros((clauseCnt,variableCnt))        
    clauseNo = -1
    with open('testCase.txt','r') as file: 
        for line in file:   
            if(clauseNo == -1):
                pass
            else:
                for word in line.split():
                    if int(word)!=0:
                        clauses[clauseNo,abs(int(word))-1] = bool(int(word)/abs(int(word)))       
                    
            clauseNo = clauseNo + 1
   
 
    values , satisfiedCount = _SA_Solver(clauses,clauseCnt,variableCnt)
    print(satisfiedCount)

    for i in range(0,variableCnt):
        print('X',i+1,' = ',int(values[0][i]))
    
    # plt.figure()
    # plt.plot(costs, 'r')
    # plt.title("Graph")
    # plt.show()

main()


