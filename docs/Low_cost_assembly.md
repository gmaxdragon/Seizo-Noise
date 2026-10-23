# Lower-cost assembly option

This purchasing option uses the existing Seizo Audio v1.0 PCB copper, but changes the fitted regulator assembly and terminal blocks. It is not a newly validated CAD revision. The saved U2 symbol, footprint and 3D model still describe the original Pololu module. The earlier ERC/DRC reports do not test this wired assembly.

## U2: Adafruit 4711 instead of Pololu 2830

Buy **Adafruit 4711**, DigiKey **1528-4711-ND**, a complete fixed 3.3V breakout, not a bare converter IC. Adafruit's current revision uses TLV62569; some distributor text still names the earlier AP3429A revision. Use the exact product and its printed labels.

**Do not insert it into the five-pin U2 footprint. Do not install the Pololu or its five-pin socket.**

Connect three short insulated wires by net:

| Existing carrier pad | Verified carrier net | Adafruit 4711 pad |
| --- | --- | --- |
| U2 pad 3 | BOARD_5V | Vin |
| U2 pad 4 | GND | GND |
| U2 pad 5 | +3V3 | 3V |
| U2 pads 1 and 2 | Unused in this design | No connection |

The manufacturer specifies 3.4-5.5V input and a 3.3V output. **Never connect this breakout to the 12V amplifier rail.** Leave the breakout's EN in its default enabled configuration; pulling EN low shuts it down. The 1.2A breakout rating does not increase the USB port or F1 current budget.

Keep the three leads short, about 2-3 cm where practical. Use the purchased 22 AWG insulated wire and mark each end. Mount the breakout on an insulating support inside the old module's available area, away from the antenna and audio wiring. Secure it so its underside and solder joints cannot touch the carrier copper, enclosure metal, or other components. Insulating support and strain relief are still required; they are not supplied by the wire pack.

With all power disconnected, check the pad numbers and continuity with a multimeter. Initially leave the breakout's output disconnected from U2 pad 5; with a current-limited 5V source, measure the breakout's output to ground and confirm approximately 3.3V. Disconnect power before connecting the output to pad 5. Then perform separate low-current board, USB and audio bring-up checks. No physical regulator or board test was performed in this purchasing update.

Source: [Adafruit 4711 product and pin information](https://www.adafruit.com/product/4711).

## J3 and J4 terminal blocks

Use **On Shore OSTTC022162**, DigiKey **ED2609-ND**, quantity 2.

The [manufacturer drawing](https://www.on-shore.com/wp-content/uploads/OSTTCXX2162.pdf) specifies 5.08mm pin pitch, 1.00mm pins and a 1.30mm PCB drill. The existing J3/J4 pads have 5.08mm spacing and 1.30mm drills. The replacement body is 7.5mm deep and 10mm high; its side interlocks extend beyond the nominal body width. The two positions on the saved board have room for that envelope. The old Phoenix 3D bodies and courtyards have not been regenerated.

Orient each wire entry toward the board edge. Check the actual delivered part against the drawing before soldering. J3 pad 1 is 12V input and J4 pad 1 is fused amplifier power; pad 2 on each is ground. Do not infer polarity from the terminal block's blue color.

## External power and speaker

The selected Tri-Mag L6R30-120 is a finished enclosed 12V supply. Its center-positive 5.5x2.1mm plug connects through **Adafruit 368**, DigiKey **1528-1386-ND**, to short wires leading to J3. Verify polarity with a meter before connection. Do not open the mains adapter or alter its mains wiring.

The **new Visaton FR 10 F - 4 OHM**, DigiKey **2056-FR10F-4OHM-ND**, connects only to the external amplifier's SPK+ and SPK- outputs. Neither speaker terminal connects to board ground. Start at minimum volume. Its 20W rating is not a promise that this 12V system produces 20W.

The 22 AWG ribbon pack can be separated for short regulator, power, speaker and signal leads. Keep I2S wiring short; the one-metre pack is not a recommendation for one-metre microphone leads. Mark polarity because all insulation is black. Secure loose leads and insulate exposed joints. The speaker enclosure and any protective grille are separate mechanical work.

The microphone remains Adafruit 3421, mapped by signal to J9 as documented in [Connections.md](Connections.md). Playback remains AUX-first; the external PCM5102 DAC remains deferred. No extra feature was removed in this cost revision.
