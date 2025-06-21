# ფუნქცია არის კოდის ბლოკი რომელიც მაშინ იშვება როდესაც გამოვიძახებთ

# --------------------------------------------------------------------------------

# name = input('შეიყვანეთ სახელი:')
# print('გამარჯობა ' + name)

# --------------------------------------------------------------------------------

# names = ['ნიკა', 'ანა', 'გიორგი', 'თამარი', 'მარიამი']
# new_name = input('შეიყვანეთ სახელი:')
# index = int(input('შეიყვანეთ ინდექსი:'))

# if index > len(names):
#     print('ერორი: ინდექსი არასწორია')
# else:
#     names.insert(index, new_name)
#     print('განახლებული სია:', names)

# --------------------------------------------------------------------------------

# number = int(input('შეიყვანეთ რიცხვი:'))
# def kenti_tu_luwi(number)
#     if number % 2 == 0:
#         return 'ლუწი'
#     else:
#         return 'კენტი'


# ----------------------------------------------------------------------------------

def words_clenghts(winadadeba):
    words = winadadeba.split()
    result = [f"{word}: {len(word)}" for word in words]
    return result
print(words_clenghts("hello how are you"))