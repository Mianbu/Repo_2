i = 0
numbers = []

val = raw_input(" ")

while i < int(val):
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
    print num
	
print numbers#Se puede imprimir una lista sin ciclos