#include <stdio.h> 
#include<string.h>

int main() { 
int i,j,n,k; 
char str[100],temp[100]; 
scanf("%s",str);  
n=strlen(str);
j=n/2; 
k=0; 
while(str[j]!='\0'){ 
temp[k++]=str[j++];
} 
j=0; 
while(k<n){ 
temp[k++]=str[j++]; 
}

for(i=0;i<n;i++){ 
for(j=0;j<n-i-1;j++){ 
printf(" ");
} 
for(k=0;k<i+1;k++){ 
printf("%c",temp[k]); 
}
printf("\n");
}
    return 0;
}
