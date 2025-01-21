import os

# Variablen zur Speicherung der Namen
path = "C:\\Users\\HartmanM\\OneDrive - Berufsförderungswerk Köln gGmbH\\Dokumente\\Testdaten"
#path = r"C:\Users\HartmanM\OneDrive - Berufsförderungswerk Köln gGmbH\Dokumente\Testdaten"

# Funktion zum Auflisten der Dateien
def list_files(path):
    # Prüfe zuerst, ob der Pfad existiert
    if not os.path.exists(path):  # Wenn der Pfad nicht existiert
        print("The Path does not exist.")
        return None
         
    return os.listdir(path)
    
# Funktion zum Sortieren der Dateien nach Länge (absteigend)
def sort_names(names):
    # Ausgabe und Sortierung der Liste nach Länge (absteigend)
    #print("\n" .join(sorted(names, key=len, reverse=True)))
    # Rückgabe der sortierten Liste
    return sorted(names, key=len, reverse=True)
    
def in_dict(sorted_names):
    dictan = {}
    for data in names:
        data_path = os.path.join(path, data)
        if os.path.isfile(data_path):
            size = os.path.getsize(data_path)
            dictan[data] = size
            
    #print(dict)
            
    return dictan

def dict_filter(sort_dict):
    filtert = {k: v for k, v in sort_dict.items() if k.endswith('.txt')}
    return filtert
# Dateien auflisten und sortieren
names = list_files(path)
sorted_names = sort_names(names)
dictanary = in_dict(sorted_names)
sort_dict = dict(sorted(dictanary.items(), key=lambda item: len(item[0]), reverse=True))
filtered_dict = dict_filter(sort_dict)
# Debugging Ausgabe
#print("\n".join(dict))
for key, value in filtered_dict.items():
   print(f"{key}: {value}")