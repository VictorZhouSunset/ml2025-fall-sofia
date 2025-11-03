class NumDetector:
    def __init__(self, len: int):
        self.len = len
        self.idx_dict = {} # Faster than storing a list
        self.ptr = 1
    
    def insert(self, num: int):
        if num not in self.idx_dict:
            self.idx_dict[num] = [self.ptr]
        else:
            self.idx_dict[num].append(self.ptr)
        self.ptr += 1
    
    def search(self, target: int):
        if target not in self.idx_dict:
            print(-1)
        else:
            for v in self.idx_dict[target]:
                print(v, end=" ")

def main():
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

if __name__ == "__main__":
    main()