import numpy as np

class KNN_REGR:
    def __init__(self, k: int = 0):
        self.k = k
        self.X_train = np.array([])
        self.Y_train = np.array([])
    
    def add_train_data(self, x: float, y: float):
        self.X_train = np.append(self.X_train, x)
        self.Y_train = np.append(self.Y_train, y)
    
    def _ln_distance(self, X_train: np.ndarray, x: float) -> np.ndarray:
        return np.abs(X_train - x)
    
    def pred(self, x: float, k: int | None = None) -> float | None:
        if k is not None:
            self.k = k # Last chance to change k
        if self.k == 0:
            print("Error: kNN's k can not be 0.")
            return
        if self.k > len(self.X_train):
            print("Error: k is bigger than the length of the whole dataset.")
            return
        
        dists = self._ln_distance(self.X_train, x)
        neighbor_idx = np.argsort(dists)[:self.k]
        neighbor_average = np.mean(self.Y_train[neighbor_idx])
        
        return neighbor_average


def main():
    N = input("Please enter a positive number N: ")
    try:
        N = int(N)
    except ValueError:
        print("N must be a positive integer.")
        exit()

    k = input("Please enter a positive number k: ")
    try:
        k = int(k)
    except ValueError:
        print("k must be a positive integer.")
        exit()

    knn = KNN_REGR(k=k)
    for i in range(N):
        x = input(f"Please enter training data x_{i+1}: ")
        try:
            x = float(x)
        except ValueError:
            print("x must be a float number.")
            exit()

        y = input(f"Please enter training label y_{i+1}: ")
        try:
            y = float(y)
        except ValueError:
            print("y must be a float number.")
            exit()
        
        knn.add_train_data(x, y)
    
    test_input = input("Please enter the test input x_test: ")
    try:
        test_input = float(test_input)
    except ValueError:
        print("test_input must be a float number.")
        exit()
    
    test_output = knn.pred(test_input)
    print(f"Using the {knn.k}-NN regression, the predicted label of the test input x_test = {test_input} is {test_output}.")

if __name__ == "__main__":
    main()
