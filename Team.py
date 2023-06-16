
class Team:
    def __init__(self, name, short_name, language, power, gold, silver, bronze, nations_league, defense=0, midfield=0, attack=0, players=None):
        self.name = name
        self.short_name = short_name
        self.language = language
        self.power = power
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
        self.nations_league = nations_league
        self.defense = defense
        self.midfield = midfield
        self.attack = attack
        self.players = players #list of players

