import abc
from abc import abstractmethod


class AbstractView(metaclass=abc.ABCMeta):

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def barChart(self):
        pass

    @abstractmethod
    def pieChart(self):
        pass


