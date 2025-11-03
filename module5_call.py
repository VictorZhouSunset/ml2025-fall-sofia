from module5_mod import NumDetector

N = input("Please enter a number N: ")
try:
    N = int(N)
except ValueError:
    print("N must be a positive integer")
    exit()

numDetector = NumDetector(N)
for i in range(numDetector.len):
    try:
        key = input(f"Please enter number #{i+1}: ")
        key = int(key)
    except ValueError:
        print("Input must be a number, continue to next input")
    numDetector.insert(key)

query = input("Please enter a number X to query: ")
try:
    query = int(query)
except ValueError:
    print("Query number must be an integer")
    exit()
numDetector.search(query)