


# ==================== Observer Pattern ====================
from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self, patient):
        pass


class Doctor(Observer):
    def update(self, patient):
        print(f"*#Doctor Alert#* Patient {patient.name}'s health updated: {patient.health_data}")


class Nurse(Observer):
    def update(self, patient):
        print(f"*#Nurse Notification#* Patient {patient.name}'s new vitals: {patient.health_data}")


class Patient:
    def __init__(self, name):
        self.name = name
        self.health_data = {}
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for obs in self.observers:
            obs.update(self)

    def set_health_data(self, data):
        print(f"\n[System] Updating health data for {self.name}...")
        self.health_data = data
        self.notify()

    # ============= Memento Pattern Integration =============
    def save_state(self):
        return HealthMemento(self.health_data)

    def restore_state(self, memento):
        self.health_data = memento.health_data.copy()
        print(f"[System] Restored {self.name}'s health data to: {self.health_data}")

    # ============= Visitor Pattern Integration =============
    def accept(self, visitor):
        visitor.visit(self)


# ==================== Memento Pattern ====================
class HealthMemento:
    def __init__(self, health_data):
        self.health_data = health_data.copy()


class HealthHistory:
    def __init__(self):
        self._history = []

    def save(self, memento):
        self._history.append(memento)
        print("[System] Health state saved.")

    def restore(self, index):
        print(f"[System] Restoring health state from history index {index}...")
        return self._history[index]


# ==================== Visitor Pattern ====================
class HealthReportVisitor:
    def visit(self, patient):
        pass


class SummaryReportVisitor(HealthReportVisitor):
    def visit(self, patient):
        print("\n--- Summary Health Report ---")
        print(f"Patient: {patient.name}")
        print(f"Temperature: {patient.health_data.get('temperature', 'N/A')}°F")
        print(f"Heart Rate: {patient.health_data.get('heart_rate', 'N/A')} bpm")
        print(f"BP: {patient.health_data.get('bp', 'N/A')}")
        print("-----------------------------")


class DetailedReportVisitor(HealthReportVisitor):
    def visit(self, patient):
        print("\n=== Detailed Health Report ===")
        print(f"Patient Name: {patient.name}")
        for key, value in patient.health_data.items():
            print(f" - {key.capitalize()}: {value}")
        # Add custom logic for observations
        temp = patient.health_data.get("temperature", 98.6)
        hr = patient.health_data.get("heart_rate", 72)
        print("\nHealth Observations:")
        if temp > 100.4:
            print(" * High temperature detected — possible fever.")
        else:
            print(" * Temperature within normal range.")
        if hr > 100:
            print(" * Elevated heart rate — monitor closely.")
        else:
            print(" * Heart rate stable.")
        print("===============================")


# ==================== Integration ====================
def main():
    patient = Patient("Anil Kumar")
    doctor = Doctor()
    nurse = Nurse()

    patient.attach(doctor)
    patient.attach(nurse)

    history = HealthHistory()

    # Initial health data
    patient.set_health_data({"temperature": 98.6, "heart_rate": 72, "bp": "120/80"})
    history.save(patient.save_state())

    # Updated health data
    patient.set_health_data({"temperature": 101.2, "heart_rate": 90, "bp": "130/85"})
    history.save(patient.save_state())

    # Generate reports
    summary = SummaryReportVisitor()
    detailed = DetailedReportVisitor()

    patient.accept(summary)
    patient.accept(detailed)

    # Restore previous state
    print("\nRestoring previous health state...")
    patient.restore_state(history.restore(0))
    patient.accept(detailed)


if __name__ == "__main__":
    main()
