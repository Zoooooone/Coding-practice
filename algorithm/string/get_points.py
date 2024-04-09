# simulation
def minimumDaysToGetPoints_naive(a, b, n):
    ans = 0
    point = a

    def containSeven(num):
        while num:
            digit = num % 10
            if digit == 7:
                return True
            num //= 10
        return False

    while point < n:
        ans += 1
        if containSeven(ans):
            point += b
        point += a

    return ans


# advanced simulation
def minimumDaysToGetPoints(a, b, n):
    def daysContainSeven(scope):
        if scope == 1:
            return 0
        return daysContainSeven(scope // 10) * 9 + scope // 10
    
    ans = 0
    point = a
    scopes = [daysContainSeven(scope) for scope in [10 ** n for n in range(10)]]  # [0, 1, 19, 271, 3439, 40951, 468559, 5217031, 56953279, 612579511]
    pointer = len(str(n // a)) - 1

    while pointer >= 0:
        digit = 0
        while point < n:
            ans += 10 ** pointer
            digit += 1
            if digit != 7:
                point += 10 ** pointer * a + scopes[pointer] * b
            else:
                point += 10 ** pointer * a + 10 ** pointer * b
        if digit != 7:
            point -= 10 ** pointer * a + scopes[pointer] * b
        else:
            point -= 10 ** pointer * a + 10 ** pointer * b
        if not pointer:
            return ans
        ans -= 10 ** pointer
        pointer -= 1


if __name__ == "__main__":
    for a in range(1, 5):
        for b in range(5, 10):
            naive = minimumDaysToGetPoints_naive(a, b, 1000)
            advanced = minimumDaysToGetPoints(a, b, 1000)
            if naive != advanced:
                print(f"a = {a}, b = {b}, naive = {naive}, advanced = {advanced}")
