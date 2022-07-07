# Email Slicer
# Input email
ser_email = input("Enter your email : ")

# Create new list
split_email = []

# Split the email by "@"
for i in user_email.split("@"):
    # Add i to split_email
    split_email.append(i)

print("Your email name is {} and your domain is {}".format(split_email[0], split_email[-1]))
