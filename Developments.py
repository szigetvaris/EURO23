from random import uniform

class Developments:
    # {'stadium': 0, 'marketing': 0, 'school': 0, 'training_center': 0, 'medical_center': 0, 'rehabilitation_center': 0, 'data_analysis': 0, 'scouting_system': 0, 'youth_academy': 0, 'education': 0, 'talent_nurturing': 0}
    def __init__(self, developments):
        self.developments = developments

    def get_stadium_bonus(self):
        bonus = 200
        return self.developments['stadium'] * bonus

    def get_marketing_bonus(self):
        bonus = 200
        return self.developments['marketing'] * bonus

    def get_school_bonus(self):
        bonus = 0.2
        return self.developments['school'] * bonus

    def get_training_center_bonus(self):
        bonus = 0.05
        return (self.developments['training_center'] * bonus) + 1

    def get_medical_center_bonus(self):
        pass

    def get_rehabilitation_center_bonus(self):
        bonus = 0.15
        return (self.developments['rehabilitation_center'] * bonus) + 1

    def get_data_analysis_center_bonus(self):
        pass

    def get_scouting_system_bonus(self):
        pass

    def get_youth_academy_bonus(self):
        base_line = (self.developments['youth_academy'] * 0.25) + 0.1
        result = uniform(0, 1)
        bonus = 0
        if result < base_line:
            bonus = 1
        return bonus

    def get_education_bonus(self):
        return self.developments['education']

    def get_talent_nurturing_bonus(self):
        return self.developments['talent_nurturing'] * 0.05
