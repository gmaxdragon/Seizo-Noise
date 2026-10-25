# Seizo Noise v2.1: independent engineering audit

**Audit date:** October 24, 2026 Pacific (native KiCad checks October 25 UTC)  
**Classification:** **DIGITAL CAD PASS. DESIGN-STAGE SUBMISSION CANDIDATE. PHYSICAL MANUFACTURING RELEASE: HOLD.**

This report applies only to Seizo Noise v2.1, the 85 x 60 mm two-layer 5V audio carrier, with 45 new B.Cu GND track segments and GND fills on both sides. It does not apply to the earlier 12V ESP32 v1, Modular Pi HAT, or physical robot-control electronics.

## What is independently verified

| Verification item | Result | Evidence / limitation |
| --- | --- | --- |
| Native KiCad 10.0.7 schematic ERC | PASS: 0 errors, 0 warnings | GitHub Actions run 40157634443, reports included |
| Native KiCad 10.0.7 PCB DRC | PASS: 0 reported violations, 0 unconnected pads, 0 footprint errors | With zone refill and schematic parity. See existing checker exclusions below |
| Fresh-branch KiCad source validation | PASS | Native CI run on exact reviewed branch commit `2cfb1bfc3f644f368587cfb322da2c3e17ca420e` |
| Independent schematic-to-PCB pin mapping | PASS: 29/29 | Compared archived XML netlist with actual board pad nets |
| Independent connectivity of each electrical net | PASS: 8/8 | Shapely union of 221 track segments and their pad copper, all nets one connected component, including ground |
| Explicit ground routing | PASS: 45 x 0.45mm tracks, nine GND pads | Total approximately 216.73 mm. F.Cu GND zone 1 fill polygon, B.Cu 3 fill polygons. All ground pads connected on B.Cu tracks |
| Board dimensions | PASS: 85 x 60mm | Edge.Cuts board rectangle parsed from source; nominal 1.6mm, 2 copper layers |
| Component pad positions | PASS nominal | J4 T/R/S positions match 2.4 and 7.9mm distances in manufacturer drawing. Pot 5.0mm pin span and 8.2mm support-tab centers match Bourns drawing |
| Fabrication data integrity | PASS | All 10 Gerber/Excellon files byte-identical to the successfully validated KiCad workflow export; ZIP integrity tests pass |
| Plated AUX slots, nonplated mounting holes | PASS digital | 3 J4 oval plated slots (2.2 x 1.1mm), 4 x 3.2mm NPTH M3 holes |
| DigiKey order-list alignment | PASS (list consistency) | 16 SKU rows, 17 pieces total, $30.46 saved unit prices; cart and shipping NOT verified |
| Original non-ground netlist and routing | PRESERVED | 176 non-GND track segments remained unchanged during GND fix |
| Actual powered operation or long-term electrical safety | **NOT TESTED** | No physical PCB or components assembled; cannot certify |

**Source traceability:** PCB SHA-256 `3e3fba5dd51b5f0ef5532a5558262cdd194abae27d6753fc8da3e996ed662f01`; JLCPCB Gerber ZIP SHA-256 `ad3efe8985af011c23d664b8237302d8a878e47cb036e4870b62a01ddd7eb537`. Independent machine-readable results are in `verification/independent_verification.json` and `verification/bom_independent_checks.json`.

