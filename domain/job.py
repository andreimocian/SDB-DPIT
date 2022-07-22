class Job:
    def __init__(self, jobID, title, department, salary, experience, positions: int) -> None:
        self.__jobID = jobID
        self.__title = title
        self.__department = department
        self.salary = salary
        self.experience = experience
        self.__positions = positions

    def get_jobID(self):
        return self.__jobID

    def set_jobID(self, new_id):
        self.__jobID = new_id

    def get_title(self):
        return self.__title
    
    def set_title(self, new_title):
        self.__title = new_title

    def get_department(self):
        return self.__department

    def set_department(self, new_department):
        self.__department = new_department

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary

    def get_experience(self):
        return self.experience

    def set_experience(self, new_experience):
        self.experience = new_experience

    def get_positions(self):
        return self.__positions

    def set_positions(self, new_positions):
        self.__positions = new_positions