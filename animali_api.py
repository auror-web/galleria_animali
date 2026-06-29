# animali_api.py — SOLUZIONE STUDENTE 1
import requests

URL_CANI  = "https://api.thedogapi.com/v1/images/search"
URL_GATTI = "https://api.thecatapi.com/v1/images/search"


def scarica_url_da_api(url_api, quante):
    """
    Funzione generica: chiama l'API con limit=quante
    e ritorna la lista degli URL delle immagini.
    """
    parametri = {"limit": quante}

    try:
        risposta = requests.get(url_api, params=parametri, timeout=10)

        if risposta.status_code == 200:
            immagini = risposta.json()
            url_list = []
            for immagine in immagini:
                url_list.append(immagine["url"])
            return url_list

        else:
            print(f"Errore API: {risposta.status_code}")
            return []

    except requests.exceptions.ConnectionError:
        print("Errore: nessuna connessione a Internet")
        return []


def scarica_url_cani(quante):
    """Scarica URL di immagini di cani."""
    return scarica_url_da_api(URL_CANI, quante)


def scarica_url_gatti(quante):
    """Scarica URL di immagini di gatti."""
    return scarica_url_da_api(URL_GATTI, quante)


if __name__ == "__main__":
    cani  = scarica_url_cani(3)
    gatti = scarica_url_gatti(3)
    print("URL cani:")
    for url in cani:
        print(" ", url)
    print("URL gatti:")
    for url in gatti:
        print(" ", url)