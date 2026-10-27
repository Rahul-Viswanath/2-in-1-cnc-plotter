#!/usr/bin/env python3
"""Generate a simple GRBL G-code square for a pen plotter."""

import argparse
import sys
from pathlib import Path


def build_gcode(size_mm: float, feed_mm_min: float, z_up_mm: float, z_down_mm: float) -> str:
    if size_mm <= 0:
        raise ValueError("size must be greater than zero")
    if feed_mm_min <= 0:
        raise ValueError("feed must be greater than zero")
    if z_up_mm <= z_down_mm:
        raise ValueError("z-up must be greater than z-down")

    xy = f"{size_mm:.3f}"
    up = f"{z_up_mm:.3f}"
    down = f"{z_down_mm:.3f}"
    feed = f"{feed_mm_min:.1f}"

    return "\n".join(
        [
            f"(Generated pen-test square: {size_mm:g} mm per side)",
            "G21",
            "G90",
            "G94",
            "G17",
            "G54",
            f"G0 Z{up}",
            "G0 X0.000 Y0.000",
            f"G1 Z{down} F60",
            f"G1 X{xy} Y0.000 F{feed}",
            f"G1 X{xy} Y{xy}",
            f"G1 X0.000 Y{xy}",
            "G1 X0.000 Y0.000",
            f"G0 Z{up}",
            "M5",
            "M30",
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=float, default=20.0, help="square side length in mm (default: 20)")
    parser.add_argument("--feed", type=float, default=240.0, help="XY feed rate in mm/min (default: 240)")
    parser.add_argument("--z-up", type=float, default=2.0, help="pen-up Z position in mm (default: 2)")
    parser.add_argument("--z-down", type=float, default=-0.2, help="pen-down Z position in mm (default: -0.2)")
    parser.add_argument("--output", type=Path, help="output file; omit to write G-code to stdout")
    args = parser.parse_args()

    try:
        gcode = build_gcode(args.size, args.feed, args.z_up, args.z_down)
    except ValueError as error:
        parser.error(str(error))

    if args.output:
        args.output.write_text(gcode, encoding="utf-8", newline="\n")
    else:
        sys.stdout.write(gcode)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
