def initialiser(name: str, shouldBeUpperCase: bool = False) -> str:
    if shouldBeUpperCase:
        return name[0 : 1].upper()
    else:
        return name[0 : 1]

