import random

# Task 1: Capture requester details and generate unique request ID
def capture_donation_request():
    requester_name = input("Enter the requester's name: ")
    project_name = input("Enter the project name: ")

    # Generate a unique request ID (e.g., a random 4-digit number)
    request_id = str(random.randint(1000, 9999))

    return request_id, requester_name, project_name

# Task 2: Capture request items and calculate total value
def capture_request_items_and_calculate_total():
    total_amount = 0

    print("Enter requested items and their prices.")
    print("Type 'done' when finished.")

    while True:
        item_name = input("Item name: ")
        if item_name.lower() == 'done':
            break
        try:
            item_price = float(input("Item price: $"))
            total_amount += item_price
        except ValueError:
            print("Invalid price. Please enter a number.")

    return total_amount

# Task 3: Approval decision based on project name and total amount
def approval_decision(request_id, requester_name, project_name, total_amount):
    if "Family" in project_name:
        priority = "High"
        status = "Approved"
        approval_id = request_id + requester_name[-2:]
    elif total_amount < 500:
        priority = "Medium"
        status = "Approved"
        approval_id = request_id + requester_name[:2]
    else:
        priority = "Low"
        status = "Pending"
        approval_id = "N/A"

    return status, priority, approval_id

# Task 4: Display all the output details
def display_output(request_id, requester_name, project_name, total_amount, status, priority, approval_id):
    print("Donation Request Summary")
    print(f"Request ID: {request_id}")
    print(f"Requester Name: {requester_name}")
    print(f"Project Name: {project_name}")
    print(f"Total Amount Requested: ${total_amount:.2f}")
    print(f"Approval Status: {status}")
    print(f"Priority Level: {priority}")
    if approval_id != "N/A":
        print(f"Approval ID: {approval_id}")
    else:
        print("Approval ID: Not generated (Pending approval)")

# Main function to run the whole process
def main():
    print("NGO Donation Request System")

    # Task 1
    request_id, requester_name, project_name = capture_donation_request()

    # Task 2
    total_amount = capture_request_items_and_calculate_total()

    # Task 3
    status, priority, approval_id = approval_decision(request_id, requester_name, project_name, total_amount)

    # Task 4
    display_output(request_id, requester_name, project_name, total_amount, status, priority, approval_id)

# Run the program
main()