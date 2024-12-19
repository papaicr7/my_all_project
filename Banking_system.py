def balance_enquery(balance):
  print(f'Your balance is ${balance:.2f}')


def deposit():
  amount = float(input("Enter the amount to be deposited $"))
  if amount<0:
    print("invalid amount")
    return 0
  else:
    return amount


def withdraw(balance):
  amount = float(input("Enter the amount to be withdraw $"))
  if amount<0:
    print("invalid amount")
    return 0
  elif amount>balance:
    print("insufficient balance")
    return 0
  else:
    return amount
    
def transfer(balance):
  amount = float(input("Enter the amount to be transfer $"))
  if amount<0:
    print("invalid amount")
    return 0
  elif amount>balance:
    print("insufficient balance")
    return 0
  else:
    receiver_name = str(input("Enter the receiver name: "))
    receiver_account_number = int(input("Enter the receiver account number : "))
    receiver_IFSC_code = str(input("Enter the receiver IFSC code : "))
    
    print(f'The transfer amount ${amount} to Mrs/miss {receiver_name} and Account number is {receiver_account_number}, IFSC code {receiver_IFSC_code}')
    print(f'The remaining balance is')
    balance_enquery(balance)
    return amount



def main():

  balance = 0
  is_running = True


  while is_running:
    print("#######################")
    print(" The Banking Solution")
    print("#######################")
    print("1. balance enquery")
    print("2. deposit")
    print("3. withdraw")
    print("4. transfer")
    print("5. exit")
    print("#######################")
    choice = input("enter your choice (1 - 5):")
    print("######################################")
    if choice == '1':
      balance_enquery(balance)
    elif choice == '2':
      balance +=deposit() 
    elif choice == '3':
      balance -= withdraw(balance)
    elif choice == '4':
      balance -=transfer(balance)
    elif choice == '5':
      is_running = False
    else:
      print("invalid choice")

  print("########################################")
  print("Thank you for using our banking system")
  print("########################################")


if __name__ == "__main__":
  main()