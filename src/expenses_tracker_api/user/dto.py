from dataclasses import dataclass


@dataclass
class CreateUserInput:
    first_name: str
    last_name: str
    email: str
    password: str


@dataclass
class UpdateUserInput:
    first_name: str | None
    last_name: str | None
    email: str | None
    password: str | None
