def li():
    for a in range(1,11):
        yield a
if __name__=='__main__':
    l=[a for a in li()]
    print(l)
    a=li()
    print(next(a))

    
