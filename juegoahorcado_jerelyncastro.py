import random

# Lista de palabras para el juego
palabras = ["momo", "programacion", "perro", "computadora"]

# Elegimos una palabra al azar
palabra_secreta = random.choice(palabras)

# Mostramos los guiones
guiones = list("_" * len(palabra_secreta))  # Convertimos los guiones en lista para editarlos
vidas = 5  # Vidas del jugador

print("¡Bienvenido al juego del Ahorcado!")
print("Palabra oculta:", " ".join(guiones))  # Mostramos guiones con espacios

# Bucle para que el jugador adivine
while vidas > 0 and "_" in guiones:
    letra = input("\nAdivina una letra: ").lower()

    # Validamos que sea una sola letra
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingresa solo una letra.")
        continue

    # Verificamos si la letra está en la palabra
    if letra in palabra_secreta:
        print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
        # Actualizamos los guiones
        for i, l in enumerate(palabra_secreta):
            if l == letra:
                guiones[i] = letra
    else:
        vidas -= 1
        print(f"La letra '{letra}' no está en la palabra. Te quedan {vidas} vidas.")

    # Mostramos el progreso
    print("Palabra oculta:", " ".join(guiones))

# Verificamos si ganó o perdió
if "_" not in guiones:
    print("\n¡Felicidades! Adivinaste la palabra:", palabra_secreta)
else:
    print("\nTe quedaste sin vidas. La palabra era:", palabra_secreta)
