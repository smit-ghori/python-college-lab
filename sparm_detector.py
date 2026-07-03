# h1) The Spam Detector (Search in Stream) – Linear Search
# A cybersecurity intern at a startup is building a basic spam filter. 
# Incoming emails are checked against a blacklist of known spam sender IDs. 
# The blacklist has no order.

# Question:
# Write a program to search for a given sender ID in the blacklist using Linear Search. 
# Print whether the sender is found or not.

block_ids = [
    "xyz@gmail.com",
    "litter@yahoo.com",
    "spam12@gmail.com",
    "position@gmail.com"
]

incoming_emails = [
    "smit@gmail.com",
    "xyz@gmail.com",
    "position@gmail.com",
    "krihsna@gmail.com"
]

for incoming in incoming_emails:
    found = False
    
    for block_id in block_ids:
        if incoming == block_id:
            found = True
            break
    if found:
        print(f"{incoming} is spam")
    else:
        print(f"{incoming} is spam free")