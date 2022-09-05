def initialiser(name: str, should_be_upper_case: bool = False) -> str:
    if should_be_upper_case:
        return name[0 : 1].upper()
    else:
        return name[0 : 1]

