from pathlib import Path

home = Path ("C:\\Users\\HartmanM\\OneDrive - Berufsförderungswerk Köln gGmbH\\Dokumente\\Testdaten\\pathlib")

def doc_creation():
    answer = "ja"
    while True:
        if answer.lower() == "ja" :
            name = input("Wie soll die datei heissen?\n")
            datentyp = input("was soll sie für ein datentypsein? (.txt,.html,.pdf,.json,.py usw.)\n")
            text = input("Was soll in der datei stehen?\n")
            dateiname = name + "." + datentyp
            # Path(home, dateiname).touch(mode=0o777, exist_ok=True)
            file_path = Path(home, dateiname)
            file_path.write_text(text)
            print(f'Die Datei "{dateiname}" wurde in "{home}" erstellt!')
            answer = input("Möchten sie noch eine Datei erstellen?\n")
        else:
            return file_path


last_file = doc_creation()

def doc_reading(last_file):
    answer = "ja"
    while True:
        if last_file.exists():
            if answer.lower() == "ja":
                with last_file.open("r", encoding="utf-8") as file:
                    print(file.read())
                answer = input("Noch etwas Lesen?\n")
        else:
            break
            
doc_reading(last_file)