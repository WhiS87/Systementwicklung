from pathlib import Path

# new_file = Path("C:\\Users\\HartmanM\\OneDrive - Berufsförderungswerk Köln gGmbH\\Dokumente\\Testdaten\\pathlib\\data.txt")
# new_file.touch()

home = Path ("C:\\Users\\HartmanM\\OneDrive - Berufsförderungswerk Köln gGmbH\\Dokumente\\Testdaten\\pathlib")

name = input("Wie soll die datei heissen?\n")
datentyp = input("was soll sie für ein datentypsein? (.txt,.html,.pdf,.json,.py usw.)\n")
dateiname = name + "." + datentyp
Path(home, dateiname).touch(mode=0o777, exist_ok=True)
print(f'Die Datei "{dateiname}" wurde in "{home}" erstellt!')