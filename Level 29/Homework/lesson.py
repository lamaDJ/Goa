# def odd(list):
#     for i in list:
#         if i % 2 != 0:
#             print(i)
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(odd(list))

# --------------------------------------------------------------------------------------------------------

# def name(names_list):
#     return(name for name in names_list if len(name) == 4)
# names_list = ['Mate', 'Pavle', 'Giorgi', 'Luka', 'Vano', 'Andria', 'Sandro']
# result = name(names_list)
# print(list(result))

# ---------------------------------------------------------------------------------------------------------

def numbers(numbers_list):
    for i in list(numbers_list):
        if i % 3 == 0 and i % 5 == 0:
            print(i)
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
print(numbers(numbers_list))

# ---------------------------------------------------------------------------------------------------------

# f - string ანუ formatted string literal - საშუალებას გვაძლევს სტრინგში პირდაპირ ჩავსვათ ცვლადების მნიშვნელობები ფრჩხილებში
