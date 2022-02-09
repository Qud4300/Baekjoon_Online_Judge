# BOJ 1747 소수&팰린드롬

def sieve(a,b):
    temp = [i for i in range(b+1)]
    temp[1] = 0
    for i in range(2, b+1):
        if temp[i]:
            for j in range(i+i, b+1, i):
                temp[j] = 0
    return [i for i in temp[a:b+1] if i != 0]


def isPalindrome(a:str):
    for i in range(len(a)//2):
        if a[i] != a[-1-i]:
            return False
    return True


def findPalindrome(a:list):
    for i in a:
        if isPalindrome(i):
            return i
    return None


n = int(input())
arr = [*map(str, sieve(n, 1003001))]  # 1003001 is the least prime-palindrome number over 1M.
print(findPalindrome(arr))
