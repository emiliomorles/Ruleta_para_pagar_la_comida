# App Name = Ruleta para pagar la comida
Ruleta_para_pagar_la comida
names_string = input("Escribe los nombre de todas las personas, separados por una coma. \n\n")
names = names_string.split(", ")

import random

random_name = random.choice(names)
print(f"\n{random_name} pagara la cuenta hoy.")