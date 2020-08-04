class CircleIter:
    def __init__(self, sequence, number_of_times):
        self.times = number_of_times
        self.sequence = sequence

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter >= self.times:
            raise StopIteration
        self.counter += 1
        if self.counter == (len(self.sequence)):
            self.times -= len(self.sequence)
            self.counter = 0
        return self.sequence[self.counter-1]


for x in CircleIter([1, 2], 5):
    print(x, end=" ")
print()

for x in CircleIter([1, 2, 3], 4):
    print(x, end=" ")
    for y in CircleIter([5, 6], 3):
        print(y, end=" ")
    print()
