from tomato import Tomato


class TomatoBush:
    """
    We create a list of tomatoes and control their ripening, after harvesting we clean the list
    """

    def __init__(self, number):
        """
        accept a list of tomatoes and create a list of tomatoes
        """
        self.tomatoes = [Tomato(i) for i in range(0, number)]


    def grow_all(self):
        """
        Transfer all objects from the list tomatoes for the next stage of ripening
        """
        for tomat in self.tomatoes:
            tomat._next_state()


    def all_are_ripe(self):
        """
        If all tomatoes are ripe, then the method returns Тrue
        """
        return all([tomat.is_ripe() for tomat in self.tomatoes])


    def give_away_all(self):
        """
        Clearing the list of tomatoes after harvesting
        """
        self.tomatoes.clear()
