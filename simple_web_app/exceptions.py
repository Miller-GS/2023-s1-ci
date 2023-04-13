from fastapi import HTTPException


class InvalidPasswordException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)


class MinimumLengthException(InvalidPasswordException):
    pass


class NoDigitException(InvalidPasswordException):
    pass


class NoLowerCaseException(InvalidPasswordException):
    pass


class NoUpperCaseException(InvalidPasswordException):
    pass


class EspecialCharacterException(InvalidPasswordException):
    pass

class ForbiddenCharactersException(InvalidPasswordException):
    pass