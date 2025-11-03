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