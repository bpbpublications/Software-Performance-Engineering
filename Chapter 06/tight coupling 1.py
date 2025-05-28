# A helper class to calculate salary tax 
class TaxCalculator:
    def calculateTax (self, salary):
        return salary * 0.1 # For Bulgaria

# Represents a company employee
class Employee:
    def __init__(self, id, fn, ln, jt, sl) -> None:
        self.id = id
        self.first_name = fn
        self.last_name = ln
        self.job_title = jt
        self.salary = sl

    def calculateSalaryTax(self):
        calculator = TaxCalculator()
        return calculator.calculateTax (self.salary)

# Example:
alon = Employee(1234, "Alon", "Rotem", "Software whisperer", 1000)
print(f"{alon.first_name}'s tax is {alon.calculateSalaryTax()}")
