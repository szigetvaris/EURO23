from random import randint, random, uniform
import time as t

class Player:
    def __init__(self, name, nationality, date_of_birth, age,
                 defense, midfield, attack, skill,
                 potential, talent, form, call_up, injured, condition,
                 games_ts, trained_ts, developed_ts, scores_ts,
                 games_at, trained_at, developed_at, injured_at,
                 notes):
        self.name = name
        self.nationality = nationality
        self.date_of_birth = int(date_of_birth)
        self.age = int(age)
        self.defense = int(defense)
        self.midfield = int(midfield)
        self.attack = int(attack)
        self.skill = int(skill)
        self.potential = int(potential)
        self.talent = float(talent)
        self.form = int(form)
        self.call_up = int(call_up)
        self.injured = int(injured)
        self.condition = int(condition)
        self.games_ts = int(games_ts)
        self.trained_ts = int(trained_ts)
        self.developed_ts = int(developed_ts)
        self.scores_ts = int(scores_ts)
        self.games_at = int(games_at)
        self.trained_at = int(trained_at)
        self.developed_at = int(developed_at)
        self.injured_at = int(injured_at)
        self.notes = notes

    def modify_condition(self, amount):
        self.condition = self.condition + amount * 2
        self.condition = min(self.condition, 12)
        self.condition = max(self.condition, 6)

    def reset_skill(self, bonus=0):
        self.skill = 0 + bonus

    def generate_potential(self, bonus=0):
        # inorder to avoid random number defect wait a little bit
        t.sleep(1 / 1000)
        potential = randint(6, 12) + bonus
        potential = min(potential, 12)
        self.potential = potential

    def generate_talent(self, bonus=0):
        t.sleep(1 / 1000)
        a = 1 + bonus
        self.talent = round(uniform(a, 1.3), 2)

    def generate_form(self):
        # inorder to avoid random number defect wait a little bit
        t.sleep(1 / 1000)
        self.form = randint(-3, 3)

    def draw_defense(self):
        random_value = randint(0, self.condition - 1)
        return self.defense + self.form + random_value + self.skill

    def draw_midfield(self):
        random_value = randint(0, self.condition - 1)
        return self.midfield + self.form + random_value + self.skill

    def draw_attack(self):
        random_value = randint(0, self.condition - 1)
        return self.attack + self.form + random_value + self.skill

    def reset_player(self):
        # reset attributes
        self.reset_skill()
        self.generate_potential()
        self.generate_talent()
        # reset stats
        self.games_at, self.trained_at, self.developed_at, self.injured_at = 0, 0, 0, 0

    def calc_age(self, year):
        age = (year % 4) - self.date_of_birth
        if age >= 0:
            return age
        return age+4

    # TODO: refactoring the age calculation structure. do it once in GENERATE NEW SEASON
    def train(self, bonus=1):
        t.sleep(1 / 1000)
        if self.potential > 0:
            year = 2022 # only for testing
            age = year % 4
            growth_probabilities = {0: 0.3, 1: 0.23, 2: 0.15, 3: 0.08}
            growth_probability = growth_probabilities.get(age, 0)
            train_result = random() / self.talent / bonus
            if train_result < growth_probability:
                self.skill += 1
                self.potential -= 1
                print("[TRAINING] " + self.name + " has managed to earn a skill point")

    def injury(self, med_bonus=1, rehab_bonus=1):
        t.sleep(1/1000)
        year = 2020
        age = year % 4
        injury_event = randint(1, self.fitness)
        if injury_event == 1:
            # TODO: modify condition by -2
            # TODO: use med center bonus
            age_penalty_probabilities = {0: 0.1, 1: 0.1, 2: 0.2, 3: 0.3}
            age_penalty_probalbility = age_penalty_probabilities.get(age, 0)
            injury_result = random() * rehab_bonus
            if injury_result < age_penalty_probalbility:
                self.skill -= 1
                # print(self.name + " has lost a skill point.")

    def get_potential(self):
        rnd_potential = self.potential + randint(-1,1)
        if rnd_potential <= 2:
            return "Low"
        elif rnd_potential >= 3 and rnd_potential <= 6:
            return "Moderate"
        elif rnd_potential >= 7 and rnd_potential <= 9:
            return "High"
        elif rnd_potential >= 10:
            return "Very High"

    def get_talent(self):
        rnd_talent = self.talent + uniform(-0.05, 0.05)
        if rnd_talent <= 1.05:
            return "Very Poor"
        elif rnd_talent > 1.05 and rnd_talent <= 1.15:
            return "Poor"
        elif rnd_talent > 1.15 and rnd_talent <= 1.2:
            return "Moderate"
        elif rnd_talent > 1.2 and rnd_talent <= 1.25:
            return "High"
        elif rnd_talent > 1.25:
            return "Very High"

    def get_form(self):
        rnd_form = self.form + randint(-1, 1)
        if rnd_form <= -2:
            return "Poor"
        elif rnd_form >= -1 and rnd_form <= 1:
            return "Good"
        elif rnd_form >= 2:
            return "Excellent"

    def get_age_category(self):
        if self.age == 0:
            return "Youngster"
        elif self.age == 1:
            return "Prospect"
        elif self.age == 2:
            return "Prime"
        elif self.age == 3:
            return "Veteran"


    def scout(self):
        return "Here is the report from " + self.name + " ("+ self.get_age_category()+"): The player currently in " \
            + self.get_form() + " form. His potential is " + self.get_potential() + " and he has a " \
            + self.get_talent() + " aptitude for trainings."
