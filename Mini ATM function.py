j=1
while j==1:
    notfound=True
    d={'SAIF':"mikey3098", 'SRI PRASATH':'dumboy123', 'Rakshmi':"rakshmi@123",'SARVESHWARAN':"sarveshwaran@123",
       'BEEMA':"beema@123",'HARINI PRIYA':"harinipriya@123",'LAYANOTOFFICIAL':"laya@123",
       'RAJAKOHILA':"rajakohila@123",'ARAVINDAN':"aravindan@123"}
    username=input('Enter your username (ALL CAPS):   ')
    password=input('Enter your password:  ')
    for i in d:
        if username==i and password==d[i]:
           print ("Successful login! Welcome", username)
           notfound=False
           break
    if notfound==True:
        print('Sorry! Your username does not exist or Your password is wrong.')
    while notfound==False:
       print ("Welcome to JD ATM",username," : \nPlease choose a function by typing the number beside them \n 1.Deposit\n 2.Withdraw \n 3.Check balance \n 4.Exit")
       a=int(input('Choose your function:    '))  
       while a==1 or a==2 or a==3 or a==4:
                  if a==1:
                     deposit=float(input('Enter the amount you want to deposit:   '))
                     print('The amount has been deposited',username)
                     print('\n')
                     break
                  elif a==2:
                      Withdraw=float(input('Enter amount to withdraw:   '))
                      print('Please collect your cash',username)
                      print('\n')
                      break
                  elif a==3:
                      Balance= len(username)
                      print(username, "Your balance is : ",Balance *18408+ 10000)
                      print('\n')
                      break
                  elif a==4:
                      print("Thank you for choosing JD ATM \n See you later!")
                      print('\n')
                      break
       break
