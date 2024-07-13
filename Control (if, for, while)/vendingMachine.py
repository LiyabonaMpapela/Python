#simulate a vending machine and calculate change based on the amount paid
#Liyabona Mpapela
#24 August 2022
cost = eval(input("Enter the cost (in cents):\n"))
deposit = eval(input("Deposit a coin or note (in cents):\n"))
while deposit<cost: #checks if the cost is less than deposit
    deposit2 =eval( input("Deposit a coin or note (in cents):\n"))# if the deposit is less than the cost the user should add another the amount of cost
    deposit= deposit+deposit2# adds the new cost added to the previous one
    
if cost!=deposit:
    change_in_rands= (deposit-cost)//100 # calculates the change and converts cents to rands
    change_in_cents=(deposit-cost)%100
    print('Your change is:')
    
    if (change_in_rands//5)>0:# checks if the change consists if any 5 rands 
        R5 = change_in_rands//5#checks the number of 5 rands in the change
        change_in_rands = change_in_rands-(5*R5)# removes the 5 rands from the change if any
        print(int(R5),"x R5");# shows the number of 5 rands in the change
    if (change_in_rands//2)>0:# checks if the change consists if any 2 rands after the 5 rands have been removed
        R2 = change_in_rands//2#checks the number of 2 rands in the change
        change_in_rands = change_in_rands-(2*R2)# removes the 2 rands from the change if any
        print(int(R2),"x R2");# shows the number of 2 rands in the change
    if (change_in_rands//1)>0:#checks if the change consists if any 1 rands after the 5 rands and 2 rands have been removed
        R1 = change_in_rands//1#checks the number of 1 rands in the change
        change_in_rands = change_in_rands-(1*R1)# removes the 1 rands from the change if any
        print(int(R1),"x R1");# shows the number of 1 rands in the change
    if (change_in_cents//50)>0:#checks if the change consists if any 50 cents after the 5,2 and 1rands have been removed
        R0_5 = change_in_cents//50#checks the number of 50 cents in the change
        change_in_cents = change_in_cents-(50*R0_5)# removes the 50 cents from the change if any
        print(int(R0_5),"x 50c");# shows the number of 50 cents in the change
    if (change_in_cents//20)>0:#checks if the change consists if any 20 cents after the 5,2,1 rands and 50 cents have been remove
        R0_2 = change_in_cents//20#checks the number of 20 cents in the change
        change_in_cents = change_in_cents-(20*R0_2)# shows the number of 20 cents in the change
        print(int(R0_2),"x 20c");# removes the 20 cents from the change if any
    if (change_in_cents//10)>0:#checks if the change consists if any 10 cents after the 5,2,1 rands and 50 and 20 cents have been removed
        R0_1 = change_in_cents//10#checks the number of 10 cents in the change
        change_in_cents = change_in_cents-(10*R0_1)# removes the 10 cents from the change if any
        print(int(R0_1),"x 10c");# removes the 10 cents from the change if any
    if (change_in_cents//5)>0:#checks if the change consists if any 5 cents after the 5,2,1 rands and 50,20 and 10 cents have been removed
        R0_05 = change_in_cents//5#checks the number of 5 cents in the change
        print(int(R0_05),"x 5c");# removes the 5 cents from the change if any