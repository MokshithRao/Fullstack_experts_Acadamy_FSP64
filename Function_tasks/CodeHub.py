print("="*30)
print("CODEHUB USER REGISTRATION")
print("="*30)
print()

# Part 1 — User Registration
full_name = input("Enter your full name: ").upper()
email = input("Enter your email: ").lower()
ph_num = input("Enter your phone number: ")
city = input("Enter your city: ").upper()
fav_tech = input("Enter your favourite technology: ")
skills = input("Enter your skills separated by comma: ")
print()


print("Processing profile...")

# Part 2 — Generate a Usernam
idx = email.find('@')
user_name = email[:idx]
# print(user_name)


# Part 4 — Skill Processing
skills = skills.split(",")
cleaned_skills =  ' |'.join(skills)


# Part 5 — Profile Card
print()
print("="*30)
print("CODEHUB PROFILE")
print("="*30)
print()


print("Name:", full_name)
print("Username:", user_name)
print("Email:", email)
print("Phone:", ph_num)
print("City:", city)
print("Technology:", fav_tech)
print("Skills:", cleaned_skills)


print("="*30)
print("PROFILE CREATED!")
print("="*30)


# Part 3 — Email Validation
print()
print("="*30)
print("EMAIL ANALYSIS")
print("="*30)
print("Email:", email)
print("Starts with user:", email.startswith(user_name))
print("Ends with .com:", email.endswith(".com"))
print("@ position:", idx)
print("Last . position:", email.rfind("."))
print("Number of dots:", email.count('.'))



# Part 6 — Developer ID
print("="*30)
print("DEVELOPER INFORMATION")
print("="*30)
first_name = full_name.split()[0]
Developer_id = (first_name + city[0] + fav_tech).upper()
print("Developer Id:", Developer_id)

Security_Key = first_name + city[-1].upper() + fav_tech
print("Security Key", Security_Key)
print()



# Part 7 — Security Check
n = "PyThOnDeVeLoPeR"
# print(n.swapcase())
#Output: pYtHoNdEvElOpEr


# # Part 8 — Case-Insensitive Technology Check
# tech = input("What technology are you learning: ").casefold()
# print(tech)

# Output:
# What technology are you learning: pYthOn
# python



# Part 9 — Find Your Name
# text_to_find = input("Enter a character or text to search in your name: ")

# first_pos = full_name.find(text_to_find)
# last_pos = full_name.rfind(text_to_find)
# total_count = full_name.count(text_to_find)

# print("\n--- Name Search Result ---")
# print("Name:", full_name)
# print("Search text:", text_to_find)
# print("First occurrence (find):", first_pos)
# print("Last occurrence (rfind):", last_pos)
# print("Number of occurrences (count):", total_count)



# Part 10 — String Literal Challenge
print("="*30)
print("WELCOME TO CODEHUB")
print("="*30)
print("Learn Python.")
print("Build APIs.")
print("Create React applications.")
print("Become a Full Stack Developer.")


