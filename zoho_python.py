
'''Input : W E L C O M E
Explanation : start with middle letter from first line. Next line two letter from middle . Continue still you print all letters in last line. Then start with the first letter and continue for the remaining letters. 
  
output :  


                     C
                 C O
              C O M
           C O M E
       C O M E W
   C O M E W E
C O M E W E L'''
#python code
string=input().strip()
lent=len(string)
answer=[]
for i in range(lent):
    answer.append(" ")
half=lent//2
#answer[0]=string[half]
for i in range(lent):
    if half==lent:
        half=0
    answer.insert(0,string[half])
    answer.pop()
    half+=1
    print("".join(answer[::-1]))
#using slicing operator
'''
s=input().strip()  
length=len(s)
l=s[length//2:]+s[:length//2]
for i in range(len(l)): 
    print(' '*(length-i-1)+l[:i+1])'''
    