def square(x):
    return x*x

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def main():
    name=input("what is your name?")
    print("hello,",name)
    p=Point(3,5)
    print(p.x)
    print(p.y)

if __name__=="__main__":
    main()
