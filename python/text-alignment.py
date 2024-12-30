# text-alignment.py


def draw_hacker_rank_logo():
    thickness = int(input())  # This must be an odd number
    if thickness % 2 == 0:
        raise ValueError("Thickness must be an odd number.")

    c = 'H'

    # top arrow
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # top of 'H'
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # middle beam of "H"
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # bottom of "H"
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # bottom arrow
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
    
    return None


def main():
    draw_hacker_rank_logo()
    return None


if __name__ == "__main__":
    main()
