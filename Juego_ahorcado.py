import random  #este modulo nos ayuda a trabajar con cosas al azar

#lista de palabras para jugar
palabras = ["python","cybersecurity","Love","mickey","dog"]

#Para elegir palabras al azar
palabra_secreta = random.choice(palabras)

#para mostrar los guiones
guiones = "_" * len(palabra_secreta)
vidas = 5 #vidas del jugador
print("Bienvenido al juego del ahorcado")
print("Palabra oculta:", " ".join(guiones))    # muestra los guines con el espacio correspondiente

#Bucle para que el jugador adivine 
while vidas > 0 and "_" in guiones:
   letra = input("Adivina una letra: ").lower()

   #para verificar que sea una sola letra
   if len(letra) != 1 or not letra.isalpha():
       print("Ingresa una sola letra")
       continue
   
   #Verificar si la letra elegida es correcta
   if letra in palabra_secreta:
     print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
     #actualizamos los guiones
     for i, l in enumerate(palabra_secreta):
        if 1 == letra:
            guiones[i] = letra

        
else:
   vidas -= 1
   print(f"La letra '{letra}' no esta en la palabra, te quedan '{vidas}' vidas")
   
   #mostramos  como vamos

   print("Palabra oculta:"," ".join(guiones))

    
     #Verificamos si gano o perdio 
if "_" not in guiones:
    print("\n¡Felicidades! Adivinaste la palabra:", palabra_secreta)
else:
    print("\nTe quedaste sin vidas. La palabra era:", palabra_secreta)



