from pathlib import Path
import hashlib

# Ordnerpfad
home = Path("C:\\Users\\HartmanM\\OneDrive - Berufsförderungswerk Köln gGmbH\\Dokumente\\Testdaten\\pathlib")

# Dictionary für die Ergebnisse
docs = {}
duplicates = {}

# Über Dateien im Ordner iterieren
if home.exists() and home.is_dir():
    for doc in home.iterdir():
        # Nur Dateien berücksichtigen
        if doc.is_file():
            # Dateiinhalt lesen und Hash berechnen
            with open(doc, "rb") as file:
                file_content = file.read()
                hash_object = hashlib.sha256(file_content)
                hash_value = hash_object.hexdigest()

                # Prüfen auf doppelte Hash-Werte
                if hash_value in docs:
                    # Wenn der Hash schon existiert, füge die Datei zu den Duplikaten hinzu
                    if hash_value not in duplicates:
                        duplicates[hash_value] = [docs[hash_value]]  # Ursprüngliche Datei hinzufügen
                    duplicates[hash_value].append(doc.name)  # Neue Datei hinzufügen
                else:
                    docs[hash_value] = doc.name  # Neuen Hash und Datei speichern
else:
    print("Der Ordner existiert nicht oder ist kein Verzeichnis!")

# Ergebnisse ausgeben
print("Alle Dateien mit ihren Hash-Werten:")
for hash_value, filename in docs.items():
    print(f"Datei: {filename}, Hash: {hash_value}")

print("\nDoppelte Dateien:")
if duplicates:
    for hash_value, files in duplicates.items():
        print(f"Du scheinst doppelte Dateien zu haben! Dateien: {', '.join(files)},\n Haben den gleichen Hash: {hash_value}")
else:
    print("Keine doppelten Dateien gefunden.")