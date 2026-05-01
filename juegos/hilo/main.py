from utils.mensajes import reglas_hilo

def iniciar_hilo():
    print(" Bienvenido al juego de High or Low\n")

    print(" Te cuento las reglas?")
    user_choice = input(" S/N").lower().strip()
    if user_choice == "s":
        print(reglas_hilo())
    