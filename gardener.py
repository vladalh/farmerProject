class Gardener:
    """
    Create a gardener and activate his work
    """

    def __init__(self, name, plant):
        """
        Create a gardener and a plant he cares for
        """
        self.name = name
        self._plant = plant


    def work(self):
        """
        Making the gardener work until the fruits ripen
        """
        print(f"{self.name} keep working")
        self._plant.grow_all()


    def harvest(self):
        """
        If all the fruits are ripe, we harvest
        """
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("All fruits are ripe")
        else:
            print(f"{self.name}, Your plant is not mature yet!")


    @staticmethod
    def knowledge_base():
        """
         Gardening Help
        """
        print("Gardening should be done with love, then the harvest will always be good.")