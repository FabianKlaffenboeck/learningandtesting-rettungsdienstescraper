class Duty:
    def __init__(self,_uid,_from_data, _to_data, _name):
        self.uid = _uid
        self.from_data = _from_data
        self.to_data = _to_data
        self.person_name = _name

class Selve_duty:
    def __init__(self,_uid,_from_data, _to_data, _duration,_other_person):
        self.uid = _uid
        self.from_data = _from_data
        self.to_data = _to_data
        self.duration = _duration
        self.other_person = _other_person
