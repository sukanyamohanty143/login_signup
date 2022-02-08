import json

txt = "login and sign up"

x = txt.title()

print(x)

user1=input("Do you wants to do login or sign up>>_______")

def signup():

    detalis2={}

    details={}

    detalis_list=[]

    user_name=input("ENTER YOUR FIRSTNAME>>>_______")

    user_name2=input("ENTER YOUR SURNAME>>>________")

    mobilenumber_or_email=input("ENTER YOUR (mobile number or email address)>>>______")

    user_dob=input("ENTER YOUR DATE OF BIRTH>>>________")

    user_Gender=input("ENTER YOUR GENDER(Female/Male/Custom)>>>________")

    user_password=input("ENTER YOUR NEW PASSWORD>>>_______")

    c_l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    s_l="abcdefghijklmnopqrstuvwxyz"

    num="0123456789"

    sp_ch="@#₹&!*$%¢€£©®"

    if len(user_password)>=8:

        i=0

        var1=0

        var2=0

        var3=0

        var4=0

        while i<len(user_password):

            if user_password[i] in c_l:

                var1+=1

            elif user_password[i] in s_l:

                var2+=1

            elif user_password[i] in num:

                var3+=1

            elif user_password[i] in sp_ch:

                var4+=1

            i+=1

        if var1>=1 and var2>=1 and var3>=1 and var4>=1:

            confirm_password=input("ENTER AGAIN SAME PASSWORD>>>_______")

            if user_password==confirm_password:

                detalis2["Firstname"]=user_name

                detalis2["Surname"]=user_name2

                detalis2["Mobile or Email"]=mobilenumber_or_email

                detalis2["DOB"]=user_dob

                detalis2["Gender"]=user_Gender

                detalis2["User Password"]=user_password


                with open("userdetails.json","a+") as file:

                    json.dump(detalis2,file,indent=4)

                    detalis_list.append(detalis2)

                    details["users"]=detalis2

                print("Congrats",user_name,"Successfully Resistered👍")
                    
            else:
                print("Both Password Are Not Same")
        else:
            print("At Least Password Should Contain One Special Character And One Number")
    else:
        print("please enter 8 digit password")

def login():
    file=open("userdetails.json","r")

    var=file.read()

    email_mobilenumber=input("ENTER YOUR EMAIL ADDRESS OR MOBILE NUMBER>>>________")

    password=input("ENTER YOUR PASSWORD>>>________")

    if email_mobilenumber in var:

        if password in var:

            print("YOUR LOGIN SUCCESSFULLY👍")

        else:

            print("PLEASE ENTER CORRCCT PASSWORD🧐")

    else:

        print("Invalid Email adress or Password,Signup First")

        signup()

def login_signup():

    if user1=="signup" or user1=="sign up":

        signup()

    else:

        login()

login_signup()