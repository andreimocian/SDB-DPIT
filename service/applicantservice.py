from repository.applicantRepository import ApplicantRepository
from domain.applicant import Applicant
from service.datehandler import DateHandler

class ApplicantService:
    def __init__(self, applicant_repository: ApplicantRepository, date_handler: DateHandler) -> None:
        self.__applicant_repository = applicant_repository
        self.__date_handler = date_handler

    def apply_for_job(self, name, linkCV, jobID):
        date = self.__date_handler.today_date()
        self.__applicant_repository.apply_to_job(Applicant(name, linkCV, jobID, date))

    def get_all_applicants_job(self, jobID):
        return self.__applicant_repository.get_all_applicants_from_job(jobID)

    def get_all_applicants(self):
        return self.__applicant_repository.get_all_applicants()