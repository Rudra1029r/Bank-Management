
import json

def load_data():
    try:
        with open('BANK_SYSTEM.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []   

def save_bank_data(account):
    with open('BANK_SYSTEM.txt','w') as file:
        json.dump(account,file)


def lst_all_account(account):
    print("\n")
    print("-" * 70)
    for index, acc in enumerate(account, start=1):
        print(f"{index}. {acc['name']}, Age: {acc['age']},Mobile_Number: {acc['mobile_num']} ")
    
    print("-" * 70)


def new_account(account):
    print("-" * 70)
    name = input("Enter your FullName: ")
    age = int(input("Enter your Correct Age: "))
    mobile_num = int(input("Enter Your Mobile Number: "))
    account.append({'name': name, 'age': age,'mobile_num':mobile_num})
    print("-" * 70)
    print("\n")
    print("THANK YOU ! YOUR ACCOUNT IS CREATED")
    print("-" * 70)
    save_bank_data(account)

def update_detail(account):
    print("-" * 70)
    lst_all_account(account)
    idx = int(input("Enter your Account to Add New Details: "))
    if 1 <= idx <= len(account):
        name = input("Enter your FullName: ")
        age = int(input("Enter your Correct Age: "))
        mobile_num = int(input("Enter Your Mobile Number: "))
        account[idx-1] ={'name': name, 'age': age,'mobile_num':mobile_num}
        print("-" * 70)
        print("\n")
        print("THANK YOU ! YOUR ACCOUNT IS UPDATED")
        print("-" * 70)
        save_bank_data(account)         

def delete_account(account):
    print("-" * 70)
    lst_all_account(account)
    idx = int(input("Enter Your Account Number To Be Deleted: "))
    if 1 <= idx <= len(account):
        del account[idx-1]
        save_bank_data(account)
    else :
        print("You Enter Invalid Index Number")
        print("-" * 70)


def main():
    account = load_data()
    while True:
        print("\n Welcome to Bank Management App")
        print("1. List All Account")
        print("2. Create a New Account")
        print("3. Update Bank Account Details")
        print("4. Delete your Bank Account")
        print("5. Exit App")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                lst_all_account(account)
            case 2:
                new_account(account)    
            case 3:
                update_detail(account)
            case 4:
                delete_account(account)    
            case 5:
                break
            case _:
                print("Invalid Choice")   


if __name__ == "__main__":
    main()