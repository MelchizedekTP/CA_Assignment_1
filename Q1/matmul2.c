#include <stdio.h>
#include <stdlib.h>


#define ROWS 4096
#define COLS 4096


int main() {
    
    

    float **mat1,**mat2,**mat3;

    mat1 = (float **)malloc(ROWS * sizeof(float *));
    mat2 = (float **)malloc(ROWS * sizeof(float *));
    mat3 = (float **)malloc(ROWS * sizeof(float *));

    for (int i = 0; i < ROWS; i++) 
        {
        mat1[i] = (float *)malloc(COLS * sizeof(float));	  
    	mat2[i] = (float *)malloc(COLS * sizeof(float));
    	mat3[i] = (float *)malloc(COLS * sizeof(float));
    	}
    
    
    
    for (int i=0;i<ROWS;i++)
    	for(int j=0;j<COLS;j++)
    		{
    		mat1[i][j]=ROWS*i+j*0.1;
    		mat3[i][j]=0;
    		
    		}
    
    for (int i=0;i<ROWS;i++)
    	for(int j=0;j<COLS;j++)
    		mat2[i][j]=ROWS*i+j*0.1;
    	 	
    
    int i,j,k,N=400;
    
    for(k=0;k<N;k++)
	for(i=0; i<N; i++)
		for(j=0; j<N; j++){
 			{
			mat3[i][j]=mat3[i][j]+mat1[i][k]*mat2[k][j];
			}
 		
 		} 
   return 0;
}
