def get_heat_point(x: int, y: int, type: int, light: bool = True) -> str:
    colors = (
        [
            {"stroke": "#F5F6F7", "fill": "#EFF0F2"},
            {"stroke": "#CEF4D5", "fill": "#CAEFD1"},
            {"stroke": "#9DE1B6", "fill": "#9DDEB4"},
            {"stroke": "#95D1AC", "fill": "#96CEAB"},
            {"stroke": "#95B9A3", "fill": "#95B7A3"},
        ]
        if light
        else [
            {"stroke": "#12171D", "fill": "#12171D"},
            {"stroke": "#0C2C20", "fill": "#123228"},
            {"stroke": "#124326", "fill": "#17472D"},
            {"stroke": "#1C622E", "fill": "#1F6435"},
            {"stroke": "#247B37", "fill": "#267D3E"},
        ]
    )

    return f"""\t<rect x="{x}" y="{y}" rx="2" ry="2" width="10" height="10" stroke="{colors[type]["stroke"]}" stroke-width="1" fill="{colors[type]["fill"]}"></rect>\n"""


def get_svg_base(h: int, w: int, body: str) -> str:
    return f"""
<svg
	xmlns="http://www.w3.org/2000/svg"
	version="1.1"
	xmlns:xlink="http://www.w3.org/1999/xlink"
	xmlns:svgjs="http://svgjs.dev/svgjs"
	viewBox="0 0 {w} {h}"
	opacity="1"
	width="{w}"
	height="{h}"
>
{body}
</svg>
"""
