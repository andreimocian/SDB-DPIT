from ui.console import UI
from service.jobservice import JobService
from repository.repository import Repository
from service.applicantservice import ApplicantService
from service.datehandler import DateHandler
from repository.applicantRepository import ApplicantRepository

def main():
    datehandler = DateHandler()
    repository = Repository()
    jobservice = JobService(repository)
    applicantrepository = ApplicantRepository()
    applicantservice = ApplicantService(applicantrepository, datehandler)
    console = UI(jobservice, applicantservice, datehandler)
    console.run()

if __name__ == "__main__":
    main()