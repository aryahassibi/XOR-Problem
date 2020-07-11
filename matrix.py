from random import uniform


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.shape = (rows, cols)
        self.data = []
        for i in range(self.rows):
            self.data.append([])
            for j in range(self.cols):
                self.data[i].append(0)

    @staticmethod
    def from_array(array):
        # turns a 1 dimensional array into a 1 dimensional Matrix
        array_length = len(array)
        result = Matrix(array_length, 1)
        for i in range(array_length):
            result.data[i][0] = array[i]
        return result

    @staticmethod
    def from_array_2d(array):
        # turns a 2 dimensional array into a 2 dimensional Matrix
        array_rows = len(array)
        array_cols = len(array[0])
        result = Matrix(array_rows, array_cols)
        for i in range(array_rows):
            for j in range(array_cols):
                result.data[i][j] = array[i][j]
        return result

    def to_array(self):
        # turns a Matrix into an Array
        result = []
        for i in range(self.rows):
            for j in range(self.cols):
                result.append(self.data[i][j])
        return result

    @staticmethod
    def subtract(a, b):

        # Subtracts each element of B form each element of A
        # A and B both should be matrices
        # also the shape of A and the shape of B should be equal

        if isinstance(a, Matrix) and isinstance(b, Matrix):
            if a.shape == b.shape:
                result = Matrix(a.rows, a.cols)
                for i in range(a.rows):
                    for j in range(a.cols):
                        result.data[i][j] = a.data[i][j] - b.data[i][j]
                return result
        else:
            print("!!! Inputs should be instances of Matrix")
            return None

    def multiply(self, n):

        # If N is a Matrix it will multiply  each element of your matrix by corresponding element in N
        # Note: the shape of N and the shape of your matrix should be the same

        if isinstance(n, Matrix):
            if self.shape == n.shape:
                for i in range(self.rows):
                    for j in range(self.cols):
                        self.data[i][j] *= n.data[i][j]

        # If N is a number then your matrix will be multiplied by N
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] *= n

    @staticmethod
    def product(a, b):
        # Returns the dot product of two matrices
        # A and B both should be matrices
        # Th number of columns of A should be same as the number B rows

        if isinstance(a, Matrix) and isinstance(b, Matrix):
            if a.cols == b.rows:
                result = Matrix(a.rows, b.cols)
                for i in range(result.rows):
                    for j in range(result.cols):
                        temp_sum = 0
                        for k in range(a.cols):
                            temp_sum += a.data[i][k] * b.data[k][j]
                        result.data[i][j] = temp_sum
                return result
            else:
                print("!!! Columns of first matrix must match row of the second matrix")
                return None

    def add(self, n):
        # If N is a Matrix it adds each element of your matrix by corresponding element in N
        # Note: the shape of N and the shape of your matrix should be the same
        if isinstance(n, Matrix):
            if self.shape == n.shape:
                for i in range(self.rows):
                    for j in range(self.cols):
                        self.data[i][j] += n.data[i][j]
        # If N is a number then it adds N to each element of your matrix
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += n

    def map_function(self, func):
        # applies given function to each element of your matrix
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.data[i][j]
                self.data[i][j] = func(val)

    @staticmethod
    def map_function_static(mat, func):
        # applies given function to each element of the given matrix
        result = Matrix(mat.rows, mat.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                val = mat.data[i][j]
                result.data[i][j] = func(val)
        return result

    @staticmethod
    def transpose(mat):
        # transposes the given matrix
        # in other words it Reverses the axes of the given matrix
        result = Matrix(mat.cols, mat.rows)
        for i in range(mat.rows):
            for j in range(mat.cols):
                result.data[j][i] = mat.data[i][j]
        return result

    def randomize(self):
        # initializes you matrix with random numbers between -1 and 1
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = uniform(-1, 1)
