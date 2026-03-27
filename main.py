import time
import os
expenses = []

#functions
def load():
 
 load_data = []
 if os.path.exists("expenses.txt"):

   with open("expenses.txt","r")as f:
      for line in f:
         parts = line.strip().split(",")
         if len(parts) == 3:
          expense_name = parts[0]
          amount = float(parts[1])
          date = parts[2]
          load_data.append({"expense":expense_name , "amount":amount, "date": date})

   #finished updating time 

 return load_data



def save(expenses):
   try:
    with open("expenses.txt","w")as f:
      for data in expenses:
         f.write(f"{data['expense']},{data['amount']},{data['date']}\n")
    return
   except Exception as e:
     print("error :",e)

 #finished updating time

def addexp(expenses):
  date = time.strftime("%Y-%m-%d")
  while True:
    
    try :
     key = input(" expense name : ")
     if not key:
        print("-----empty details!! please fill in--------\n ")
        continue 
     

     amount = float(input(" amount spent : "))
     if amount <= 0:
         print("-----empty details!! please fill in--------\n ")
         continue
     expenses.append({"expense":key,"amount":amount, "date": date })
     print("loading......")
     time.sleep(1.0)
     save(expenses)
     print("succefully added........\n")
     return
    except ValueError:
       print(" please enter correct value type") 

 # finished updating time 



def view_all(expenses):
    min_name= expenses[0]['expense']
    min_amt= expenses[0]['amount']

    max_name= expenses[0]['expense']
    max_amt= expenses[0]['amount']
    total_spent = 0

    if not expenses:
       time.sleep(0.4)
       print("-----------no data filled yet!--------------")
       return
    time.sleep(0.2)

    for data in expenses:
        print(f"{data['expense']} | ₹{data['amount']} | {data['date']}")
        c_name = data['expense']
        c_amt = data['amount']
        total_spent += c_amt

        if c_amt > max_amt:
          max_name = c_name
          max_amt = c_amt

        if c_amt < min_amt:
          min_name = c_name
          min_amt = c_amt  


    print("\n")    
    print(f"your cummulative total money spent is ₹{total_spent}\n")
    print(f"your most costly expense was ₹{max_amt}, spent on : {max_name}")
    print(f"your least coslty expense was ₹{min_amt}, spent on : {min_name}\n")
    return


# finished time


def view_today():
  total_amount = 0
  flag = 0
  today = time.strftime("%Y-%m-%d")
  print(f"------------TODAY'S EXPENSES, THE DATE TODAY IS {today}-------------------------")
  if os.path.exists("expenses.txt"):
    try:
     with open("expenses.txt","r") as f:
      for line in f :
        parts = line.strip().split(",")
        if len(parts)== 3 and parts[2] == today  :
         
          flag += 1
          total_amount += float(parts[1])
          print(f"{parts[0]} |  ₹{parts[1]} |  {parts[2]}\n")

             
      if  flag > 0:
        print(f"today's total amount is ₹{total_amount}") 
      else :  
        print("nothing added today")     
    except Exception as e:
      print("Error")
  else:
    print(" file not found!!")
    return
  
  
#main program
expenses = load()
print("-------------------this is denzel's first ever project--the espense tracker appv1--------------------------")
while True:
    print("-------------------choose any options using numbers--------------------------")
    print("1.add new expense")
    print("2.show all expenses")
    print("3.show today's expenses")
    print("4.exit\n")
    print("---------------please enter numbers as options-------------------")
    try:
     a = int(input())
     
     if( a<1 or a>4):
       print(" ----------------only enter options from 1 t0 4---------------")

     if a == 1 :
        print("--------adding new expense-------------\n")
        addexp(expenses)
        print("--------successfully added------")    
     elif a == 2 :
        view_all(expenses)
     elif a == 3:
       view_today()
   
     elif a == 4:
      print("byeeeeeeeeee!")
      exit()    
    except ValueError:
       print("thats not a number enter a proper number") 
