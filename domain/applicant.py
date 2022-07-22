class Applicant:
    def __init__(self, name, linkCV, jobs, date) -> None:
        self.__name = name
        self.__linkCV = linkCV
        self.__jobs = jobs
        self.__date = date

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_linkCV(self):
        return self.__linkCV

    def set_linkCV(self, new_linkCV):
        self.__linkCV = new_linkCV

    def get_jobs(self):
        return self.__jobs

    def set_jobs(self, new_jobs):
        self.__jobs = new_jobs

    def get_date(self):
        return self.__date

    def set_date(self, new_date):
        self.__date = new_date