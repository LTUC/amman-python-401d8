# Poetry: poetry add requests
# PIP: pip install requests
import requests


URL = "https://www.basketball-reference.com/draft/NBA_2020.html"
res = requests.get(URL)
# print(res.content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(res.content, "html.parser")

results_div = soup.find("div", id="div_stats")
# print(type(results_div))
players_table = results_div.find("table", id="stats")
# print(players_table)

table_body = players_table.find("tbody")
# print(table_body)
players_list = table_body.find_all('td')
# print(players_list)

# for player in players_list:
#     print(player)
#     print("="*50)

needed_features = []
names_list=[]
teams_list=[]
for feature in players_list:
    if feature.attrs["data-stat"] == "player":
        names_list.append(feature.get_text())
    if feature.attrs["data-stat"] == "team_id":
        teams_list.append(feature.get_text())


# ["NOP", "Sam Merrill", "LAC", "Whatever"]
# player_data={
#     "player_name":"Sam Merrill",
#     "player_team":"NOP"
# }

"""
[
    {
    "player_name":"Sam Merrill",
     "player_team":"NOP"
 },
     {
    "player_name":"Whatever",
     "player_team":"LAC"
 },
]
"""
zipped_list = zip(names_list, teams_list)
cleaned_players_list=[]
for player in zipped_list:
    player_data ={}
    player_data["name"] = player[0]
    player_data["team"] = player[1]
    cleaned_players_list.append(player_data)
    print(player_data)


# for index in range(len(names_list)):
#     player_data ={}
#     player_data["name"] = names_list[index]
#     player_data["team"] = teams_list[index]
#     cleaned_players_list.append(player_data)
#     print(player_data)
import json

with open('players_names.json', 'w') as f:
    content = json.dumps(cleaned_players_list)
    f.write(content)
