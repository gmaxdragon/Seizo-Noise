# Seizo Noise v2.1 — engineering release audit and research

Date: October 23, 2026 Pacific / KiCad timestamps October 24 UTC. **Engineering verification complete for CAD; fabrication and ordering remain on HOLD.** This is an AI-assisted technical record, not a claim of user-performed physical testing.

## Purpose and system boundary

Seizo's existing Raspberry Pi 4 processes USB microphone input and supervises action proposals; motor permissions are not provided by this audio PCB. Raspberry Pi headphone output -> 3.5mm TRS cable -> the PCB's resistive stereo-to-mono mix -> Bourns knob -> preassembled Adafruit PAM8302 analog amplifier -> enclosed 4-ohm/3W speaker. The microphone plugs **directly into the Pi USB port** (not this PCB), and microphones/speakers are not present in the board's 3D geometry. The Pi retains its own power supply, distinct from the existing user-owned 5V/1A charger proposed for the audio board.

The PCB is a **passive + protected power and audio breakout**, not a USB audio codec, voice-recognition board, autonomous controller, or motor safety component. The separately mounted amplifier requires four short control/power wires (VIN, GND, A+, A−) and two speaker wires; that is an explicit mechanical integration cost. User request to minimize wires cannot be met by describing a separate breakout as soldered on the carrier.

## Changes since v2 (source-derived CAD changes)

- Revision 2.1 has an 85 × 60 mm two-layer board, four unplated 3.2 mm mounting holes, 14 electrical footprints and a front GND plane.
- The 3.5mm AUX J4 center is (30,6)mm, moved 2mm toward the board edge from v2. The jack's three oval plated slots were increased from the nominal 2.0 × 1.0 mm to 2.2 × 1.1 mm to give mechanical insertion allowance, while retaining copper annular rings about 0.30–0.35 mm. JLCPCB's published plated-slot requirement is min 0.5 mm width, length >= 2× width, and ±/tolerance as given below. The exported Excellon includes three G85 slot commands.
- The side-mounted 10k audio Bourns PTV09A-2020F-A103 volume pot moved from (65,26)mm to **(78,26)mm** so the modeled shaft end extends ~9.8mm past the board's x=85mm edge. The available grip after any case wall is unknown until a knob and enclosure are measured. **No panel nut is assumed: PTV09A-2 is the bushingless variant.**
- **Significant discovered footprint fault fixed:** the earlier custom potentiometer footprint had mounting tabs separated by 10.0mm. Bourns' PTV09A-2 dimensioned drawing recommends **8.2mm** between the two board-lock holes. The two tab-center pads now use 8.2mm spacing. Earlier nominal 2.3mm round holes were too small to confidently accept tabs for a manufacturer-recommended rectangular mounting aperture of 2.2(+0.2) × 1.8(+0.2)mm. Each is now a 3.3mm PTH round hole, with 4.6mm copper pad (nominal annular ring 0.65mm). **Engineering compromise:** the enlarged round holes accommodate the worst-case nominal tab diagonal in theory and are fabricable, but let the tabs float more until soldered; the exact mechanical fit and retention MUST be verified with one purchased genuine potentiometer and the fabricated board. They do not reproduce the manufacturer's rectangular-hole recommendation exactly. A real part trial-fit is a release blocker.
- Removed warning-heavy silkscreen sentences and retained useful functional labels, reference designators, polarity markers, and `V2.1`. Both AUX and volume component shapes are approximate project-local mechanical STEP envelopes, not exact manufacturer-certified STEP geometry.
- Diode/power input, resistor mixing network, volume netlist, and four-wire amplifier connector **have not been electrically altered** by these mechanical modifications.

## Independently verified (digital evidence)

- KiCad CLI **10.0.7** native schematic ERC: zero errors and zero warnings. KiCad PCB DRC with copper-zone refill and schematic-parity: **zero reported violations, zero unconnected pads, zero footprint errors, and zero parity issues**. Repeated in independent fresh project folder.
- Separate Python pad-to-net audit compares all **29 electrical schematic pin/net pairs** across 14 schematic components against the physical PCB pad nets, preserving the 8 nets; the board also has four mechanical M3 holes and two unconnected metallic potentiometer board-lock tabs.
- Power path: J1 pin1 5V input -> RXEF075 PTC -> 1N5819 Schottky anode pin2 -> cathode pin1 protected `+5V_AUDIO` -> PAM8302 J3 VIN; J1 pin2 is ground. Testpoint TP1 is protected +5V, TP2 GND. Polarized 470µF capacitor C1 + to protected supply.
- AUX contact mapping for **SJ1-3533NG** is **1 sleeve, 2 tip, 3 ring** per current Same Sky manufacturer datasheet. The custom footprint uses pad S=pin1, T=pin2, R=pin3, and R1/R2 4.7k separately mix channels; R3 100k to ground holds the amp input quiet when source absent. J3 connects in order 1 VIN, 2 GND, 3 A+, 4 A−. Speaker connects only to amplifier SPK+/SPK− (bridged output, not GND).
- Fabrication outputs separate F.Cu/B.Cu, masks/silkscreens, Edge.Cuts, **31 plated holes including 3 AUX plated slots and 2 × 3.3mm pot mounting holes**, plus **4 unplated 3.2mm M3 holes**. Generated Gerbers are under `fabrication/DRAFT_ONLY`: **NOT an approved production order**.
- General PCB clearance/silkscreen checks are clear under the stored project rules. Configured KiCad rule exclusions are still declared in reports; nothing has been falsely claimed about untested high-speed impedance or mechanical retention.

