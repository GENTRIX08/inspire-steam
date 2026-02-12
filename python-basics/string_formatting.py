# Gentrix Anyango
# 2/12/2026
# string formatting

# Get string length
sentence = "I watch anime"

string_length = len(sentence)

print(f"The length is: {string_length}")

# Splitting a string
sentence_2 = "Mathematics physics"
split = sentence_2.split(" ")

print(f"the first subject is: ", split[0])
# Make everything CAPS
mpesa_code = "ub5555"

capitalised = mpesa_code.upper()

print("New mpesa code: ", capitalised)

# Make everything lower case
mpesa_code = "TRTRTR32"

lowercase = mpesa_code.lower()

print("New mpesa code: ", lowercase)

# Replacing characters in a string

balance = "100Kes"
amount_added = "50Kes"

cleaned_balance = balance.replace("Kes", "")

print("Cleaned balance: ", cleaned_balance)

cleaned_amount_added = amount_added.replace("Kes", "")

print("Cleaned amount added: ", cleaned_amount_added)

# Gentrix answer
new_balance = int(cleaned_balance) + int(cleaned_amount_added)

print(f"The new balance is:", new_balance)

#Assignment
mpesa_message = "CONFIRMED you have received 40Kes from philip"

split1 = mpesa_message.split(" ")
print(mpesa_message)
print("The amount is: ", split1[4])

