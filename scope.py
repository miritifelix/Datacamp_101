#defineing num at global scope
num = 5

def func1():
    """defining num in local scope"""
    num = 3
    print(num)

def func2():
    """definging num again"""
    #calling global num
    global num
    double_num = num * 2
    num = 6
    print(double_num)

#func1 returns 3
#func2 returns 10
func1()
func2()
#global can be used to change the value of variable in the global scope
#value of num has been changed
print(num)