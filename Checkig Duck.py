def isDuck(num):
    if num == 0:
        return False
    else:
        while num > 0:
            if num % 10 == 0:
                return True
            num = num // 10
    return False
isDuck(1024)
