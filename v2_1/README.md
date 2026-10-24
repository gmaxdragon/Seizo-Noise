# Seizo Noise v2.1 — CHECKED CAD / HOLD FOR PHYSICAL RELEASE

This project is the **new, simpler 5V analog speaker/interface board** for Seizo. It is **not** the old ESP32/12V board.

## Open in KiCad

1. Extract the complete ZIP into one folder (do not pull out just the PCB file).
2. Open `Seizo_Noise_v2.kicad_pro` in **KiCad 10**.
3. Open the schematic and PCB through the project manager, preserving `Seizo_V2_Symbols.kicad_sym`, `Seizo_Noise_v2.pretty`, the local library tables, and `models/`.
4. To rerun checks, use Inspect -> Electrical Rules Checker in the schematic and Inspect -> Design Rules Checker in the PCB, with **Refill zones** and **Test for schematic parity** enabled.

**Revision v2.1 moves the AUX jack closer to the board edge, shifts the volume shaft farther toward the right edge, corrects a discovered 10.0mm-vs-8.2mm potentiometer mounting-tab footprint mismatch, and enlarges the jack insertion slots; see `docs/research/ENGINEERING_RELEASE_AUDIT.md`.**

The project was created from the user-uploaded `sz2(1).kicad_sch` and intentionally discarded its empty `.kicad_pcb` placeholder. The upload used `5V_AUDIO` and `+5V_AUDIO` for different nets, leaving the amp connector without the intended protected supply; v2 merges them into the single `+5V_AUDIO` rail.

## What it does

- Audio from a Raspberry Pi or laptop goes to J4 (Same Sky SJ1-3533NG, 3.5mm stereo AUX).
- R1/R2 (4.7k each) isolate and combine left and right to mono.
- RV1 (Bourns PTV09A-2020F-A103) controls analog volume, and R3 (100k) pulls the amp input to ground.
- External protected **regulated 5V only** enters J1. F1 is a 0.75A-hold PTC, D1 is a 1N5819 Schottky (PIN1/cathode on the downstream +5V rail), and C1/C2 stabilize the rail.
- J3 connects by four labelled wires to the **separately purchased Adafruit PAM8302 (product 2130)**: pin1 VIN, pin2 GND, pin3 A+, pin4 A−/GND.
- The **speaker attaches directly to PAM8302 SPK+/SPK−**; do not run speaker output to J3 or board GND.
- The USB microphone connects **directly to the Pi**, not to this board. The Pi performs speech recognition and Seizo's supervised action-validation process.

## Native verification evidence

On KiCad CLI 10.0.7, first in the original local build and then **again in a clean copied project directory**:

- ERC: **0 errors, 0 warnings**.
- DRC: **0 violations, 0 unconnected pads, 0 footprint errors** with ground refill and schematic-to-PCB parity.
- Independent pad/net comparison: **29 assigned electrical pad connections, no mismatches**.
- Board: **85 x 60 mm; 2 copper layers; nominal 1.6mm; 4 x M3 NPTH holes; 14 electrical footprints; 4 mounting footprints**.
- Routing: routed copper traces on B.Cu with a F.Cu GND pour; independent audited segment count is in `validation/INDEPENDENT_RELEASE_AUDIT.json`.
- Drill preview: 31 plated holes (including three routed 2.2×1.1mm AUX plated slots and two oversized 3.3mm plated potentiometer mounting holes); 4 unplated 3.2mm M3 mounting holes; PTH/NPTH drills separate.

Updated reports are under `validation/`; the final v2.1 3D preview is `docs/plots/Seizo_Noise_v2_1_CAD_RENDER.png`. **This is digital CAD validation only, not a physical or electrical functional demonstration.** Existing KiCad ignored-check categories are disclosed in the reports; no new DRC exemption was added to hide copper/clearance faults.

## Ordering status — HOLD

The `fabrication/GERBERS_DRAFT_DO_NOT_ORDER` folder is a complete native Gerber/drill **preview**. **Do not send it to fabrication yet**, even though KiCad checks pass. Exact procurement and mechanical-fit review must precede release; see `docs/TOMORROW_HANDOFF.md` and `docs/ASSEMBLY_AND_TEST.md`.

Purchasing lists from v1 are **not valid for this new board**. The user reports owning a 5V 1A adapter but its loaded voltage, connector fit and polarity have not been independently measured; remaining components and their physical fit are unverified. The 65-dollar Hack Club project target has not been reconciled as a delivered purchase quote.

## Links to primary hardware documentation

- [Same Sky SJ1-3533NG jack datasheet](https://www.sameskydevices.com/product/resource/sj1-353xng.pdf)
- [Bourns PTV09A dimensions](https://www.bourns.com/docs/product-datasheets/PTV09.pdf)
- [Littelfuse RXEF075 PTC datasheet](https://www.littelfuse.com/assetdocs/littelfuse_ptc_radial_leaded_rxef_datasheet?assetguid=e9a7b6b3-79ce-478c-a39a-0a70ee48ccec)
- [Adafruit PAM8302 product 2130 pinouts](https://learn.adafruit.com/adafruit-pam8302-mono-2-5w-class-d-audio-amplifier/pinouts)

AI assistance was used in this CAD revision for net correction, footprint generation, placement, routing, native checks, and documentation. This does not replace the author's KiCad work and does not claim assembled-hardware testing.
