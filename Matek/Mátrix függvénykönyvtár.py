def check_depth(elements, depth):
        if depth == 1:
            if type(elements) is int:
                return True
            return False
        ok = True
        if type(elements) is not list:
            return False
        for i in elements:
            ok &= check_depth(i, depth-1)
        return ok

class Matrix:
    def __init__(self, elements, depth):
        print(check_depth(elements, depth))
        if not check_depth(elements, depth):
            raise ValueError("Hibás mélység, vagy adatok")
        self.e = elements
        self.elements = elements
        self.d = depth
        self.depth = depth
    def determine(self):
        if self.d == 1:
            return self.e
        elif self.d == 2:
            return 0
        elif self.d == 3:
            neg = 0
            poz = 0
            temp = 1
            e = self.e
            l = len(e)
            for i in range(len(e)):
                for j in range(len(e)):
                    temp *= e[]
                
        else:
            pass

def main():
    m = Matrix(1,1)
    m2 = Matrix([0,1],2)
main()
        
        
