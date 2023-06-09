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


# text = 'apple,banana,orange'
# food_list = text.split(',')
# print(food_list)
#
# food_text = ','.join(food_list)
# print(food_text)
#
# user_file_text = """
# hoge
# fuga
# taro
# ziro
# saburo
# """
# user_list = user_file_text.split()
# user_list.sort()
# user_text = """ """.join(user_list)
# print(user_text)
#
# user_list2 = user_file_text.split()
# user_list2.sort()
# user_text2 = """\n""".join(user_list2)
# print(user_text2)


# hosi = {
#     '水': 'water',
#     '風': 'wind',
#     '火': 'fire',
#     1: 'one',
#     (1, 1, 1): 5,
#     (6, 6, 6): 3
# }
# print(hosi['火'])


# number_list = [1,1,2,2,4,4]
# number_set = set(number_list)
# print(number_set)

# number = 200
# number_list = ['taro','jiro']
# if number != 100:
#     print('aaa')
# else:
#     print('hhh')
# if 'taro' in number_list:
#     print('hhh')
# else:
#     print('not')

# Pythonで、if 変数: と書いたとき、Falseとなるもの一覧
# a = []
# a = ''
# a = 0
# a = {}
# a = ()
# a = None
# a = False
# if a:
#     print('空じゃなかった')
# else:
#     print('aは空でした')
#
# name_list = ['suzuki','ata','siraisi']
#
# for name in name_list:
#     if name == name_list[2]:
#         break
#     print(name,end=' ')
#
# for i in range(1,10,2):
#     if i < 4:
#         continue
#     print(i,end=' ')
#
# dic = {
#     '商品A': 3,
#     '商品B': 10,
#     '商品C': 7,
#     '商品D': 5
# }
#
# print('商品一覧')
# 辞書のkeysメソッドは、for key in ['商品A', '商品B', '商品C', '商品D']
# for key in dic.keys():
#     print(key)
#
# # キーの一覧を取り出すときは、わざわざkeysメソッド呼ばないほうが多い
# # for 変すうめい in 辞書オブジェクト
# for key in dic:
#     print(key)
#
#
# print('\n商品と在庫数の一覧')
# for key, value in dic.items():  # このitemsを使ったを暗記したい
#     print('商品名：' + key + '\t在庫数：' + str(value))
#

# dic.items()
# 次のようなリストを作る
# tuple_list = [
#     ('商品A', 3),
#     ('商品B', 10),
#     ('商品C', 7),
#     ('商品D', 5)
# ]
#
# for key, value in tuple_list:
#     print(key)
#     print(value)
#
#
# key, value = ['商品A', 3]

# numlist = [[i for i in range(1,3)],[j for j in range(3)]]
# print(numlist)

def say_hello(s,h):
    print('say hello' + s + h)


say_hello(s = 'a', h ='f')

# def kazu(number):
#     for j in range(2, number):
#         if i % j == 0:
#             return  False
#     return True
#
# for i in range(2,101):
#     if kazu(i):
#         print(i)

def tax(price):
    tax = int(price * 0.1)
    return tax

def tax2(price):
    tax = int(price * 0.1)
    price_tax = int(price + tax)
    return (price_tax,tax)


def message(s=None):
    if s is not None:
        print('入力文字列は「' + s + '」です')
    else:
        print('未入力')


a = tax(75)
b = tax(100)
c, d = tax2(100)
print(a)
print(b)
print(c)
print(d)
message()
message('Hello')

# 関数の外側で定義した変数は、関数の中からでも見れる
# 関数の中で定義した変数は、関数の外に出ると消滅する
# 関数の中、外側の変数を書き換えることは(基本的に)できない

def hello():
    #グローバルを書くと、ちゃんと変更される
    global a
    a = 1

a = 10
hello()
print(a)

class Character:
    def speak(self,commnet):
        print(self.name + ':' + commnet)
    def __init__(self,name,comment):
        self.name = name
        self.comment = comment
    def speak2(self):
        print(self.name + ':' + self.comment)
chara = Character('タロー','こんにちは')
# chara.name = 'taro
chara.speak('hello')
chara.speak2()