import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNN_REGR:
    def __init__(self, k: int = 0):
        self.k = k
        self.X_train = []
        self.Y_train = []
        self.np_X_train = None
        self.np_Y_train = None
        self.data_changed = False
    
    def add_train_data(self, x: float, y: float):
        self.X_train.append(x) # Faster than nparray's append because it is O(1)
        self.Y_train.append(y)
        self.data_changed = True
    
    def train(self, k: int | None = None):
        if self.data_changed:
            self.np_X_train = np.array(self.X_train).reshape(-1, 1)
            self.np_Y_train = np.array(self.Y_train)
            self.data_changed = False
        if k is not None:
            self.k = k # Last chance to change k
        if self.k == 0:
            print("Error: kNN's k can not be 0.")
            return
        if self.k > len(self.np_X_train):
            print("Error: k is bigger than the length of the whole dataset.")
            return
        self.model = KNeighborsRegressor(n_neighbors=self.k)
        self.model.fit(self.np_X_train, self.np_Y_train)
        
    def pred(self, x: float) -> float | None:
        return self.model.predict(np.array([[x]])).item()


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
    
    knn.train()
    test_output = knn.pred(test_input)
    print(f"Using the {knn.k}-NN regression, the predicted label of the test input x_test = {test_input} is {test_output}.")

if __name__ == "__main__":
    main()
