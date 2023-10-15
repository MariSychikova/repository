# начальные данные
DISK_SIZE_MEGABYTES = 1.44
DISK_SIZE_BYTES = 1.44 * 1024 * 1024
PAGES_IN_THE_BOOK = 100
STRINGS_PER_PAGE = 50
SYMBOLS_PER_STRING = 25
SPACE_FOR_ONE_SYMBOL_BYTES = 4

# расчет количества книг на диск
symbols_per_book_bytes = PAGES_IN_THE_BOOK * STRINGS_PER_PAGE * SYMBOLS_PER_STRING
space_for_one_book = symbols_per_book_bytes * SPACE_FOR_ONE_SYMBOL_BYTES
number_of_books_on_disk = int(DISK_SIZE_BYTES // space_for_one_book)

print("Количество книг, помещающихся на дискету:", number_of_books_on_disk)
