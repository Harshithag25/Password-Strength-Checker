import string
class PasswordStrengthChecker:
    def strength(self,s):
        lower=False
        upper=False
        digit=False
        special=False
        for i in s:
            if i.isupper()==True:
                upper=True
            elif i.islower()==True:
                lower=True
            elif i.isdigit()==True:
                digit=True
            elif i in string.punctuation:
                special=True
        if len(s)<8:
            return "Invalid password"
        if (lower==True and upper==True and digit==True and special==True):
            print("Your password is Strong")
        elif (digit):
            print("Your password is of Medium Strength")
        else:
            print("Your password is Weak")
        print("Thank You")
print("------Password Strength Checker------")
print("The constraints are: 1.Length of password is 8 2.Contain upper characters 3.Contain lower characters 4.Contains digits 5.Contains special symbols")
p=input("Enter your Password: ")
check=PasswordStrengthChecker()
result=check.strength(p)
#print(result)