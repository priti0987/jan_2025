###create a class employee with attributes emp_id, name, salary and also define methods to access properties of employee###

class Employee:
    def __init__(self,emp_id=None,emp_name=None,emp_salary=None):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
    def set_emp_id(self,empID):
        self.emp_id = empID

    def set_emp_name(self, empNAME):
            self.emp_name = empNAME

    def set_emp_salary(self, empSalary):
        self.emp_salary = empSalary

    def get_emp_id(self):
        return self.emp_id

    def get_emp_name(self):
        return self.emp_name

    def get_emp_salary(self):
        return self.emp_salary




e1=Employee()
e2=Employee(23,"Priti",4500)
e1.set_emp_name("priya")
e1.set_emp_id(22)
e1.set_emp_salary(5000)
print("Employee 1 = ",e1.get_emp_id(),e1.get_emp_name(),e1.get_emp_salary())
print("Employee 2 = ",e2.get_emp_id(),e2.get_emp_name(),e2.get_emp_salary())