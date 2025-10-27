from typing import List

N = input("Please enter a number N: ")
try:
    N = int(N)
except ValueError:
    print("N must be a positive integer")
    exit()
if not N > 0:
    print("N must be a positive integer")
    exit()

input_dict = {}
for i in range(N):
    try:
        key = input(f"Please enter number #{i+1}: ")
        key = int(key)
    except ValueError:
        print("Input must be a number, continue to next input")
        continue
    if key not in input_dict:
        input_dict[key] = [i]
    else:
        input_dict[key].append(i)

query = input("Please enter a number X to query: ")
try:
    query = int(query)
except ValueError:
    print("Query number must be an integer")
    exit()
if query in input_dict:
    for v in input_dict[query]:
        print(v+1, end=" ")
else:
    print(-1)
