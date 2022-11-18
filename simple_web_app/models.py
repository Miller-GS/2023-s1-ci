from pydantic import BaseModel
from string_validators import (
    Validator,
    LengthValidator,
    DigitValidator,
    LowerCaseValidator,
    EspecialCharacterValidator,
)


class PasswordSchema(BaseModel):
    content: str


class ValidationResponse(BaseModel):
    message: str


class PasswordValidator(BaseModel):
    content: str
    response: ValidationResponse | None = None

    def get_validators(self) -> list[Validator]:
        validators = [
            LengthValidator(),
            DigitValidator(),
            LowerCaseValidator(),
            EspecialCharacterValidator(),
        ]
        return validators

    def password_validate(self) -> ValidationResponse:
        validators = self.get_validators()
        for validator in validators:
            validator.validate(self.content)
        self.response = ValidationResponse(message="OK")
        return self.response
