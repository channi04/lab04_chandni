class FlightRecord:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def sort_by_p_id(self):
        self.records.sort(key=lambda x: x.p_id)

    def sort_by_start_time(self):
        self.records.sort(key=lambda x: x.start_time)

    def sort_by_priority(self):
        self.records.sort(key=lambda x: x.priority, reverse=True)

    def display(self):
        for record in self.records:
            print(f"P_ID: {record.p_id}, Process: {record.process}, Start Time: {record.start_time} ms, Priority: {record.priority}")

def main():
    flight_table = FlightTable()

    flight_table.add_record(FlightRecord("P1", "VSCode", 100, "MID"))
    flight_table.add_record(FlightRecord("P23", "Eclipse", 234, "MID"))
    flight_table.add_record(FlightRecord("P93", "Chrome", 189, "High"))
    flight_table.add_record(FlightRecord("P42", "JDK 9", 9, "High"))
    flight_table.add_record(FlightRecord("P9", "CMD", 7, "High"))
    flight_table.add_record(FlightRecord("P87", "NotePad", 23, "Low"))

    while True:
        print("\nOptions:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            flight_table.sort_by_p_id()
        elif choice == '2':
            flight_table.sort_by_start_time()
        elif choice == '3':
            flight_table.sort_by_priority()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

        flight_table.display()

if __name__ == "__main__":
    main()