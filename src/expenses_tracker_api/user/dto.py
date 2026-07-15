from dataclasses import dataclass


@dataclass
class CreateUserInput:
    first_name: str
    last_name: str
    email: str
    password: str
