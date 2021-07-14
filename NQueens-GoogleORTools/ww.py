# from ortools.constraint_solver import pywrapcp
from ortools.sat.python import cp_model

def n_queens_solver(N):
    
    solver = cp_model.CpSolver()
    model = cp_model.CpModel()
    # model.NewIntVar(0, num_vals - 1, 'x')
    queens = [model.NewIntVar(0, N - 1, 'q%i' % i)for i in range(N)]

    model.AddAllDifferent(queens)

    # x []= queens[i] + i for i in range(N) ;
    # for i in range(0,N-1):

    # model.AddAllDifferent()
    # model.AddAllDifferent([queens[i] + i for i in range(N)])
    # model.AddAllDifferent([queens[i] - i for i in range(N)])

    for i in range(0,N):
        for j in range(0,N):
            if j != i:
                model.Add(queens[i]-i != queens[j]-j)

    for i in range(0,N):
        for j in range(0,N):
            if j != i:
                model.Add(queens[i]+i != queens[j]+j)      

    result = solver.Solve(model)
   
    if result == cp_model.OPTIMAL or result == cp_model.FEASIBLE :
        for i in range(0,N):
            print(solver.Value(queens[i]) + 1,i+1)
    else:
        print('Solution Result Is Not Feasible OR Optimal')
     
        


if __name__ == '__main__':

    n = int(input("Enter n :"))
    n_queens_solver(n)