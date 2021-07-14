/*****************************************************************
            Solving FeruLock Using Breadth-First Search

            [Run Guide] 
                1. g++ 16.cpp
                2. cat tests.txt | ./a.out 
 *****************************************************************/

#include <iostream>
#include <queue>

using std::queue;


int AvailableButtons[10];



int BFS_UnlockLock(int L, int U, int R)
{
    std::queue <int> frontier;
    int explored[10000] = {0};

    // add current lock code to queue
    frontier.push(L); 
    explored[L]++; 
 
    // while there exists a node in the queue for expansion do :
    while( !frontier.empty() ){

        // pop oldest node in the queue for expansion (First-in First-out)
        int parent = frontier.front(); 
        frontier.pop();

        //late goal test (before expansion)
        if (parent == U) 
            return explored[parent] - 1;
        else {
            //expand node
            for (int i = 0; i < R; ++ i) {
                //generate a child 
                int child = (parent + AvailableButtons[i]) % 10000;

                //if child is not in explored list do:
                if (!explored[child]) {
                    // set value of child in explored list to its parents count plus 1 (another move occured) and push child into queue
                    explored[child] = explored[parent] + 1;
                    frontier.push(child);
                }
            }
        }
    }
    //if answer not found, then return -1
    return -1;
}

int main()
{
    int L;
    int U;
    int R;
    int cnt = 0;

    while (1){

        int minPressCnt;

        scanf("%d%d%d", &L, &U, &R);

        if (L==0 && U==0 && R==0)
            break;
        
        for (int i = 0; i < R; i++) 
            scanf("%d", &AvailableButtons[i]);

        cnt ++;

        minPressCnt = BFS_UnlockLock(L,U,R);

        if (minPressCnt == -1)
            printf("Case %d: Permanently Locked\n",cnt );
        else
            printf("Case %d: %d\n",cnt,minPressCnt );

    }

}
