def queen_attack(pos1,pos2):

    # exceptions for out of bounds
    if pos1[0] < 0 or pos1[0] > 7:
        raise ValueError("Queen out of bounds")
    if pos2[0] < 0 or pos2[0] > 7:
        raise ValueError("Queen out of bounds")
    if pos2[1] < 0 or pos2[1] > 7:
        raise ValueError("Queen out of bounds")
    if pos1[1] < 0 or pos1[1] > 7:
        raise ValueError("Queen out of bounds")

    # exceptions for same spot
    if pos1 == pos2:
        raise ValueError("Queens cannot be on same square!")

    # queens share column or row
    if pos1[0] == pos2[0] or pos1[1] == pos2[1]:
        return True

    # queens share diagonal
    if pos1[0] - pos2[0] == pos1[1] - pos2[1]:
        return True

    # no match
    return False

# TRUE
print(queen_attack((0,0),(2,0)))
print(queen_attack((0,0),(2,2)))
print(queen_attack((0,0),(0,2)))
print(queen_attack((0,0),(7,7)))
print(queen_attack((7,7),(0,0)))

# FALSE
print(queen_attack((0,0),(2,1)))
print(queen_attack((0,0),(4,6)))

# Exceptions
print(queen_attack((0,0),(0,0)))
