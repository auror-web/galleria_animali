# animali_galleria.py — SOLUZIONE STUDENTE 4
import os


def ordina_alfabeticamente(file_list):
    """
    Ritorna la lista di nomi file ordinata alfabeticamente.
    """
    lista_ordinata = sorted(file_list)
    print(f"File da visualizzare: {len(lista_ordinata)}")
    return lista_ordinata


def stampa_galleria(file_list, cartella):
    """
    Stampa la galleria in ordine alfabetico con percorso e dimensione.
    """
    print()
    print("╔══════════════════════════════════════════╗")
    print("║         🐾 GALLERIA ANIMALI 🐾           ║")
    print("╚══════════════════════════════════════════╝")
    print()

    for numero, nome_file in enumerate(file_list, start=1):
        percorso       = os.path.join(cartella, nome_file)
        dimensione_byte = os.path.getsize(percorso)
        dimensione_kb  = dimensione_byte / 1024

        print(
            f"[{numero:<2}] {nome_file:<20}"
            f"→ {percorso:<40}"
            f"({dimensione_kb:.1f} KB)"
        )

    print()
    print(f"Totale: {len(file_list)} immagini in {cartella}")


if __name__ == "__main__":
    os.makedirs("test_galleria", exist_ok=True)
    nomi = ["gatto_1.jpg", "cane_2.jpg", "cane_1.jpg", "gatto_2.png"]
    for nome in nomi:
        with open(os.path.join("test_galleria", nome), "wb") as f:
            f.write(b"x" * 1024)
    ordinati = ordina_alfabeticamente(nomi)
    stampa_galleria(ordinati, "test_galleria")