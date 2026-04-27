# used @classmethod to create a class method
class Employee:
    company_name = "Tech Solutions"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod #using the class method instead of using self  as instance method to change the class variable
    def change_company_name(cls, new_name):
        cls.company_name = new_name

    @classmethod
    def display_company_info(cls):
        print(f"Company Name: {cls.company_name}")
# Display initial company information
Employee.display_company_info()  # Output: Company Name: Tech Solutions
# Change the company name using the class method
Employee.change_company_name("Innovative Tech")
# Display updated company information
Employee.display_company_info()  # Output: Company Name: Innovative Tech
