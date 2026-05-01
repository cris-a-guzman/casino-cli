from juegos.prueba.prueba import prueba
from juegos.hilo.main import iniciar_hilo

print("Bienvenido al casino virtual\n")

juegos = {
    "1": ("Prueba", prueba),
    "2": ("High-Low", iniciar_hilo)
}

def listar_juegos():
    print("\n🎮 Juegos disponibles:\n")
    for key, (nombre, _) in juegos.items():
        print(f"{key} - {nombre}")
    print()


def elegir_juego():
    while True:
        user_choice = input("Ingresa el número del juego: ")

        if not user_choice.isdigit():
            print("❌ Lo ingresado no es un número\n")
            continue

        if user_choice not in juegos:
            print(f"❌ No existe el juego '{user_choice}'\n")
            continue

        return juegos[user_choice][1]  # devuelve la función

# 🔁 Loop principal
while True:
    listar_juegos()
    juego = elegir_juego()
    print()
    juego()  # ejecuta el juego