## Physical part facts to buy against the approved design (research, NOT a purchase list)

| Designator | Exact part / attribute | Electrical and physical constraint | Primary sourcing evidence |
| --- | --- | --- | --- |
| J1 | On Shore OSTTC022162, DigiKey ED2609-ND | 2-pin 5.08mm through-hole horizontal screw terminal, accept 14–22AWG, body/leg and 1.3mm board hole check | https://www.digikey.com/en/products/detail/OSTTC022162/ED2609-ND/614558 |
| F1 | Littelfuse RXEF075, RXEF075HF-ND | 0.75A **hold** / 1.5A **trip** at specified conditions, 5.05mm lead spacing; NOT an accurate 0.75A current limiter | https://www.digikey.com/en/products/detail/littelfuse-inc/RXEF075/5015922 |
| D1 | onsemi 1N5819G, DigiKey 1N5819GOS-ND | Schottky 40V 1A DO-41; cathode stripe downstream; Vf up to ~0.6V at 1A means amp sees less than 5V | https://www.digikey.com/en/products/detail/onsemi/1N5819G/1474211 |
| C1 | Panasonic EEU-FR1E471, P14419-ND | 470µF 25V polar electrolytic, 10mm diameter, 5mm lead spacing, up to 14mm tall; correct +/- orientation mandatory | https://www.digikey.com/en/products/detail/panasonic-electronic-components/EEU-FR1E471/2433553 |
| C2 | KEMET C052C104K5R5TA, 399-C052C104K5R5TA-ND | 100nF X7R 50V radial 5.08mm pitch, 4.83x2.29mm body, practical 0.8mm board drill | https://www.digikey.com/en/products/detail/kemet/C052C104K5R5TA/12699186 |
| J4 | Same Sky SJ1-3533NG, CP1-3533NG-ND | Through-hole right-angle unswitched TRS, correct S/T/R, manufacturer's recommended 1x2mm slots, released drawing has 1.1x2.2mm oval holes | https://www.sameskydevices.com/product/resource/sj1-353xng.pdf |
| R1,R2 | 4.7k 1/4W through-hole axial, 7.62mm hole spacing | Match 0.85mm holes, body 6.3mm max; no hard-tie of stereo outputs | https://www.digikey.com/en/products/filter/through-hole-resistors/53 |
| R3 | 100k 1/4W through-hole axial, 7.62mm spacing | AMP_IN-to-ground pull-down; no placement under pot mechanism | https://www.digikey.com/en/products/filter/through-hole-resistors/53 |
| RV1 | Bourns PTV09A-2020F-A103, DigiKey PTV09A-2020F-A103-ND | 10k **audio/log** taper, side mount (PTV09A-2), bushingless 20mm shaft; board-lock holes corrected to 8.2mm spacing, oversized round drill trial-fit required | https://www.bourns.com/docs/product-datasheets/PTV09.pdf |
| J3 | 1x4 2.54mm THT pin strip | Four SHORT individually-labelled insulated leads to preassembled PAM8302 (not a module directly plugged into board) | https://learn.adafruit.com/adafruit-pam8302-mono-2-5w-class-d-audio-amplifier/pinouts |
| External amplifier | Adafruit 2130 PAM8302 | Factory assembled, 2.0–5.5V VIN, A− tied to GND for single-ended source, SD open/enable, speaker bridge outputs stay isolated from GND; max power headline 2.5W **at 5.5V, 10% THD** | https://www.adafruit.com/product/2130 |
| Speaker | Adafruit 3351, 4Ω / 3W enclosed | Does not mount on carrier; its lead/connector must match supplied amplifier screw terminals; real acoustic output not tested | https://www.adafruit.com/product/3351 |
| USB mic | Adafruit 3367 example | USB microphone is independent of PCB; needs available Pi USB port or verified powered hub and a suitable position away from fan/speaker | https://www.adafruit.com/product/3367 |

**Power calculations:** A regulated 5V × 1A adapter is nominally 5W, not the previous 12V × 2.5A/30W unit. For illustrative 2W audio output at assumed 85% class-D efficiency and ~4.6V delivered after Schottky/PTC: approximately 0.51A average, below 0.75A PTC hold at room temperature, but real music peaks, 4Ω speaker load, hot PTC derating, cable drop, and capacitor inrush are not measured. The RXEF075's trip specification of 1.5A means **it is not a guaranteed protection against every overload of a 1A-rated adapter**: supplier adapter overcurrent and short-circuit protection must also be checked. Actual input power, distortion and thermal margin must be tested at a safe audible level; allow time for cooldown if PTC trips. Do not assume a barrel jack labeled `5V charger` is regulated/center-positive without checking its specification and measuring loaded output.

