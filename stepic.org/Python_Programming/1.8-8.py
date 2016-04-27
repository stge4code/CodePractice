class IntInput:
    def __init__(self, size=3):
        self.size = size
    def __iter__(self):
        return self
    def __next__(self):
        if self.size > 0:
            self.size -= 1
            return int(input())
        else:
            raise StopIteration()
def minToTime(x,h,m):
    hx = x // 60
    mx = x % 60
    H = h + hx + (mx + m) // 60
    M =  (mx + m) % 60
    return str(H) + '\n' + str(M)

(x,h,m) = IntInput(3)
print(minToTime(x,h,m))