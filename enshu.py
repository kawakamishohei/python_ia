# data_dict = {}
# userdict = {}
# key = input('keyを入力してください > ')  # 辞書のkeyを入力してもらう
# value = input('valueを入力してください > ')  # 辞書のvalueを入力してもらう
# data_dict[key] = value
# userdict = data_dict
# print(data_dict.items())
# print(data_dict[key])
# print(data_dict.get(key))
# print(data_dict.get('age','ありませんでした'))

# for i in range(1,20):
#     if i % 15 == 0:
#         print('FizzBuzz')
#         continue
#     if i % 5 == 0:
#         print('Buzz')
#     if i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)

for k in range(2,100):
    for l in range(2,k):
        if k % l == 0:
            break
    else:
        print(k)

