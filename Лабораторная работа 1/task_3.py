list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

number_of_players = len(list_players)
index_middle = number_of_players // 2

# разделение на игроков на две команды
first_team = list_players[:index_middle]
second_team = list_players[index_middle:]

print(first_team)
print(second_team)
