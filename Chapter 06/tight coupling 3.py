from abc import ABC, abstractmethod

# A binding interface
class ITaxCalculator(ABC):
    @abstractmethod
    def calculateTax(self, salary):
        pass

# A helper class to calculate salary tax 
class TaxCalculator(ITaxCalculator):
    def calculateTax (self, salary):
        return salary * 0.1 # For Bulgaria
    
# A helper to calculate salary tax for managers!
class ManagerTaxCalculator(ITaxCalculator):
    def calculateTax (self, salary):
        return salary * 0.05

# Represents a company employee
class Employee:
    def __init__(self, id, fn, ln, jt, sl) -> None:
        self.id = id
        self.first_name = fn
        self.last_name = ln
        self.job_title = jt
        self.salary = sl

    def calculateSalaryTax(self, calculator:ITaxCalculator):
        return calculator.calculateTax (self.salary)


# Example
alon = Employee(1234, "Alon", "Rotem", "Software whisperer", 1000)
zaphod = Employee(5678, "Zaphod", "Beeblebrox", "Manager", 6000)

calc = TaxCalculator()
manager_calc = ManagerTaxCalculator()

print(f"{alon.first_name}'s tax is {alon.calculateSalaryTax(calc)}")
print(f"{zaphod.first_name}'s tax is {zaphod.calculateSalaryTax(manager_calc)}")
