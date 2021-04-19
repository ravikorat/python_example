class SalaryNotInRangeError(Exception):
    def __init__(self, salary, message=" Not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        

    def __str__(self):
        return f'Your salary is: {self.salary},{self.message}'


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
else:
    print("Your salary is between 5000 to 15000")