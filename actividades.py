class Activity:
    def __init__(self, name, date, priority):
        self.name = name,
        self.date = date,
        self.priority = priority
    
    def set_date(self, date):
        self.date = date

    def set_priority(self, priority):
        self.priority = priority

    def set_name(self, name):
        self.name = name