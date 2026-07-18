class Employee:
    def __init__(self, first_name, last_name, age, employee_id, position):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.employee_id = employee_id
        self.position = position
        self.is_clocked_in = False
        self.has_called_out = False
        self.hours_worked = 0

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def clock_in(self):

        if self.is_clocked_in:
            print(f"{self.full_name()} is already clocked in.")
            return

        self.is_clocked_in = True
        print(f"{self.full_name()} has been clocked in.")

    def clock_out(self):
        if not self.is_clocked_in:
            print(f"{self.full_name()} is not clocked in.")
            return

        self.is_clocked_in = False
        print(f"{self.full_name()} has been clocked out.")

    def call_off(self):
        if self.has_called_out == True:
            print(f"{self.full_name()} has called off.")
            return

        self.has_called_out = False
        print(f"{self.full_name()} has not called out")
