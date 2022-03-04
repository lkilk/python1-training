import re

file_contents = """
1234 Credit:
David Smith,500.0
2345 Debit:
Sarah Jones,-150.0
3456 Credit:
Tom Wilson,2000.0
4567 Savings:
Jane Thompson,275.0
5678 Debit:
Simon Davis,100.0
"""

accounts = {}
pattern = "(\d{4}) \w+:\n\w+ (\w+),(.+)"
#pattern = "(\d{4})\s\w+:\s\w+\s(\w+),(.+)"

matches = re.findall(pattern, file_contents)
print(matches)
# for number, name, balance in matches:
#     accounts[number] = {
#         "number": int(number),
#         "name": name,
#         "balance": float(balance)
#     }

# for acc in accounts.values():
#     print(acc)