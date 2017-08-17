#Rode o script com os argumentos necessários.
#Crie um arquivo de texto com u texto qualquer e coloque no mesmo diretório do script
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Typen the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
