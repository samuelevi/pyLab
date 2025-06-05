###save money
customer_name : str = 'James'
customer_acc = '1234567890'
bal : float = 0.0
def save_money(cust_name : str , cust_acc : str , amount : float = 0.0):
   global bal
   if (cust_name == customer_name) and (cust_acc == customer_acc):
      bal = bal + amount
      print(f'Mr/Mrs {customer_name} you have deposited {amount}')
   else:
      print('Check your details!!!')


def check_bal( cust_acc : str ) -> float :
   if customer_acc == cust_acc:
      return bal
   else:
      return 'Check your details!!!'
   
def withdraw_money(cust_name : str , cust_acc : str , amount : float):
   global bal
   if (cust_name == customer_name) and (cust_acc == customer_acc):
      if amount < check_bal(customer_acc):
         bal = bal - amount
         return amount
      else:
         return 'insufficient balance'
   else:
      print('Check your details!!!')

save_money('James' , '1234567890')
save_money('James' , '1234567890' , 5000)
save_money('James' , '1234567890' , 3000)
save_money('James' , '1234567890' , 500)
withdraw_money('James' , '1234567890' , 500)
print(withdraw_money('James' , '1234567890' , 50000))
print(check_bal('1234567890'))