# standard libs
import random as rnd

import pandas as pd
import streamlit as st

from Player import Player
# third party libs

# user imports
import Player as pl
import Team
from Developments import Developments

# team creation
# df_teams = pd.read_excel('data/database.xlsx', sheet_name='countries')
# df_players = pd.read_excel('data/players.xlsx', sheet_name='players')
#
# teams = list()
# for row in df_teams.itertuples():
#     teams.append(Team.Team(row.cname, row.shortName, row.language,
#                            row.power, row.gold, row.silver, row.bronze,
#                            row.NL))
# team = teams[0]

# p = Player("Bukayo Saka", "England", 0, 0, 72, 81, 81, 0, 9, 1.2, 0, 1, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, "")
# print(p.scout())

d = Developments({'stadium': 3, 'marketing': 3, 'school': 3, 'training_center': 3,
                  'medical_center': 3, 'data_analysis': 3, 'scouting_system': 3,
                  'youth_academy': 3, 'education': 3, 'talent_nurturing': 3})
print(d.developments[3])