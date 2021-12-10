file = open("string.in", 'r')
b = file.read()
file.close()
otvet = ""
b = list(b)
while (len(b) > 0):
    temp = min(b)
    otvet += temp
    b.remove(temp)
file = open("string.out", 'w')
file.write(otvet)
file.close()