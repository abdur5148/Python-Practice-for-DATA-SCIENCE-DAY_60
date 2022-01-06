def div(n):
    for i in range(n+1):
        if i % 35 == 0:
            yield i


n = int(input("Enter Number : "))
var = []
for i in div(n):
    var.append(str(i))
print(",".join(var))
