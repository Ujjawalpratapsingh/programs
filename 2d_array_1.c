#include<stdio.h>
int main(){
    int row =3,col=4,i,j,row2=3,col2=4;
    float element;
    float arr[row][col];
    float arr2[row2][col2];
    printf("enter the elements of array one by one \n");
    for(i =0 ;i<row;i++){
        for(j=0;j<col;j++){
            printf("enter element [%d][%d] :",i+1,j+1);
            scanf("%f",&element);
            arr[i][j]=element;
        }
    }
    for(i=0;i<row;i++){
        for(j=0;j<col;j++){
            printf("%.2f",arr[i][j]);
        }
        printf("\n");
    }
    printf("enter the elements of array 2 one by one \n");
    for(i =0 ;i<row2;i++){
        for(j=0;j<col2;j++){
            printf("enter element [%d][%d] :",i+1,j+1);
            scanf("%f",&element);
            arr[i][j]=element;
        }
    }
    for(i=0;i<row2;i++){
        for(j=0;j<col2;j++){
            printf("%.2f",arr[i][j]);
        }
        printf("\n");
    }
    return 0;
    }