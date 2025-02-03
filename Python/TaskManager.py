import psutil
import json

class TaskManager:
    @staticmethod
    def processes_manager():
        process_list = []
        for pid in psutil.pids():
            p = psutil.Process(pid)
            name = p.name()
            mem_usage = p.memory_percent()
            memusagemb = p.memory_info().rss
            mem_usage_mb = memusagemb / (1024 * 1024)
            # Erstelle eine Instanz von Process (deine eigene Klasse) für jeden Prozess
            process_info = Process(pid, name, mem_usage, mem_usage_mb)
            process_list.append(process_info)
        
        return process_list

    @staticmethod
    def json_export(filename="processes.json"):
        process_list = TaskManager.processes_manager()
        json_list = []
        for proc in process_list:
            # Erstelle ein Dictionary aus den Attributen deiner Process-Objekte
            info = {
                "pid": proc.pid,
                "name": proc.name,
                "memory_percent": proc.memory,
                "memory_mb": proc.memory_mb
            }
            json_list.append(info)
        
        # Schreibe die JSON-kompatiblen Daten in die angegebene Datei
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(json_list, json_file, ensure_ascii=False, indent=4)
            
        return filename
        
class Process:
    def __init__(self, pid, name, mem_usage, mem_usage_mb):
        self.pid = pid
        self.name = name
        self.memory = mem_usage
        self.memory_mb = mem_usage_mb

    def output(self):
        # Formatierte Ausgabe: PID, Name, Memory Usage % und Memory Usage MB (auf 2 Dezimalstellen)
        print(f"{self.pid:<15}{self.name:<35}{self.memory:<15.2f}{self.memory_mb:<15.2f}")

# Hauptprogramm
if __name__ == "__main__":
    # Alle Prozesse abrufen
    processes = TaskManager.processes_manager()
    # JSON exportieren
    filename = TaskManager.json_export()
    
    # Kopfzeile ausgeben
    print(f"{'PID':<15}{'Name':<35}{'Memory %':<15}{'Memory MB':<15}")
    print("-" * 80)

    # Für jeden Prozess die Informationen ausgeben
    for proc in processes:
        proc.output()
        
    print(f"Eine JSON Datei mit dem Namen: {filename} wurde erstellt.")