import random

mili = 62.37
kilometri = 100


# enter = input()
# coef = float(enter)


def assort(coef):
    Error = mili - (kilometri * coef)
    print("Your error")
    print(Error)


# assort(coef)


def assert_auto(main_dep, second_dep, learning_rate, accur, epoch):
    coef = random.uniform(0, 1)
    for i in range(epoch):
        error = second_dep - (main_dep * coef)
        if error > 0:
            coef += learning_rate
            print(error)
            print(coef)
            if error < accur:
                print("our final score")
                print(coef)
                return
        elif error < 0:
            coef -= learning_rate
            print(error)
            print(coef)
            if error > -accur:
                print("our final score")
                print(coef)
                return


enter_lr = input("enter the learning_rate")
lr = float(enter_lr)

allow_error = input("enter the allow error of neuro")
accur = float(allow_error)

enter_epoch = input("enter epoch")
epoch = int(enter_epoch)

assert_auto(kilometri, mili, lr, accur, epoch)

# адаптиовать функцию assert_auto на слишким выский коэфицент
# пишем дополнительный if
# найти в документации стандартную функцию, что питон коэфицент генерировал от 0 до 1
# потестить на дюймах и сантиметрах
# любая валюта






