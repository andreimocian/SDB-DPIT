from service.jobservice import JobService
from service.applicantservice import ApplicantService
from service.datehandler import DateHandler

class UI:
    def __init__(self, job_service: JobService, applicant_service: ApplicantService, date_handler: DateHandler) -> None:
        self.__job_service = job_service
        self.__applicant_service = applicant_service
        self.__date_handler = date_handler

    def __print_first_menu(self):
        print("1. Employer menu")
        print("2. Applicant menu")
        print("0. Exit")

    def __print_employer_menu(self):
        print("1. Add job") 
        print("2. Delete job (by id)") 
        print("3. Edit job (by id)") 
        print("4. All jobs") 
        print("5. All jobs by department") 
        print("6. All applicants from job")
        print("7. Jobs with applicants")
        print("0. Exit submenu")

    def __print_applicant_menu(self):
        print("1. All jobs") 
        print("2. Apply to job") 
        print("3. All jobs by experience") 
        print("4. All jobs sorted by salary") 
        print("0. Exit submenu")

    def __add_job(self):
        jobID = input("Job ID: ")
        title = input("Job title: ")
        department = input("Job department: ")
        salary = int(input("Job salary: "))
        experience = int(input("Job experience: "))
        positions = int(input("Job Positions: "))
        self.__job_service.add(jobID, title, department, salary, experience, positions)

    def __delete_job(self):
        id = input("Job id: ")
        self.__job_service.delete(id)

    def __edit_job(self):
        id = input("Job id: ")
        attribute = input("What to edit: ")
        value = input("New value: ")
        self.__job_service.edit(id, attribute, value)

    def __print_job(self, job):
        print("Id: " + job.get_jobID())
        print("Title: " + job.get_title())
        print("Department: " + job.get_department())
        print("Salary: " + str(job.get_salary()))
        print("Experience: " + str(job.get_experience()))
        print("Positions: " + str(job.get_positions()))
        print("\n")

    def __print_all_jobs(self):
        jobs = self.__job_service.get_all()
        if len(jobs) == 0:
            print("No Jobs")
        else:
            for job in jobs:
                self.__print_job(job)

    def __print_all_jobs_sorted_salary(self):
        jobs = self.__job_service.get_all_sorted_salary()
        if len(jobs) == 0:
            print("No Jobs")
        else:
            for job in jobs:
                self.__print_job(job)

    def __print_all_jobs_by_department(self):
        department = input("Department: ")
        jobs = self.__job_service.get_all_department(department)
        if len(jobs) == 0:
            print("No Jobs")
        else:
            for job in jobs:
                self.__print_job(job)

    def __print_all_jobs_under_experience(self):
        experience = int(input("Experience: "))
        jobs = self.__job_service.get_all_uder_experience(experience)
        if len(jobs) == 0:
            print("No Jobs")
        else:
            for job in jobs:
                self.__print_job(job)

    def __apply_to_job(self):
        jobID = input("Job id: ")
        applicant_name = input("Applicant name: ")
        linkCV = input("Link CV: ")
        try:
            self.__job_service.decrement_positions(jobID)
            self.__applicant_service.apply_for_job(applicant_name, linkCV, jobID)

        except Exception as error:
            print(error)

    def __print_applicant(self, applicant):
        print("Name: " + str(applicant.get_name()))
        print("LinkCV: " + str(applicant.get_linkCV()))
        print("\n")

    def __print__all_applicants_from_job(self):
        recent_applicants = []
        jobID = input("JobID: ")
        applicants = self.__applicant_service.get_all_applicants_job(jobID)
        for applicant in applicants:
            if self.__date_handler.time_between_dates(applicant.get_date(), self.__date_handler.today_date()) < 30:
                recent_applicants.append(applicant)
        if len(recent_applicants) == 0:
            print("No Jobs")
        else:
            for applicant in recent_applicants:
                self.__print_applicant(applicant)

    def __print_all_jobs_with_applicants(self):
        jobs_with_applicant_list = []
        number_of_applicants_list = []
        joblist = self.__job_service.get_all_sorted_salary()
        applicantlist = self.__applicant_service.get_all_applicants()
        for job in joblist:
            number_of_applicants = 0 
            has_passed = False
            for applicant in applicantlist:
                if job.get_jobID() == applicant.get_jobs():
                    if has_passed == False:
                        jobs_with_applicant_list.append(job)
                        has_passed = True
                    number_of_applicants += 1
            if number_of_applicants != 0:
                number_of_applicants_list.append(number_of_applicants)
        if len(jobs_with_applicant_list) == 0:
            print("No jobs with applicants")
        else:
            for i in range(len(jobs_with_applicant_list)):
                print("Number of applicants: " +  str(number_of_applicants_list[i]))
                self.__print_job(jobs_with_applicant_list[i])

    def run(self):
        mode = False
        while True:
            self.__print_first_menu()
            role = int(input("Choose command: "))
            try:
                if role == 0:
                    return 
                elif role == 1:
                    mode = True
                elif role == 2:
                    mode = False
                else:
                    print("Invalid input")
                    self.run()
                    break
            except Exception as error:
                print(error)

            if mode == True:
                while True:
                    self.__print_employer_menu()
                    command = int(input("Choose command: "))
                    try:
                        if command == 0:
                            break
                        elif command == 1:
                            self.__add_job()
                        elif command == 2:
                            self.__delete_job()
                        elif command == 3:
                            self.__edit_job()
                        elif command == 4:
                            self.__print_all_jobs()
                        elif command == 5:
                            self.__print_all_jobs_by_department()
                        elif command == 6:
                            self.__print__all_applicants_from_job()
                        elif command == 7:
                            self.__print_all_jobs_with_applicants()
                        else:
                            print("Invalid input")
                    except Exception as error:
                        print(error)

            if mode == False:
                while True:
                    self.__print_applicant_menu()
                    command = int(input("Choose command: "))
                    try:
                        if command == 0:
                            break
                        elif command == 1:
                            self.__print_all_jobs()
                        elif command == 2:
                            self.__apply_to_job()
                        elif command == 3:
                            self.__print_all_jobs_under_experience()
                        elif command == 4:
                            self.__print_all_jobs_sorted_salary()
                        else:
                            print("Invalid input")
                    except Exception as error:
                        print(error)


    



