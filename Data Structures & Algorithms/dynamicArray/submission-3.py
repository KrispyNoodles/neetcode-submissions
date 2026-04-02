class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [0]*self.capacity

    def get(self, i: int) -> int:

        if i < self.size:
            return self.array[i]
        else:
            return null

    def set(self, i: int, n: int) -> None:
        
        # reassiginign
        self.array[i] = n

    def pushback(self, n: int) -> None:

        # if len same as capacity, double capacity
        if self.size == self.capacity:
            self.resize()

        # adding a value to the end based on the size of the array rather then at the end end [-1]
        self.array[self.size] = n

        # increase size
        self.size += 1

    def popback(self) -> int:
        # retrieve the last value of the array
        last_val = self.array[self.size-1]

        # reassogm to 0
        self.array[self.size-1] = 0

        # reduce size
        self.size -= 1
        
        return last_val

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        
        # creating a new array
        new_array = [0]*self.capacity

        for index in range(self.size):
            new_array[index] = self.array[index]

        self.array = new_array[:]

    def getSize(self) -> int:

        return self.size
    
    def getCapacity(self) -> int:

        return self.capacity
