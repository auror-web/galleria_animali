import os

def crea_cartella(percorso):

    gia_esistente = os.path.exists(percorso)
    os.makedirs(percorso, exist_ok=True)

    if gia_esistente:
        print(f"Cartella già esistente: {percorso}")
    else:
        print(f"Cartella cartella: {percorso}")

def elenca_immagini(cartella):
    all_file = os.listdir(cartella)
    immagini = []

    for nome_file in all_file:
        nome_lower = nome_file.lower()

        if nome_lower.endswith(".jpg"):
            immagini.append(nome_file)
        elif nome_lower.endswith(".jpeg"):
            immagini.append(nome_file)
        elif nome_lower.endswith(".png"):
            immagini.append(nome_file)

    print(f"Trovate {len(immagini)} immagini in {cartella}")
    return immagini

if __name__ == "__main__":
    crea_cartella("test_cartella")
    crea_cartella("test_cartella")

    with open("test_cartella/foto.jpg", "wb") as f:
        f.write(b"")
    with open("test_cartella/nota.txt", "w") as f:
        f.write("non un immagine")

    immagini = elenca_immagini("test_cartella")
    print("Immagini trovate:", immagini)