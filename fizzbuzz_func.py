def fizzbuzz():
    for i in range(1,20):
        if i % 15 == 0:
            print('FizzBuzz')
            continue
        if i % 5 == 0:
            print('Buzz')
        if i % 3 == 0:
            print('Fizz')
        else:
            print(i)