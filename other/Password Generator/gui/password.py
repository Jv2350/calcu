import secrets


def create_new(length: int, characters: str) -> str:
    return "".join(secrets.choice(characters) for _ in range(length))
