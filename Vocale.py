
# Funktion zur Zählung der Vokale
def count_characters(text):
    characters = {"A":0,"E":0,"I":0,"O":0,"U":0,"a":0,"e":0,"i":0,"o":0,"u":0}
    for character in text:
        for vocal in characters.keys():
            if character == vocal:
                characters[vocal] += 1
                #!print("Mein Charcter ist :",character, "::: Mein Vacal ist: ",vocal) Debugging
            else:
                continue
                 
    total_count = sum(characters.values())    
    uppercase_count = sum(value for key, value in characters.items() if key.isupper())
    lowercase_count = sum(value for key, value in characters.items() if key.islower())

    print(f"Du hast insgesamt {uppercase_count} Vokale in Großbuchstaben und {lowercase_count} Vokale in Kleinbuchstaben eingegeben.") 
    print(f"Das sind insgesamt {total_count} Vokale.")
    print("Detaillierte Vokalhäufigkeit:")
    for character, count in characters.items():
        print(f"Der Buchstabe {character} kommt {count} mal vor.")
            
    return characters, uppercase_count, lowercase_count, total_count

while True:
    # Eingabe vom Benutzer
    text = input("Geben Sie den Text ein (oder Ende zum Beenden): ").strip()

    # Beendigungsabfrage direkt nach der Eingabe
    if text.lower() == "ende":
        print("Programm wird beendet.")
        break

    # Leere Eingabe prüfen
    if not text:  # Leere Eingabe
        print("Leere Eingabe ist nicht erlaubt. Bitte erneut eingeben.")
        continue  # Zur nächsten Iteration springen

    # Funktion ausführen
    count_characters(text)