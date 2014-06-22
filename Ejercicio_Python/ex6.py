x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
yes = "yes"
y = "Those who know %s and those who %s %s" % (binary, do_not, yes)
#Se deben poner el mismo numero de variables % que entre los parentesis
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
a = "Angela"
b = "Angelo"

print a > b#Comparación alfabetica

c = 'D_D'*10#Repetir una cadena el numero de veces
print c