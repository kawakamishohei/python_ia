import fizzbuzz_func


# def fizzbuzz():
#     for i in range(1,20):
#         if i % 15 == 0:
#             print('FizzBuzz')
#             continue
#         if i % 5 == 0:
#             print('Buzz')
#         if i % 3 == 0:
#             print('Fizz')
#         else:
#             print(i)
#
# def fizzbuzz2(start,end):
#     for i in range(start,end+1):
#         if i % 15 == 0:
#             print('FizzBuzz')
#             continue
#         if i % 5 == 0:
#             print('Buzz')
#         if i % 3 == 0:
#             print('Fizz')
#         else:
#             print(i)
#
#
# fizzbuzz()
# fizzbuzz2(start=10,end=20)

class Character:

    def __init__(self, name, age, item):
        self.name = name
        self.age = age
        self.item = item

    def speak(self, comment):
        print(self.name + ':' + comment)

# デバッグなど、人間が見やすいクラスの文字列表現を返そう
    def __str__(self):
        return f'Character({self.name})'

# class クラス名(継承元):
class Healer(Character):

    # __init__も上書きできます
    def __init__(self, name, age, item, heal_power):
        # 親クラスのメソッドを呼ぶ
        # super().親クラスのメソッド名(親で必要な引数...)
        # super()関数の引数は、今は空でよいです
        super().__init__(name, age, item)
        self.heal_power = heal_power

    # オーバーライド
    # 親クラスのspeakは呼ばれなくなる
    def speak(self, comment):
        # 親のspeakも読んでみる
        super().speak(comment)
        print('私はヒーラーです')

    # 新規追加のメソッド
    def healing(self):
        print(f'{self.name}は回復した！')


taro = Healer('tarou',20,'きびだんご',10)  # インスタンスか
taro.speak(comment='ハロー')
taro2 = Character('tarou',10,'き')
print(taro2)
# fizzbuzz_func.fizzbuzz()
from fizzbuzz_func import fizzbuzz
fizzbuzz()
print(taro.name)
# 定義だけしたい場合にpass文を使う(エラーにならなくなる)
# def hello():
#     pass

class Character:
    def __init__(self, name, level, exp, itembox):
        self.name = name
        self.__level = level
        self.__stamina = level * 20
        self.exp = exp
        self.itembox = itembox

    # ゲッターメソッド
    @property
    def stamina(self):
        return self.__stamina

    # セッターメソッド
    @stamina.setter
    def stamina(self, new_stamina):
        # 体力の最小値は0、最大値はレベル×20
        if new_stamina > self.__level * 20:
            self.__stamina = self.__level * 20
        elif new_stamina <= 0:
            self.__stamina = 0
            print(self.name + 'は力尽きた')
        else:
            self.__stamina = new_stamina


taro = Character('タロー', 1, 0, {'かいふくやく': 2})
taro.stamina = 200
print(taro.stamina)
taro.stamina = -10
print(taro.stamina)