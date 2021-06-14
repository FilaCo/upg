from ui.cli.group import Group


class Menu(Group):
    def __init__(self):
        super().__init__()

        self.__current = 0

    @property
    def current(self) -> int:
        return self.__current

    @current.setter
    def current(self, value) -> None:
        if value < 0:
            raise ValueError("current element: %d < 0" % value)
        menu_len = len(self.children)
        if value >= menu_len:
            raise ValueError("current element: %d >= menu length: %d" % (value, menu_len))

        self.__current = value