**Connection minimization:** The user-owned barrel-to-terminal adapter can connect by two short leads into J1; the current PCB has **no on-board barrel jack**. A direct barrel footprint would require exact plug outer/inner diameter and case details; do not change blindly. Amplifier uses a short four-conductor harness, and speaker uses two directly to amp. Pi AUX and USB microphone use off-the-shelf cables. Pi power remains isolated from J1 so no unverified USB/5V backfeed. Audio sleeve provides the necessary signal ground reference; test hum with both separately powered devices running.

## Fabrication assessment

JLCPCB lists for two-layer boards min plated slot width **0.5mm**, minimum slot length **2× width**, plated-slot hole-size tolerance **+0.13/−0.08mm**, and a recommended 1oz copper PTH annular ring **at least 0.25mm**. The current AUX slots 2.2x1.1 and copper pads 2.8x1.8 have nominal 0.30–0.35mm side rings. Bourns mounting PTH drill3.3 and pad4.6 have ~0.65mm ring, meeting these numerical fabricator capabilities. **This does not guarantee mechanical insertion**, which depends on actual plated-hole tolerances, metal tab corner geometry, and supplier interpretation. Source: https://jlcpcb.com/capabilities/pcb-

**Do not fabricate yet:** request fabrication-preview approval for 3 AUX PTH slots, 2 oversized PTH potentiometer tabs, and 4 NPTH M3 holes; run the full Gerber preview at the chosen fab and verify no feature is inferred as ordinary round through-holes. The component 3D models here are envelope drawings, not manufacturer-validated mechanical representations. Test jack mating and control-knob clearance with the real parts and intended case wall thickness. Small-batch fab may have minimum PCB quantity and disproportionately large shipping; no checkout total recorded.

## Integration and test blockers (release gates)

1. **Adapter:** Verify label says DC output 5V/1A, not merely 'charger'; match exact barrel adapter dimensions and polarity, check no-load and loaded voltage and current, polarity and connector grip. A generic DC plug of unknown dimensions cannot be matched just by visual resemblance.
2. **Potentiometer:** Order or physically measure the specific Bourns A103 first; ensure the side-mounted metal tabs insert into current two 3.3mm round holes and can be soldered securely, confirm 20mm shaft remains sufficiently exposed with actual 3D-printed wall and knob hub, and inspect mechanical strain from turning. The right edge housing model is only approximate.
3. **Jack:** Trial fit SJ1-3533NG's 3 pins in the 1.1x2.2 rounded slots, confirm barrel protrusion through case opening, and stress from repeated headphone-plug insertion. This jack has a quoted mating cycle rating; product-use testing is still absent.
4. **Soldering:** verify 1.0–1.3mm holes accept purchased lead gauges; bend through-hole resistor leads to 7.62mm without stressing body; solder pot metal tabs as anchors. Observe Bourns' <=300C/3s soldering condition as manufacturer guidance where possible. Ensure the volume-control pads are not used as structural anchors for the enclosure.
5. **Electrical power:** multimeter continuity/polarity with power removed, current-limited first power, measure protected testpoint TP1 relative TP2 with amplifier disconnected and loaded, inspect diode/PTC heating and hum. Wrong soldering CAN cause damage; there is no zero-risk solder design.
6. **Audio:** test Pi3.5mm analog output selection, R1/R2 summing from left/right test signals, potentiometer direction and low level, PAM8302 A+ A- connection, then clean speech/music from speaker without clipping or overheating. The separate amplifier's bridge SPK+ and SPK- must never go to PCB GND.
7. **Voice:** verify Pi USB availability given cameras/controllers; run ALSA microphone enumerate-and-record; test the actual live Pi speech software. The Seizo website's browser speech recognition is NOT evidence of installed Pi USB-mic recording. Keep motors disarmed and use proposal-only workflows until independent controls/physical stop and motion limits are verified.
8. **Budget:** source **every** required v2 part, microphone, amplifier, speaker, AUX cable, hookup wires, case/mounting, PCB manufacture minimum quantity, taxes, tariff and shipping; compare delivered total to the user's desired $65. Do not reuse the old v1 BOM or presume an external microphone/adapter exists except the user's reported 5V/1A supply.

## Final classification

- **CAD/ERC/DRC/net/drill audit:** PASS for saved project.
- **Manufacturer dimensional comparison:** PASS for key electrical attributes; **mechanical insertion remains UNVERIFIED**.
- **Part procurement and fitted-assembly mapping:** PARTIAL, no checked complete cart or purchased samples.
- **Power/audio/microphone software integration:** UNTESTED ON HARDWARE.
- **PCB / electronics household-use certification:** NOT CLAIMED.
- **Gerber release / order authorization:** HOLD.

This is a credible, independently checked prototype PCB. It is **not** a validated household-ready commercial product. The next costly step is actual supplier order/fab: do not authorize either based on this CAD report alone.
