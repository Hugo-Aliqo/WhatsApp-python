import webbrowser
from urllib.parse import quote
import re

# Mettez le nom du contact puis son numéro de téléphone puis mettez une virgule s'il n'est pas le dernier contact#
# Exemple:"Jimmy": 33640475021 #

contacts = {
    "Adrien": 3364047502,
    "James": 33789208219
        
}

def envoyer_message():
    message = input("Ecris ton message ici: ")
    personne = input("A qui veux-tu envoyer ce message?: ")

    if personne not in contacts:
        print("Contact inconnu.")
        return

    numero_tel = str(contacts[personne])
    cleaned = re.sub(r"[^\d]", "", numero_tel)

    if not cleaned:
        raise ValueError("Numéro invalide.")

    url = f"https://wa.me/{cleaned}"
    if message:
        url += f"?text={quote(message)}"

    print(f"Ouverture de : {url}")
    webbrowser.open(url)


recommencer = "Y"

print(f"Voici la liste de tes contacts : {', '.join(contacts)}")
while recommencer == "Y":
    envoyer_message()
    recommencer = input("Veux-tu envoyer un autre message ? Y/n: ")
