# s = 'あいうえお'
# k = 'かきくけこ'
# h = s + k
# user_input = input()
# print(h)
# result = f'こんにちは、{user_input}'
# print(resulet)
#
# 文字列の長さとりだす
# a = len("aiue")
# b = 'aiue'
# print(a)
# # 先頭3文字とりだす
# print(b[:3])
# # 3文字以降とりだす
# print(b[2:])
# c = str(18)
# print(c)
#
# s = f'今年は{user_input}年。来年は{str(int(user_input) + 1)}年です。'
# print(s)

# data_list = [1, 2, [3, 4, 5], [6, 7], 8, 9, [10, 11]]
# print(data_list[3][1])
#
# data_list_2 = []
# user_input = input()
# user_input2 = input()
# user_input3 = input()
# data_list_2.append(user_input)
# data_list_2.append(user_input2)
# data_list_2.append(user_input3)
# data_list_2.sort()
# print(data_list_2)
#
# data_list_3 = []
# user_input4 = input()
# user_input5 = input()
# user_input6 = input()
# data_list_3.insert(0, user_input4)
# data_list_3.insert(1, user_input5)
# data_list_3.insert(2, user_input6)
# data_list_3_sample = sorted(data_list_3, reverse=True)
# print(data_list_3_sample)


# data_list_2 = sorted(data_list)
# print(data_list_2)


text = 'apple,banana,orange'
food_list = text.split(',')
print(food_list)

food_text = ','.join(food_list)
print(food_text)

user_file_text = """
hoge 
fuga 
taro 
ziro 
saburo
"""
user_list = user_file_text.split()
user_list.sort()
user_text = """ """.join(user_list)
print(user_text)

user_list2 = user_file_text.split()
user_list2.sort()
user_text2 = """\n""".join(user_list2)
print(user_text2)

hosi = {
    '水': 'water',
    '風': 'wind',
    '火': 'fire',
    1: 'one',
    (1, 1, 1): 5,
    (6, 6, 6): 3
}

print(hosi['火'])