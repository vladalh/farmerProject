class Tomato:
    """
    We plant and control the ripening of tomatoes
    """

    states = {0: "missing", 1: "bloom", 2: "green", 3: "mature"}

    def __init__(self, index):
        """
        We plant tomatoes
        """
        self._index = index
        self._state = 0


    def grow(self):
        """
        In the process of tomato ripening, we transfer it to the next stage
        """
        self._next_state()


    def is_ripe(self):
        """
        Check if the tomato is ripe
        """
        if self._state == 3:
            return True
        return False


    def _next_state(self):
        """
        We move the tomato to the next stage until we reach the last stage
        """
        if self._state < 3:
            self._state += 1
        print(f"Tomat {self._index + 1} is {Tomato.states[self._state]}")

