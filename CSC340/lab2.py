#return False if x^n + y^n = z^n and x,y and z are integers
#otherwise return True
def FermatTheorumFunction(x, y, n):
    z = x**n + y**n
    z = z**(1/n)
    if z.is_integer():
        return False
    else:
        return True
    
def EulersABCDTheorum(a,b,c):
    d = a**4 + b**4 + c**4
    d = d**(1/4)
    print(d)
    if d.is_integer():
        return True
    else:
        return False
def main():
    #print true if you can find x,y,z and n that make Fermat's last theorum wrong
    #otherwise print false
    print(FermatTheorumFunction(5,3,2))
    print(EulersABCDTheorum(95800, 217519,414560))
if __name__=="__main__":
    main()