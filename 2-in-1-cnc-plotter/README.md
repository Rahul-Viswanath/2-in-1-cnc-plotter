# 2-in-1 CNC Plotter

Starter repository for the CNC plotter project listed in Rahul Viswanath's portfolio. The portfolio describes a machine for drawing, plotting, and laser engraving using Arduino, GRBL, and Benbox.

## Starter hardware assumptions

This starter setup assumes an Arduino Uno, a CNC Shield V3, three stepper drivers, two NEMA 17 stepper motors for X/Y, and a Z stepper that raises and lowers a pen. These are example assumptions because the original source files and wiring details were not available.

The repository includes a small GRBL-compatible G-code file in `gcode/pen-test-square.nc`. It is a motion example, not a full CNC controller firmware. The machine controller is assumed to use GRBL; see the official GRBL project for firmware and documentation.

## Before connecting or running

1. Confirm your controller, shield, drivers, motor wiring, and axis directions.
2. Configure GRBL's steps-per-mm, travel limits, and feed rates for your machine.
3. Set the work origin at the lower-left corner of a clear test area.
4. Test with the spindle or laser disabled and the pen lifted. Keep the emergency stop within reach.
5. Start with a small, safe Z-down value and adjust for your actual pen mechanism and surface.

The sample assumes the paper surface is Z=0, pen up is Z=2 mm, and pen down is Z=-0.2 mm. Change those values for your machine before running. Never use the sample with a laser enabled; laser operation needs its own safe configuration and eye protection.

## Repository contents

- `gcode/pen-test-square.nc` — a 20 mm square pen-motion example.
- `tools/generate_square.py` — a small Python utility that generates square test patterns.
- `docs/hardware-and-setup.md` — starter wiring and setup notes.

Generate a different square with:

```sh
python tools/generate_square.py --size 30 --feed 180 --output gcode/my-square.nc
```

The generator assumes a stepper-driven Z pen lift. Review the output and confirm the machine's travel and Z positions before sending it to GRBL.

## Portfolio description

This project explores a compact CNC machine for precision drawing, plotting, and laser engraving. The portfolio credits Arduino, GRBL, and Benbox.

## Status

Starter documentation, a sample motion file, and a square-pattern generator. Update the hardware assumptions and machine settings to match the built machine before using it.

## License

MIT for the original files in this repository. Third-party firmware and software retain their own licenses.
