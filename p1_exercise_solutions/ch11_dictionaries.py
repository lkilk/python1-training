accounts = {
    1234: {
        "number": 1234,
        "name": "Smith",
        "balance": 500.0
    },
    2345: {
        "number": 2345,
        "name": "Jones", 
        "balance": -150.0
    },
    3456: {
        "number": 3456, 
        "name": "Wilson", 
        "balance": 2000.0
    },
    4567: {
        "number": 4567,
        "name": "Thompson", 
        "balance": 275.0
    },
    5678: {
        "number": 5678,
        "name": "Davis",
        "balance": 100.0
    }
}

while True:
    acc_num = input("Enter the account number: ")
    acc_num = int(acc_num)
    acc = accounts.get(acc_num)
    if acc:
        print(acc["name"], acc["balance"])
    else: 
        print("Account not found")
    more = input("More? (y/n): ")
    if more == "n":
        break

sorted_accounts = sorted(accounts.values(), key=lambda acc: acc["balance"], reverse=True)
for acc in sorted_accounts:
    print(acc["name"], acc["balance"])