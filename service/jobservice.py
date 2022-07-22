from repository.repository import Repository
from domain.job import Job

class JobService:
    def __init__(self, job_repository: Repository) -> None:
        self.__job_repository = job_repository

    def get_all(self):
        return self.__job_repository.get_all()

    def add(self, jobID, title, department, salary, experience, positions):
        self.__job_repository.add_job(Job(jobID, title, department, salary, experience, positions))

    def delete(self, id):
        self.__job_repository.delete_job(id)

    def edit(self, id, attribute, attribute_value):
        self.__job_repository.update_job(id, attribute, attribute_value)

    def get_all_department(self, department):
        return self.__job_repository.get_all_by_department(department)

    def get_all_sorted_salary(self):
        return self.__job_repository.get_all_sorted_salary()
    
    def get_all_uder_experience(self, experience):
        job_list = self.__job_repository.get_all_sorted_experience()
        new_list = []
        for job in job_list:
            if job.get_experience() <= experience:
                new_list.append(job)
        return new_list

    def decrement_positions(self,jobID):
        self.__job_repository.decrement_positions(jobID)


    