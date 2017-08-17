#Rode o script com os argumentos necessários.
#Crie um arquivo de texto com u texto qualquer e coloque no mesmo diretório do script

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")
#Deleta o conteudo
print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write(" ")
target.write(line2)
target.write(" ")
target.write(line3)
target.write(" ")

print("And finally, we close it.")
target.close()
