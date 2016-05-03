class CustomException(Exception):

    def __init__(self, theReason=""):
        self._reason = theReason

    def __str__(self):
        return repr(self._reason)


class InvalidGenderException(CustomException):

    def __init__(self, theReason="Invalid Gender"):
        super(InvalidGenderException, self).__init__(theReason)


class StringException(CustomException):

    def __init__(self, theReason="Supplied Variable is not a String"):
        super(StringException, self).__init__(theReason)


class InvalidIDException(CustomException):

    def __init__(self, theReason="Invalid ID"):
        super(InvalidIDException, self).__init__(theReason)


class DuplicateIDException(CustomException):

    def __init__(self, theReason="ID Already Taken"):
        super(DuplicateIDException, self).__init__(theReason)


class EnumException(CustomException):

    def __init__(self, theReason="Enum not Committed"):
        super(EnumException, self).__init__(theReason)


class MaxRecordsException(CustomException):

    def __init__(self, theReason="ERP has the Maximum Amount of Records"):
        super(MaxRecordsException, self).__init__(theReason)

class ViewException(CustomException):

    def __init__(self, theReason="Not a View"):
        super(ViewException, self).__init__(theReason)


class InsufficientArgumentsException(CustomException):

    def __init__(self, theReason="Not Enough Arguments Provided"):
        super(InsufficientArgumentsException, self).__init__(theReason)