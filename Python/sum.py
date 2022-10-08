def sum(lst, n):
    # Your code here!
    sum = 0
    for i in range(len(lst)):
      sum += lst[i]
    return sum == n

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()
