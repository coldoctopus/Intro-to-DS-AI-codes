# x = 123
# a=[]
# while(x%10!=0):
#     a.append(x%10)
#     x = x//10
#     print(a, x)

# print(a[0])
# print(a[1:])


def isPalindrome(x):
        if (x<0):
            return False
        stack = []
        
        while(x%10!=0):
            print("Num of place: ", x%10)
            print("Current stack: ", stack)
            print("Current x: ",x)
            if((x%10) in stack):
                if(stack[len(stack)-1]!=(x%10)):
                    print("False")
                    break
                else:
                    stack.pop()
                    print("Stack's popped")
                    print(" ")
            else:
                stack.insert(-1, x%10)
                print("Stack's added")
                print(" ")
            
            x = x//10
        
        print("True")

isPalindrome(20)