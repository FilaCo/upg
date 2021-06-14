from ui.cli.command import Command


class Group(Command):
    def __init__(self):
        self.__children = []

    def render(self):
        map(lambda x: x.render(), self.__children)

    def add(self, child: Command):
        self.__children.append(child)

    @property
    def children(self) -> list:
        return self.__children
