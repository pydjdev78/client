
import rook
def ton():
    a = 4
    b = 6
    print(a + b)

if __name__ == '__main__':
    rook.start(token='499178836c84e60592d7c1f33866fa93e957b191fe5b8169192403760c6cae65', labels={"env":"dev"})
    ton()