**Native verification:** [successful GitHub Actions run](https://github.com/gmaxdragon/Seizo-Noise/actions/runs/40157634443). The saved KiCad project rule set ignores the following categories: missing footprint courtyards; via-centered track endpoints; tuning profile geometry; footprint symbol-filter mismatch; pad component-type matching. No evidence of new exclusions added to force a pass. A zero-count DRC is not a mechanical safety test.

## Circuit behavior verified on schematic/net level

1. The 5V input is **J1 pin 1**; J1 pin 2 is ground. J1+ travels through RXEF075 F1 and forward-biased 1N5819 D1 (cathode toward protected rail). D1 feeds filtered +5V_AUDIO at J3 pin 1 and TP1. The amp receives ground on J3 pin 2 and TP2.
2. Stereo input jack SJ1-3533NG connects tip/ring individually through R1/R2 (4.7k) to AUDIO_MIX. It never directly shorts left and right together. RV1 (10k logarithmic taper) wiper goes to J3 pin 3 A+, and R3 (100k) pulls that node toward GND. RV1 pin 1 is GND.
3. J3 pin 4 is audio A-/GND and must connect to the separate Adafruit PAM8302 module's A-. The PAM8302 `SPK+` and `SPK-` are a bridge-tied speaker output and **must never be connected to ground**.
4. The selected USB microphone is external and plugs directly into the Raspberry Pi. This PCB has no microphone circuit, ESP32, ultrasonic sensor connection, DAC, firmware or motor authorization. It cannot automatically make voice recognition or robot motion work.

## Manufacturing HOLD items

**B1. Bourns potentiometer board locks: primary mechanical hold.** Manufacturer PTV09A-2 drawing recommends two **2.2 x 1.8mm rectangular openings** at 8.2mm spacing. The current board uses two **3.3mm round plated holes** at that spacing, an intentional compromise. The geometry is digitally manufacturable but mechanical retention/soldering strength are **unverified**. Obtain the genuine Bourns part and compare both clip dimensions and real insertion/retention in an approved prototype or dimensional sample. Do not assume the shaft and knob clear a future panel.

**B2. Same Sky AUX jack insertion.** Current J4 pad centers and net numbering match the manufacturer nominal drawing. Board uses 2.2 x 1.1mm plated slots, wider than the nominal 2.0 x 1.0mm footprint recommendation. JLCPCB states minimum plated-slot width 0.5mm and length at least 2x width, so the nominal design is within public published limits. Whether the actual plated holes pass the jack terminals and allow the full plug to enter an enclosure remains a physical check. Upload Gerbers and inspect the *selected fabrication job* including the three slots.

**B3. Regulated power and current.** Identify an actual **5V DC** regulated supply, check polarity, at least 1A nominal rating, and supplier overcurrent protection. **No 12V/19V, no direct Raspberry Pi power rail, and no linking of two +5V sources.** The 1N5819 drops voltage; RXEF075 0.75A hold current derates with heat and does not impose a precise 0.75A ceiling. The PAM8302 may distort or trip the PTC near full volume. Test measured +5V_AUDIO voltage at TP1 vs TP2 and amp temperature under increasing audio load. The design does not provide **overvoltage protection** against wrong higher-voltage adapters.

**B4. Assembly/board body.** Confirm 4×M3 standoffs/screws, two separate module mounting areas, at least a four-wire short amp harness, full jack plug access, 6mm D-shaft knob engagement, and safe speaker wire insulation. J3 is a **male header**, not a keyed connector, so swapped wires can destroy the amplifier. Connect only from the verified J3 pin numbers and use keyed/labelled harnessing.

**B5. True landed cost.** Saved price subtotal: $30.46 DigiKey components + $4 placeholder PCB = $34.46. Does not include shipping, tax, actual fab lot quantity, actual 5V supply/replacement, M3 mounting, enclosure, solder or any adapter not owned. The order/cart totals and per-part stock are unverified. Two items (AUX cable and wire) were recently shown with low stock by DigiKey; check the live cart.

**B6. Powered acceptance.** With motors disconnected and amp disconnected, unpowered meter check J1+/GND and no short; then first power from a fused/current-limited verified 5V source; measure J1 and TP1/TP2 with no load. Power off to connect amplifier (VIN, GND, A+, A-); at low laptop/Pi volume connect isolated speaker to amplifier `SPK+`/`SPK-` and gradually check output/noise, voltage sag, heat and sustained behavior. Connect USB microphone directly to Pi and test independent recording/playback. Do not enable robot automatic motion.

## Fit-check printout

`verification/Seizo_Noise_v2_1_1to1_Fit_Check.pdf` is generated from actual KiCad pad positions. Print on US Letter at 100% size and measure its 50mm scale bar before placing the real potentiometer and jack to check nominal hole alignment. Paper cannot simulate drill plating, solder fillet retention or mechanical load; it is a low-cost preliminary fit aid only.

## Hack Club submission distinction

The files support a **design-stage submission as an unbuilt prototype**, with native KiCad project, Gerbers, realistic BOM, design screenshots, honest personal progress and AI assistance disclosure. Submission approval is not guaranteed. A price screenshot cannot certify physical operation. Do not call the board assembled, fully tested, or electrically safe for unattended use.

## Source references

- [Bourns PTV09A series datasheet](https://www.bourns.com/docs/product-datasheets/PTV09.pdf)
- [Same Sky SJ1-3533NG manufacturer drawing (archived)](https://datasheet.octopart.com/SJ1-3533NG-CUI-datasheet-32236.pdf)
- [JLCPCB PCB capabilities (plated slots, annular ring and drilling)](https://jlcpcb.com/capabilities/pcb-capabilities/)
- [Adafruit PAM8302 pinouts](https://learn.adafruit.com/adafruit-pam8302-mono-2-5w-class-d-audio-amplifier/pinouts)
- [Littelfuse RXEF075 listing (0.75A hold, 1.5A trip)](https://www.digikey.com/en/products/detail/littelfuse-inc/RXEF075/5015922)
- [Hack Club Half Life](https://halflife.hackclub.com/)