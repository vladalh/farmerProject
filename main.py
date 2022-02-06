from tomato_bush import TomatoBush
from gardener import Gardener


def main():
    user_name = input("Enter gardener's name ")
    number = int(input("Enter number of tomatoes: "))
    Gardener.knowledge_base()
    user_tomato_bush = TomatoBush(number)
    gardener = Gardener(user_name, user_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
    
    
if __name__ == '__main__':
    main()
