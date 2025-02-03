import psutil

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
            # Erstelle eine Instanz von ProcessInfo für jeden Prozess
            process_info = Process(pid, name, mem_usage, mem_usage_mb)
            process_list.append(process_info)
        return process_list

class Process:
    def __init__(self, pid, name, mem_usage, mem_usage_mb):
        self.pid = pid
        self.name = name
        self.memory = mem_usage
        self.memory_mb = mem_usage_mb

    def output(self):
        # Formatierte Ausgabe: PID, Name, Memory Usage %  und Memory Usage MB (auf 2 Dezimalstellen)
        print(f"{self.pid:<15}{self.name:<35}{self.memory:<15.2f}{self.memory_mb:<15.2f}")

# Hauptprogramm
if __name__ == "__main__":
    # Alle Prozesse abrufen
    processes = TaskManager.processes_manager()

    # Kopfzeile ausgeben
    print(f"{'PID':<15}{'Name':<35}{'Memory %':<15}{'Memory MB':<15}")
    print("-" * 80)

    # Für jeden Prozess die Informationen ausgeben
    for proc in processes:
        proc.output()
