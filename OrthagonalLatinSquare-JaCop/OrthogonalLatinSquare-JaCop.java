/*------------------------------------------------------

Elaheh Toulabi Nejad  |  9631243

[+] RUN GUIDE :
    java -cp ".:./jacop-4.8.0.jar" OrthogonalLatinSquare-JaCop.java  

--------------------------------------------------------*/

import org.jacop.constraints.*;
import org.jacop.core.*;
import org.jacop.search.*;
import java.util.*;


class CommandLineExample
{
    public static IntVar[] getColumn(Object[][] array, int index,int n){
        Store store = new Store();
        IntVar[] column = new IntVar [n];  
        for(int i=0; i< n; i++){
            column[i] = new IntVar(store, "column"+i, 1, n);   
        }
        return column;
    }

    public static void main ( String [] arguments )
    {   
        Scanner sc= new Scanner(System.in);    
        System.out.print("Enter n : ");  
        int n= sc.nextInt();  

        Store store = new Store();

       // Variables :
        IntVar[][] A = new IntVar[n][n]; 
        for (int i=0; i<n; i++) 
            for (int j=0; j<n; j++)
                A[i][j] = new IntVar(store, "A"+i+j, 1, n); 

        IntVar[][] B = new IntVar[n][n]; 
        for (int i=0; i<n; i++) 
            for (int j=0; j<n; j++)
                B[i][j] = new IntVar(store, "B"+i+j, 1, n); 

        //Constraints:

        for (int i=0;i<n;i++)
            store.impose(new Alldifferent(A[i]));

        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                for (int k=0; k<n; k++){

                    if ( k != j)
                        store.impose(new XneqY(A[j][i],A[k][i]));
                }
            }
        }

        
        
        for (int i=0;i<n;i++)
            store.impose(new Alldifferent(B[i]));

        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                for (int k=0; k<n; k++){

                    if ( k != j)
                        store.impose(new XneqY(B[j][i],B[k][i]));
                }
            }
        }

        for (int i=0; i<n; i++) 
            for (int j=0; j<n; j++)
                store.impose(new XneqY(A[i][j],B[i][j]));


        ArrayList<IntVar> list = new ArrayList<IntVar>();
         IntVar[] v = new IntVar [2*n*n];
        for (int i=0; i<n; i++) 
            for (int j=0; j<n; j++){
                list.add(A[i][j]);
                list.add(B[i][j]);
            }
        list.toArray(v);

  
        
        Search<IntVar> label = new DepthFirstSearch<IntVar>(); 
        SelectChoicePoint<IntVar> select = 
                    new InputOrderSelect<IntVar>(store, 
                                        v, new IndomainMin<IntVar>()); 
        label.getSolutionListener().recordSolutions(true);
        label.setPrintInfo(false);
        boolean result = label.labeling(store, select);
        // for (int i=1; i<=label.getSolutionListener().solutionsNo(); i++){  
            for (int j=0; j<label.getSolution(1).length; j++){ 
               System.out.print(label.getSolution(1)[j]); 
               System.out.print(" ");

               if( (j+1) % (2*n) ==0)
                    System.out.println(); 
            }
            System.out.println(); 
        // }

    }
}