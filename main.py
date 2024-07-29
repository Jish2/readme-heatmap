from components import get_heat_point, get_svg_base
from random import randint

gap = 3
block_height = 10
block_width = 10


def main():
    body = ""
    dark_body = ""

    for w in range(53):
        for d in range(7):
            x = w * (block_width + gap)
            y = d * (block_height + gap)
            body += get_heat_point(x, y, randint(0, 4), True)
            dark_body += get_heat_point(x, y, randint(0, 4), False)

    h = 7 * (block_height + gap)
    w = 53 * (block_width + gap)

    with open("result_light.svg", "w") as f:
        f.write(get_svg_base(h, w, body))
    with open("result_dark.svg", "w") as f:
        f.write(get_svg_base(h, w, dark_body))


if __name__ == "__main__":
    main()
