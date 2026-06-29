import os
import requests


def scarica_immagine(url, percorso):
    """
    Scarica un'immagine e la salva in percorso.
    Ritorna True se ok, False se errore.
    """
    try:
        risposta = requests.get(url, timeout=15)

        if risposta.status_code == 200:
            with open(percorso, "wb") as f:
                f.write(risposta.content)

            dimensione_kb = len(risposta.content) / 1024
            print(f"  Salvato: {percorso} ({dimensione_kb:.1f} KB)")
            return True

        else:
            print(f"  Errore HTTP {risposta.status_code}: {url}")
            return False

    except requests.exceptions.ConnectionError:
        print(f"  Errore connessione: {url}")
        return False


def scarica_tutte(url_list, cartella, prefisso):
    """
    Scarica tutte le immagini in url_list.
    I file vengono nominati: prefisso_1.ext, prefisso_2.ext, ...
    """
    salvate = 0

    for numero, url in enumerate(url_list, start=1):
        estensione = url.split(".")[-1]
        nome_file  = prefisso + "_" + str(numero) + "." + estensione
        percorso   = os.path.join(cartella, nome_file)

        successo = scarica_immagine(url, percorso)
        if successo:
            salvate = salvate + 1

    print(f"  {salvate}/{len(url_list)} immagini salvate")
    return salvate