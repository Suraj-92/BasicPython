username = input("Enter the Username: ")
a = len(username)

if (a > 3) :
    print("Username is valid")
    b = "Hello <<username>> How are you?"
    c = b.replace("<<username>>", username)
    print(c)
else:
    print("Invalid Username")

print("Done")
