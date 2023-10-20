#This function computes x^3+8
#Calling a function- getting it(note for me)
def CalcCubedFunc(y):   #this identifies that calcubedfunc is a function, and the function requires an int argument  
    fun= y**3+8
    return(fun)    


#After you def a main function, or use an if statement, or a for loop, you need a colon
def main():
    x = float(input('Enter a float value for x: '))
    cubedFun_val= CalcCubedFunc(x)
    print(cubedFun_val)
    if cubedFun_val>27:
        print('YAY!')


if __name__=="__main__":
    main()

