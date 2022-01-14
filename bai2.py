print("câu a")
a ='Việt'
b= len ('cường')
c=len(a)
print(a)
print("câu b")
def totalDigitsOfNumber(n):
    total = 0
    while (n > 0):
        total = total + n % 10
        n = int(n / 10)
    return total
n = int(45)
print("Tổng các chữ số của", n, "là", totalDigitsOfNumber(n))

