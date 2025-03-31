class DutyPlanEntity:
    def __init__(self, uid, from_data, to_data, name):
        self.uid = uid
        self.from_data = from_data
        self.to_data = to_data
        self.person_name = name


class Duty:
    def __init__(self, uid, duty_type, from_data, to_data, duration, other_person):
        self.uid = uid
        self.type = duty_type
        self.from_data = from_data
        self.to_data = to_data
        self.duration = duration
        self.other_person = other_person
