# Hardware and setup notes

These notes describe one common starter configuration. They do not confirm the exact parts used in the original build.

## Assumed parts

- Arduino Uno running a GRBL-compatible firmware
- CNC Shield V3
- X/Y stepper motors and drivers
- Z stepper for pen lift
- Pen holder attached to the Z carriage
- Optional laser module, used only after a separate safety and firmware review

## Connection outline

Install the drivers in the X, Y, and Z sockets with the correct orientation. Connect each motor to its matching driver output and connect the shield to the Uno. Set driver current limits for the specific motors and drivers. Confirm the shield's supply voltage and motor wiring before powering it.

Do not connect a servo directly to a GRBL pin based on these notes. Standard GRBL does not provide a generic hobby-servo pen-lift output; a servo-based build needs compatible firmware and wiring.

## GRBL setup

Use a sender compatible with GRBL to connect over USB. Determine the machine's steps per millimeter from its mechanics, then configure travel, acceleration, and feed limits conservatively. Check axis direction and homing behavior with motors disabled or at low power first.

## Test sequence

1. Test X and Y motion with the pen lifted and no tool enabled.
2. Verify that soft limits and limit switches behave as expected.
3. Set Z=0 at the paper surface and verify that the pen clears the page when raised.
4. Run the square file at low feed rate with an emergency stop ready.
5. Adjust pen pressure and Z values in small increments.
