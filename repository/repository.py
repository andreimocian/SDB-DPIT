class Repository:
    def __init__(self) -> None:
        self.__entitiesList = []

    def find_position(self, entity):
        for i in range(len(self.__entitiesList)):
            if self.__entitiesList[i] == entity:
                return i
        return None

    def find_by_id(self, id):
        for i in range(len(self.__entitiesList)):
            if self.__entitiesList[i].get_jobID() == id:
                return self.__entitiesList[i]
        return None

    def add_job(self, entity):
        if self.find_by_id(entity.get_jobID()) is not None:
            raise Exception("Already exists!")
        self.__entitiesList.append(entity)

    def delete_job(self, id):
        position = self.find_position(self.find_by_id(id))
        if position == None:
            raise Exception("Does not exist!")
        del self.__entitiesList[position]

    def update_job(self, id, attribute, attribute_value):
        entity = self.find_by_id(id)
        if entity == None:
            raise Exception("Does not exist!")

        if attribute == "jobID":
            self.__entitiesList[self.find_position(entity)].set_jobID(attribute_value)
        elif attribute == "title":
            self.__entitiesList[self.find_position(entity)].set_title(attribute_value)
        elif attribute == "department":
            self.__entitiesList[self.find_position(entity)].set_department(attribute_value)
        elif attribute == "salary":
            self.__entitiesList[self.find_position(entity)].set_salary(int(attribute_value))
        elif attribute == "experience":
            self.__entitiesList[self.find_position(entity)].set_experience(int(attribute_value))
        elif attribute == "positions":
            self.__entitiesList[self.find_position(entity)].set_positions(int(attribute_value))
        else:
            raise Exception("Invalid attribute")

    def get_all(self):
        return self.__entitiesList

    def get_all_by_department(self, department):
        department_jobs = []
        for entity in self.__entitiesList:
            if entity.get_department() == department:
                department_jobs.append(entity)
        return department_jobs

    def get_all_sorted_salary(self):
        jobs = self.__entitiesList
        jobs.sort(key=lambda x: x.salary, reverse=True)
        return jobs

    def get_all_sorted_experience(self):
        jobs = self.__entitiesList
        jobs.sort(key=lambda x: x.experience, reverse=False)
        return jobs

    def decrement_positions(self, jobID):
        job = self.find_by_id(jobID)
        position = self.find_position(job)
        if position == None:
            raise Exception("Does not exist!")
        initial_value = self.__entitiesList[position].get_positions()
        if initial_value == 0:
            raise Exception("No more positions left")
        self.__entitiesList[position].set_positions(initial_value - 1)


