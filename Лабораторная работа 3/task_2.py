def find_common_participants(participants_1, participants_2, separator=','):
    set_participants_1 = set(participants_1.split(separator))
    list_common_participants = sorted(set_participants_1.intersection(participants_2.split(separator)))

    return list_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", common_participants)
