def curriedAdd():
    total = 0
    def add(num = None):
        nonlocal total
        if num == None: return total
        total += num
        return add
    return add

firstAdder = curriedAdd()
print(firstAdder(2)(8)(5)(1)())
