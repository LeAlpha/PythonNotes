
# String: lowercase i qoutes
Kursusnavn = "PythonMadafaka"

# String Multiple lines:
Kursusnavn2 = """
    Kursus
    Med
    Flere
    Linjer
"""

print(Kursusnavn2)

# Print plads x i string
# String, ligesom i java, er en list af chars.

print(Kursusnavn[2])

# String : Baglæns kan også gøres, ved minus, så man starter med -1
print(Kursusnavn[-1] + "\n")


# Del string op:

print("\'"+Kursusnavn[0:3] + "\'" +
      " og resten : " + Kursusnavn[3:])
