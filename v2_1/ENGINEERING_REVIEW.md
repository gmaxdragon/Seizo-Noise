# Seizo Noise v2.1: engineering file index and status

**Status: EDITABLE CAD VERIFIED IN SAVED REPORTS; FABRICATION AND PURCHASING HOLD.** Original ESP32/12V v1 remains in the existing `hardware/` and `fabrication/` folders. This newer 5V audio-only prototype is different: it has no ESP32, DAC, onboard microphone, or ultrasonic sensor connector. The USB microphone is external and connects directly to a Raspberry Pi.

## Source

Open `Seizo_Noise_v2.kicad_pro` in KiCad 10 with the schematic, PCB, fp/sym library tables, `.pretty` and symbol libraries in the same directory. The full archive at `../v2_1_full_source.zip` also includes models, original source inputs, previous reports, audit scripts and draft Gerbers.

## System

Raspberry Pi or laptop TRS AUX -> J4 -> R1/R2 stereo-to-mono resistive mix -> RV1 10k audio-taper volume -> J3 four-wire cable -> *external* Adafruit PAM8302. Speaker wires connect only to external PAM8302 `SPK+` and `SPK-`, not PCB GND. A *separate regulated 5V* source enters J1 and feeds amplifier power via PTC F1, Schottky D1 and filter capacitors. The USB mic goes into the Pi, not this PCB.

## Saved digital audit

Archived KiCad 10.0.7 validation: schematic ERC 0 errors/warnings; PCB DRC 0 violations, 0 unconnected pads, and 29/29 schematic-to-board electrical pad assignments matched. No copper, Gerber or native design geometry was modified by this GitHub publication. These are archived results, not a new powered test. See `docs/research/ENGINEERING_RELEASE_AUDIT.md` and `validation/`.

## Real release blockers

- Verify genuine Bourns PTV09A-2020F-A103 support tabs insert and retain securely in the candidate's TWO 3.3mm round plated holes on 8.2mm centers. The manufacturer's recommended layout uses a rectangular opening, so round-hole geometry is a trial-fit compromise.
- Verify Same Sky SJ1-3533NG physically inserts into the THREE 1.1 x 2.2mm plated slots, case clearance and plug access. Verify a fab preview shows THREE PTH slots and four nonplated M3 mounting holes.
- Measure regulated 5.0V adapter output, J1 polarity, current headroom through RXEF075/1N5819 and cable insulation. NEVER use 12V/19V and NEVER backfeed the Pi. Disconnect motors for audio testing.
- Check full landed total including delivery/tax, 5-board fab lot if required, knob, enclosure, standoffs, solder, amp/speaker harness; blank/unquoted costs do not equal $0.
- After assembly check power-off shorts and live voltages, test low-volume speaker output and microphone recording, and confirm there is no automatic robot movement.

**Do not place a PCB order from `fabrication/DRAFT_ONLY` until physical and manufacturer verification.** This publication is not a claim of fabricated, assembled or tested hardware.

## BOMs

- `../BOM.csv`: 17 priced lines ($34.46 at saved catalog/estimated prices), *not* the landed total.
- `../purchasing/BOM_Engineering_v2_1.csv`: additional missing expenses recorded as unquoted.
- `../purchasing/DigiKey_Upload_v2_1.csv`: draft distributor cart, not an order.

The author's Hack Club journal and personal README wording remain unchanged. AI-assisted technical edits to schematic, footprint, route, and analysis are disclosed in the source records.
