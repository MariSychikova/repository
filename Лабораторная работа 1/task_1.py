numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_of_excepted_element = 4

# замена пропущенного элемента
numbers[index_of_excepted_element] = sum(numbers[:index_of_excepted_element]+numbers[index_of_excepted_element + 1:]) \
                                     / len(numbers)
print("Измененный список:", numbers)
