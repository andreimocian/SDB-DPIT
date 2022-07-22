class ApplicantRepository:
    def __init__(self) -> None:
        self.__entitiesList = []

    def find_position(self, entity):
        for i in range(len(self.__entitiesList)):
            if self.__entitiesList[i] == entity:
                return i
        return None

    def find_position_by_name(self, name):
        for i in range(len(self.__entitiesList)):
            if self.__entitiesList[i].get_name() == name:
                return i
        return None

    def add_applicant(self, entity):
        self.__entitiesList.append(entity)

    def apply_to_job(self, entity):
        name = entity.get_name()
        position = self.find_position_by_name(name)
        if position is not None:
            raise Exception("You already applied for a job")
        else:
            self.add_applicant(entity)
        """ if position is not None:
            tempCV = set()
            tempJobs = set()
            try:
                tempCV.add(self.__entitiesList[position].get_linkCV())
                tempJobs.add(self.__entitiesList[position].get_jobs())
            except Exception as error:
                print(error)

            tempCV.add(entity.get_linkCV())
            self.__entitiesList[position].set_linkCV(tempCV)

            tempJobs.add(entity.get_jobs())
            self.__entitiesList[position].set_jobs(tempJobs)
        else: """

    def get_all_applicants_from_job(self, jobID):
        applicants_job = []
        for entity in self.__entitiesList:
            if entity.get_jobs() == jobID:
                applicants_job.append(entity)
        return applicants_job

    def get_all_applicants(self):
        return self.__entitiesList

