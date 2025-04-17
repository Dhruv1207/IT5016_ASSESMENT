student_id = input("Enter Student ID: ")
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

message = "I am a newbie in Whitecliff college!"

if "Whitecliff" in message and "college" in message:

    personal_code = student_id[:2] + last_name[:3]
    print(f"Personal Code: {personal_code}")
else:
    print("Message does not contain the required words.")