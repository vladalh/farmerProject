from tomato import Tomato
from tomato_bush import TomatoBush
from gardener import Gardener

user_name = input("Enter gardener's name ")
number = int(input())

if __name__ == '__main__':
    Gardener.knowledge_base()
    user_tomato_bush = TomatoBush(number)
    gardener = Gardener(user_name, user_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()

