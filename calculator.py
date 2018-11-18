import sys

class Calculator(object):
    def sum(self, a, b):
        val = a + b
        return val

    def mult(self, a, b):
        val = a * b
        return val

if __name__ == '__main__':
    print(Calculator().sum(int(sys.argv[1]), int(sys.argv[2])))
    print(Calculator().mult(int(sys.argv[1]), int(sys.argv[2])))
