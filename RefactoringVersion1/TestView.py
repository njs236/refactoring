from AbstractView import *

theLog = []

def ClearLog():

    global theLog
    theLog = []

class TestView(AbstractView):

    def show(self, message):
        global theLog
        theLog.append(message)

    def pieChart(self, *args):
        pass

    def barChart(self,*args):
        pass

