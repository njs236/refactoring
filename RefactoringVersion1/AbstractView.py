import abc
from abc import abstractmethod


class AbstractView(metaclass=abc.ABCMeta):

    def __init__(self, message=None):
        if message is not None:
            print(message)

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def barChart(self):
        pass

    @abstractmethod
    def pieChart(self):
        pass


