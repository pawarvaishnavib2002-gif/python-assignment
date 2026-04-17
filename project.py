import oracledb 

# ================= DATABASE CONNECTION =================
def get_connection():
    return oracledb.connect(
        user="system",            # change if needed
        password="your_password", # put your password
        dsn="localhost:1521/XE"   # XE or ORCL
)

# ================= PATIENT CLASS =================
class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        status_map = {
            0: "Normal",
            1: "Urgent",
            2: "Super Urgent"
        }
        return f"{self.name} ({status_map[self.status]})"


# ================= SPECIALIZATION CLASS =================
class Specialization:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        # Priority logic
        if patient.status == 2:
            self.patients.insert(0, patient)
        elif patient.status == 1:
            self.patients.insert(len(self.patients)//2, patient)
        else:
            self.patients.append(patient)


    def get_next_patient(self):
        if self.patients:
            return self.patients.pop(0)
        return None

    def print_patients(self):
        if not self.patients:
            print("No patients")
        for p in self.patients:
            print(p)


# ================= DATABASE FUNCTIONS =================
def save_patient(name, status, specialization):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO patients (name, status, specialization)
        VALUES (:1, :2, :3)
    """, (name, status, specialization))

    conn.commit()
    cursor.close()
    conn.close()


def show_db_patients():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, status, specialization FROM patients")

    print("\n--- Patients from Database ---")
    for row in cursor:
        print(row)

    cursor.close()
    conn.close()


# ================= OPERATIONS MANAGER =================
class OperationsManager:
    def __init__(self):
        self.specializations = {i: Specialization() for i in range(1, 6)}

    def menu(self):
        while True:
            print("\n===== Hospital System =====")
            print("1. Add Patient")
            print("2. Show Patients (Queue)")
            print("3. Get Next Patient")
            print("4. Show Database Patients")
            print("5. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.add_patient()
            elif choice == 2:
                self.print_all()
            elif choice == 3:
                self.get_next()
            elif choice == 4:
                show_db_patients()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice")

    def add_patient(self):
        spec = int(input("Enter specialization (1-5): "))
        name = input("Enter patient name: ")
        status = int(input("Enter status (0=Normal,1=Urgent,2=Super Urgent): "))

        patient = Patient(name, status)
        self.specializations[spec].add_patient(patient)

        # SAVE TO DATABASE
        save_patient(name, status, spec)

        print("✅ Patient added successfully!")

    def print_all(self):
        for spec, obj in self.specializations.items():
            print(f"\nSpecialization {spec}:")
            obj.print_patients()

    def get_next(self):
        spec = int(input("Enter specialization: "))
        patient = self.specializations[spec].get_next_patient()

        if patient:
            print("Next patient:", patient)
        else:
            print("No patients in queue")


# ================= MAIN =================
if __name__ == "__main__":
    app = OperationsManager()
    app.menu()
    
    