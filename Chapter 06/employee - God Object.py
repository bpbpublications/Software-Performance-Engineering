class Employee:
    def __init__(self, id, fn, jt, ln, ad, ct, pc, t1, t2, t3, sl, cc) -> None:
        self.id = id
        self.first_name = fn
        self.last_name = ln
        self.job_title = jt
        self.home_address = ad
        self.home_city = ct
        self.home_postcode = pc
        self.active_task1 = t1
        self.active_task2 = t2
        self.active_task3 = t3
        self.salary = sl
        self.company_car = cc

    def calculateSalaryTax(self):
        return self.salary * 0.1 #in Bulgaria
