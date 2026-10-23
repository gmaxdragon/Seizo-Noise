# Seizo Noise engineering status

**Purchasing and fabrication are paused. The current mixed CAD and buying instructions are not a released assembly design.**

Review: October 22, 2026 Pacific time. Source snapshot: `2e83e959f38a16fd6a22fe580d14751d571b7039`. This is an AI-assisted technical review, not an owner-written development journal or a grant submission.

## DRC diagnosis

The owner's October 22 21:11 DRC report contains 81 messages: 52 missing `Seizo_Audio` footprint-library warnings, 28 USB connector internal pad-clearance errors, and one AUX-jack copper-to-edge error. It reports zero unconnected pads. These are not 81 independent broken circuits or short circuits.

The complete current project was rerun with KiCad 10.0.7: native ERC and DRC pass, including zone refill and schematic parity. Opening the PCB without its companion project/rules/libraries reproduces the same error categories. The isolated reproduction contained 83 messages because it also flagged two zone-edge clearances. A bare PCB download is not an adequate project handoff.

A separate local legacy review copy moves J8 inward 0.35 mm, moves its two connected signal endpoints, sets a 0.50 mm board-edge copper constraint, and includes all project libraries. It passes native ERC/DRC and a fresh-folder retest with zero violations or unconnected items. All original pad/net assignments are preserved. That repaired copy is NOT committed over the main hardware in this update and is NOT the new low-power design. It retains the old 12V circuitry and Pololu regulator footprint. It is supplied separately for review, not fabrication.

## Unresolved assembly issues

- U2 in CAD is Pololu D24V10F3. The lower-cost buying plan uses Adafruit 4711 wired onto selected old pads. It is not a drop-in or a validated matching PCB assembly.
- The saved microphone label is INMP441; the selected Adafruit 3421 is SPH0645LM4H. Carrier J9 and that breakout do not have identical physical pin order. The carrier has WS then data; the breakout has DOUT then LRCLK. Connect by signal only, not by row position. No recording firmware or hardware test has been completed.
- Replaced terminal blocks retain older visual/courtyard representations. Exact purchased-part geometry must match the new assembly definition.
- Native USB connectivity is not working USB microphone firmware. Clean CAD checks do not establish power margin, loudness, microphone quality or household-product safety.

## Recommended simpler architecture for this week

Choose Pi-hosted audio: Pi/laptop analog AUX output -> separate stereo-mixing resistors -> volume control -> a small 5V mono amplifier -> enclosed 4-ohm/3W speaker. Use a finished USB microphone connected directly to the Raspberry Pi for capture. Confirm a free USB port and test the microphone in its intended position.

A PAM8302 module such as Adafruit 2130 is a documented reference candidate, not an approved substitution on the old 12V rail. Its 2.5W headline is specified at 5.5V and 10% THD. Design for roughly 1-2W usable indoor speech output, then measure/test. Never apply 12V to this module; its supply maximum is 5.5V. Neither bridged speaker terminal connects to ground.

A dedicated regulated 5V/1A supply is a reasonable amplifier-only starting point. It is not a demonstrated whole-robot supply. Keep the Pi's existing supply separate and do not backfeed host USB. Protection, cable rating and peak current still need a final calculation and test.

Defer the duplicate bare ESP32, its USB programming and 3.3V subsystem, the unpurchased PCM5102 DAC, unused source selector and extra ultrasonic/UART/I2C expansion from the simplified audio board. Those functions remain possible on the robot controller or a later integrated revision. Displays remain separate next-week work.

This deliberately gives up standalone ESP32 voice/audio operation. Speech processing stays on the Pi. Start with push-to-talk or listen-then-speak; do not claim untested far-field wake-word reliability or echo cancellation.

## What is and is not finished

The old design has been audited and its project/edge-clearance repair tested locally. The proposed lower-power replacement has NOT been routed or released. No new BOM, cart, purchase, grant submission or motor command was created by this review. Existing CSVs and fabrication exports are historical until a consistent design is approved.

Use $65 as the conservative total target. With approximately $20 reserved for delivery/tax, aim around $45 or less for hardware, PCB and all required cables/connectors. This is a planning cap, not a verified delivered quote; nothing is assumed already owned or free.

Before ordering: reconcile exact modules, connectors, power, footprints and physical mounting; finish the new schematic/layout; rerun native ERC/DRC with parity; verify a clean-folder open and complete delivered cost. After assembly: continuity/polarity, controlled first power, measured rails, audio and microphone tests, clipping/thermal observations, host reconnects, strain relief and enclosure checks. No digital check can replace these physical tests.

Robot motion must remain independently constrained and supervised. Motor disable and a physical stop must not depend on audio recognition or an AI/network response. No motion was enabled by this work.

## Primary references

- [KiCad PCB documentation](https://docs.kicad.org/10.0/en/pcbnew/pcbnew.html)
- [TI TPA3118](https://www.ti.com/product/TPA3118D2)
- [PAM8302 module specifications](https://www.adafruit.com/product/2130)
- [Enclosed 4-ohm/3W speaker reference](https://www.adafruit.com/product/3351)
- [I2S microphone pinouts](https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/pinouts)
- [USB microphone reference](https://www.adafruit.com/product/3367)
- [JBL Go 4 specifications: 4.2W output](https://www.jbl.com/GO-4.html)
- [Current assembly mismatch record](docs/Low_cost_assembly.md)
