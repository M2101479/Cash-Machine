from menu import menu


pin="1324"
amount=2400
loop=0
attempts=3
leave=" "

while loop<3:
  check=input("What is your pin")

  if check == pin :
    
  

    menu()
    choice = int(input("Enter your choice [1-4]: "))

    while leave !="yes" or leave != "Yes:
    
 
     if choice == 1:
       print("£" ,amount)
       leave=input("Would you like to leave?")
       if leave=="Yes" or 'yes':
        break
    
     elif choice == 2:
       print ("Your withdrawal must be a multiple of 10")
       withdraw = int(input('How much do you wish to Withdraw?:'))
   
       if withdraw > amount:
         print("Insufficient funds")
         withdraw = int(input("Enter new amount to Withdraw: "))
       elif withdraw <= amount:
          balance = amount - withdraw
          print (' New Balance :', balance)
       leave=input("Would you like to leave?")
       if leave=="Yes" or 'yes':
        break
    
     elif choice == 3:
       deposit = int(input('How much do you want to Deposit?:'))
       new=amount+deposit
       print("You have choosen to deposit ",deposit,'. Your new total is £',new)
       leave=input("Would you like to leave?")
       if leave=="Yes" or 'yes':
        break
    
     elif choice== 4:
       pin=input("Enter your new pin")
       leave=input("Would you like to leave?")
       if leave=="Yes" or 'yes':
        break

     break

  else:
    loop=loop+1
    attempts=attempts-1
    print("Wrong ping.")
    if attempts>0:
      print("You have ",attempts," amount of attempts left")
    else:
      print("Your card has been locked")



