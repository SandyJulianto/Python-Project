# Email Slicer
ser_email = input("Enter your email : ")

split_email = []

for i in user_email.split("@"):
    split_email.append(i)

print("Your email name is {} and your domain is {}".format(split_email[0], split_email[-1]))
