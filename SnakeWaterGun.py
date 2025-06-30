#### Snake Water Gun ####
import random
print("WELCOME TO Snake,Water,Gun Game...")
print("choose \nS for Snake \nW for Water \nG for Gun")
char=['S','W','G']
i=1
user_count=0
cmp_count=0
while i<6:
    print("user:",end="")
    user=input()
    cmp=random.choice(char)
    print("computer:",cmp)
    
    if user=='S' and cmp=='W':
        print("User Win..")
        user_count+=1
    elif user=='W' and cmp=='S':
        print("Computer Win")
        cmp_count+=1
    elif user=='W' and cmp=='G':
        print("User Win")
        user_count+=1
    elif user=='G' and cmp=='W':
        print("Comuter Win")
        cmp_count+=1
    elif user=='G' and cmp=='S':
        print("User Win")
        user_count+=1
    elif user=='S' and cmp=='G':
        print("Computer Win")
        cmp_count+=1
    else:
        print("Tie")
    print("------------------")
    i+=1
    
print("User Score:",user_count)
print("Computer Score:",cmp_count)
print("--------------------")
if user_count>cmp_count:
    print("Congrats..! Your are win")
else:
    print("Computer Win..! Try Next Time")



    


