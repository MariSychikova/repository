users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# создание словаря с двумя ключами
dict_ = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

# подсчет всех посетителей и уникальных
total_number_of_users = len(users)
unic_number_of_users = len(set(users))

# обновление значений в словаре
dict_["Общее количество"] = total_number_of_users
dict_["Уникальные посещения"] = unic_number_of_users

print(dict_)
