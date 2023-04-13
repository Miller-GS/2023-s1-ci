from typing import List, Optional

from pydantic import BaseModel

from .string_validators import (
    DigitValidator,
    EspecialCharacterValidator,
    ForbiddenCharactersValidator,
    LengthValidator,
    LowerCaseValidator,
    UpperCaseValidator,
    Validator,
)


class PasswordSchema(BaseModel):
    content: str


class ValidationResponse(BaseModel):
    message: str


class PasswordValidator(BaseModel):
    content: str
    response: Optional[ValidationResponse] = None

    def get_validators(self) -> List[Validator]:
        validators = [
            LengthValidator(),
            DigitValidator(),
            LowerCaseValidator(),
            UpperCaseValidator(),
            EspecialCharacterValidator(),
            ForbiddenCharactersValidator()
        ]
        return validators

    def password_validate(self) -> ValidationResponse:
        validators = self.get_validators()
        for validator in validators:
            validator.validate(self.content)
        self.response = ValidationResponse(message="OK")
        return self.response
