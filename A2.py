# # # r=1
# # # while r<=5:
# # #     c=1
# # #     while c<=r:
# # #         print("*",end='')
# # #         c+=1
# # #     print()
# # #     r=r+1

# # # n=4
# # # i=1
# # # while i<=n:
# # #     print(n-1,"-",i,"*")
# # #     i+=1
    
# # from random import randint
# # def win():
# #     print ('You win!')
# # def lose():
# #     print ('You lose!') 
# # while True:
# #     player_choice = input('What do you pick? (rock, paper, scissors): ')
# #     player_choice.strip()
# #     random_move = randint(0, 2)
# #     moves = ['rock', 'paper', 'scissors']
# #     computer_choice = moves[random_move]
# #     if player_choice ==computer_choice:
# #         print ('Draw!')
# #     elif player_choice=='rock' and computer_choice == 'scissors':
# #             win()
# #     elif player_choice == 'paper' and computer_choice == 'scissors':
# #             lose()
# #     elif player_choice == 'scissors' and computer_choice == 'paper':
# #             win()
# #     elif player_choice == 'scissors' and computer_choice== 'rock':
# #             lose()
# #     elif player_choice == 'paper' and computer_choice == 'rock':
# #             win()
# #     elif player_choice=='rock' and computer_choice=='scissor':
# #             lose()
# #     again = input('Do you want to play again? (y or n)').strip()
# #     if again=="n":
# #         break
    
# def fun():
# 	print("welcome to our ATM home")
# 	print("please insart your card")
# 	l=int(input("please enter your language 1.hindi, 2.english::"))
# 	if l==1:
# 		print("Hindi")
# 	elif l==2:
# 		print("English")
# 	pincode=1234
# 	p=int(input("please enter your pin code no.4 of 4 digit::"))
# 	if p>=1000 and p<9999:
# 		print("**")
# 	t=int(input("please select the____transaction::1.cashwithdrawl  2.balance 	inquary  3. diposite  4.fast cash  5.			tranfer  6.pin change::"))
# 	if t==1:
# 		print("cash withdrawl")
# 	elif t==2:
# 		TA=100000000
# 		print("balance inquary=",TA)
# 	elif t==3:
# 		print("diposit")	
# 	elif t==4:
# 		print("fast cash")
# 	elif t==5:
# 		a="another account"
# 		print("transfer= ",a)
# 	elif t==6:
# 		p="enter your pin"
# 		print("pin change=",p)
# 	A=int(input("please select your account: 1.From corrent account, 2.From saving account::"))
# 	if A==1:
# 		print("From corrent account")
# 	if A==2:
# 		print("From saving account")
# 	m=int(input("please enter your amount::"))
# 	if m>=100:
# 		print("take you recieved in amount")
# 	else:
# 		print("you can not bewlo the 100 ")	
# 	total=100000000
# 	balance=total-m
# 	print("total your balance=",balance)
# 	print("Thank you for use of ATM card")
# fun()   
    
# class Flower:
#     attr1 = "Flowwer"
#     def __init__(self , name):
#         self.name = name
        
# Rodger = Flower("Rodger")
# Lotus = Flower("Lotus")
# print("Rodger is a {}".format(Rodger.__class__.attr1))
# print("Lotus is also a {}" .format(Lotus.__class__.attr1))
# print("my name is {}" .format(Rodger.name))
# print("my name is {}" .format(Lotus .name))   
    
import random
test_list =[1,4,5,6,3]
print("The original list is : " + str(test_list))  
for i in range(len(test_list)-1, 0, -1):
    j = random.randint(0, i +-1,)

    
    
    
    
    
    
    
    
    
    
    
    
    
    