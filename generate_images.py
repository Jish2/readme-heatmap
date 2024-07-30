from components import get_heat_point, get_svg_base
from utils import get_heat

gap = 3
block_height = 10
block_width = 10


def generate_images(date_map: dict[int, int], quartiles: list[int], outDir: str = "./"):
    if not date_map or not quartiles:
        raise ValueError("missing arguments")

    body = ""
    dark_body = ""

    for w in range(53):
        for d in range(7):
            x = w * (block_width + gap) + 1
            y = d * (block_height + gap) + 1
            heat = get_heat(date_map.get(w * d, 0), quartiles)
            body += get_heat_point(x, y, heat, True)
            dark_body += get_heat_point(x, y, heat, False)

    h = 7 * (block_height + gap)
    w = 53 * (block_width + gap)

    with open(f"{outDir}result_light.svg", "w") as f:
        f.write(get_svg_base(h, w, body))
    with open(f"{outDir}result_dark.svg", "w") as f:
        f.write(get_svg_base(h, w, dark_body))
