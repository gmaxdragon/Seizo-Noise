# Assembly and first power-up

The files describe an unassembled prototype. Passing ERC/DRC verifies the configured CAD rules, not soldering quality, audio performance, USB compliance or thermal behavior.

## Parts and orientation

Use the supplied BOM and footprints. U2 is the **Pololu D24V10F3**, not the earlier RECOM part. Its five connections are PG, SHDN, VIN, GND and VOUT. The first two are intentionally unconnected. Mount the module on the five-pin header with insulated support; do not let its underside touch traces.

F1 is soldered directly to the PCB. F2 is a Keystone 3568 holder with a separate 2A MINI fuse. D1's banded cathode faces the amplifier supply. C6 is polarized: its positive lead goes to AMP_12V. Check the real part's markings before soldering.

RV1 is Bourns PTV09A-2020F-A103, with a 20mm shaft. Its body, shaft and courtyard are inside the board outline in this design. USB and AUX openings intentionally face outside the edge. The ESP32 antenna overhang is intentional; do not place metal or an enclosure wall against it.

## First power-up

1. Inspect solder bridges, connector polarity, fuse values and module orientation with no power connected. Keep the external amplifier and robot actuators disconnected.
2. Check resistance between the supply rails and ground. Use a current-limited 5V bench source for the initial logic test, with USB VBUS disconnected from other sources. Verify BOARD_5V and +3V3 with a meter before attaching external modules.
3. Connect a data-capable USB cable after the supply checks. Verify native USB enumeration and firmware upload. The PCB supports USB data; USB audio playback/recording requires suitable firmware and is not enabled by wiring alone.
4. Add external modules one at a time. Measure current and the regulator/PTC temperature. Do not infer the Pi's total USB budget from the converter's 1A output rating. A 0.5A hold PTC is not a precise current limiter and its hold current depends on temperature.
5. Test the 12V amplifier supply separately, with correct polarity and the volume at minimum. Connect the speaker only to the amplifier's two speaker terminals. Raise volume gradually and check clipping, current and heating.

The 5V logic and 12V amplifier supplies share ground, but their positive rails must remain separate. Avoid using the robot motor supply as an unreviewed audio supply. Leave the optional UART cable disconnected unless both endpoints' power states and pin use are known.

The ECHO divider and exposed ports are not safety-rated robot sensors. Do not use this PCB as an emergency stop or sole collision-prevention device.
