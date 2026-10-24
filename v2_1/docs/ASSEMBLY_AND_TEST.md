# Assembly / first test plan — pending physical part verification

## Carrier-mounted parts

| Designator | Exact footprint / planned physical part | Pins and notes |
|---|---|---|
| J1 | On Shore OSTTC022162 5.08mm two-way terminal | 1=external regulated +5V, 2=GND; confirm drill 1.30mm |
| F1 | Littelfuse RXEF075 radial PTC | 0.75A hold (not precise current limiter); pin spacing nominal 5.1mm |
| D1 | 1N5819 axial DO-41 | **Striped cathode = pin1 at downstream +5V_AUDIO** |
| C1 | Panasonic EEU-FR1E471 470uF 25V | 10mm body / 5mm leads; square pin1 +5V, pin2 GND |
| C2 | 100nF 50V ceramic, radial **5.08mm** lead pitch | KEMET **C052C104K5R5TA**; don't buy 2.54mm-only lead pitch |
| J4 | Same Sky SJ1-3533NG TRS jack | `S=GND, T=L, R=R` |
| R1, R2 | 4.7k 1/4W axial, 7.62mm pitch | Isolating stereo-to-mono mixing resistors |
| R3 | 100k 1/4W axial, 7.62mm pitch | AMP_IN to GND bleeder |
| RV1 | Bourns PTV09A-2020F-A103 | 10k audio taper; 1=GND,2=AMP_IN,3=AUDIO_MIX |
| J3 | Through-hole 1x4 male header, 2.54mm pitch | 1=+5V, 2=GND, 3=A+, 4=A−/GND |
| TP1–TP3 | Probeable THT pads, 2.6mm | TP1=+5V, TP2=GND, TP3=A+ / mono audio |

Bourns PTV09A-2 mechanical tabs use enlarged **3.3mm plated mounting holes, 8.2mm center spacing**, not the original incorrect 10.0mm spacing; fit test with the physical part remains mandatory. The headphone jack uses three **1.1×2.2mm plated slots**; these also require physical fit confirmation. Four unplated M3 mounting holes have 3.2mm drills. No 12V rail, bare ESP32, microphone chip, DAC, or motor connection exists on this audio board.

## External system

```
USB mic ─► Raspberry Pi 4 ── audio jack 3.5mm ─► J4 / mixer / volume ─► J3 A+
                                               separate regulated 5V 1A ─► J1
                                   J3 VIN, GND, A+, A− ─► Adafruit PAM8302
                                       amplifier SPK+ and SPK− ─► 4Ω/3W speaker
```

The Pi is **not powered by J1**. Only send 5V to J1. SD on Adafruit PAM8302 can remain unconnected in its normal enabled configuration. Do not feed 12V to the PAM8302. The amplifier is wired externally, so no direct footprint mating is required between its pads and J3; **wire by label**, not by physical row order.

## Soldering, unpowered checks, first power

1. Mount low-profile resistors R1-R3, axial diode D1 (check stripe), ceramic C2, PTC F1, electrolytic C1 (check plus and minus), test pads, header J3, J1, then jack J4 and volume pot RV1; use flux, clean joints, and mechanically support heavy connectors.
2. Before connecting any power, inspect shorts: J1+ versus J1 GND should not be shorted; test C1 polarity, orientation D1, and that fused power cannot bypass F1/D1. Use resistance/continuity carefully: capacitor charging can briefly beep without a true short.
3. With a checked regulated 5V supply connected to J1 alone, measure TP1 relative to TP2: it should be **below the adapter voltage** due to D1 and F1, but comfortably in the 2–5.5V PAM8302 module range. No fixed measured value is claimed in advance. Cut power immediately on unexpected heat, smell, reversed polarity, or a voltage outside the module's rating.
4. With power disconnected, wire J3 pin1 to PAM8302 VIN, pin2 to GND, pin3 to A+, pin4 to A−; connect speaker directly to the amplifier floating SPK+ and SPK− outputs, **not ground**.
5. Begin with the Pi or laptop headphone volume low and RV1 turned down; turn up gradually and listen for clean speech/music without clipping; inspect supply voltage and amplifier/diode/connector temperature.
6. Only after analog playback is verified, connect and test a USB microphone on the Pi with no motors enabled. Confirm recording, replay, device enumeration and recoverability after unplug/reboot. Speech-to-action remains preview/approval-only.

**Do not order/fabricate directly from the included draft Gerbers before the full parts/fit and fab checks listed in `TOMORROW_HANDOFF.md`.**
