counter = 1000

def id_generator():
    global counter
    id = counter+1
    return id

def make_request():
    name = input("enter name")
    project = input("enter th project name")
    amount = int(input("donation amount"))
    id = id_generator()

    return name,project,amount,id
#d = make_request()
#print(d)
for i in range(2):
    print("make_request")

def donation_details():
    details = {}
    num = int(input('how many items are you providing'))

    for i in range(num):
        items = input("enter item name")
        price = int(input("enter the price"))
        details[items] = price

    total = 0
    for price in details.values():
        total = total+price
        return total

e = donation_details()
print(e)

def decision():
    priority = ()
    status = ()
    name,project_name,amount,id = make_request()


    approvel_id = ''
    if 'family' in project_name:
        priority = "high"
        status = "approved"
        new_id = str(id)
        approval_id = new_id+name[-2:]
        return name,project_name,priority,status,approval_id
y = decision()
print(y)