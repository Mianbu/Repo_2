from sys import argv

script, input_file = argv

def escribir(linea,file):
	file_w = open(file, 'w')
	file_w.write(linea)

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)#Es para comenzar el bit 0 del archivo

def print_a_line(line_count, f):
    print line_count, f.readline()#Lee hasta que encuenra un salto de linea para diferenciar lineas

linea = raw_input()
escribir(linea, input_file)

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

#rewind(current_file) 

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)