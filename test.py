from pythonds.basic import Stack


def postfixevl(posfixevlion):
    Emptystack = Stack()
    tokenlist = posfixevlion.split()


    for token in tokenlist:
        if token in "0123456789":
            Emptystack.push(int(token))

        else:
            operand2 = Emptystack.pop()
            operand1 = Emptystack.pop()
            result = domath(token,operand1,operand2)
            Emptystack.push(result)

    return Emptystack.pop()

def domath(op,op1,op2):
    if op == '+':
        return op1+op2
    
    elif op == '-':
        return op1-op2
    
    elif op =='*':
        return op1*op2
    
    else :
      return op1/op2

res = postfixevl('7 7 + 4 3 + /')
print(res)      