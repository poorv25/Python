r="rock"
p="paper"
s="scissors"
choice1=input("Enter your choice from rock, paper and scissors ")
choice2=input("Enter your choice from rock, paper and scissors ")
if choice1==r and choice2==p:
    print("user 1 wins")
elif choice1==r and choice2==s:
    print("user 1 wins")
elif choice1==r and choice2==r:
    print("Tie")
elif choice1==p and choice2==r:
    print("user 1 wins")
elif choice1==p and choice2==p:
    print("Tie")
elif choice1==p and choice2==s:
    print("User 2 wins")
    
elif choice1==s and choice2==r:
    print("user 2 wins")
elif choice1==s and choice2==p:
    print("user 1 wins")
elif choice1==s and choice2==s:
    print("Tie")
    
    
    
     
    
