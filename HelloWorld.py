global a
a = 0


def b():
    global a
    a += 1

if __name__ == '__main__':
    print a
    b()
    print a
