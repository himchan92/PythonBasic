def open_account():
    print("새로운 계좌를 개설합니다")

open_account()

def deposit(balance, money):
    print("{0}원을 입금했습니다. 잔액은 {1}원 입니다." .format(money, balance + money))
    return balance + money

balance = 1000
balance = deposit(balance, 2000)

def profile(name, age=20, lang="파이썬"):
    print("이름 :{0}\t나이 :{1}\t주 사용언어: {2}".format(name, age, lang))
profile("찰리")
profile("루시")    

def test(name, age, lang):
    print(name, age, lang)

test("철수", 20, "자바")
test("미영", 18, "코틀린")    