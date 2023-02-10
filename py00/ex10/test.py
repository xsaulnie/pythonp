from loading import ft_progress

X = range(100, 200)

def test_X(X):
    for elem in ft_progress(X):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
