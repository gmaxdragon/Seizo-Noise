# Connections

Pin numbers below are **carrier-board connector numbers**. They are not the pin order of an arbitrary external module. Match the printed signal labels at both ends.

## Initial-build purchasing update

The lower-cost first build uses **AUX input for playback**, with SW3 set to AUX. The external PCM5102 DAC is deferred. The microphone selection is now **Adafruit 3421 (SPH0645LM4H)**, wired by signal to J9, not plugged directly into it. The saved carrier's INMP441 label identifies the original design, not the new breakout's pin order. All carrier-board electrical nets below are unchanged.

| Carrier J9 pin | Adafruit 3421 signal |
| --- | --- |
| 1 | 3V |
| 2 | GND |
| 3 | BCLK |
| 4 | LRCLK |
| 5 | DOUT |
| 6 | SEL, tied low for left-channel output |

Solder the breakout's header and configure firmware for this microphone's data format and I2S timing. The [manufacturer guide](https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/pinouts) specifies a 2-4 MHz bit clock. No microphone firmware or physical recording test has been completed by this purchasing update.

The selected adapter is **Tri-Mag L6R30-120, 12V 2.5A**, with a center-positive 5.5x2.1mm barrel plug. A correctly rated barrel-to-wire/terminal connection is required to reach J3. The adapter plugs into mains as a finished enclosed product; do not open it or modify mains wiring. See [budget and purchase scope](../purchasing/Budget.md).

## J1 - USB_C_Receptacle_USB2.0_16P

| Pin | Net |
|---|---|
| A1 | GND |
| A4 | USB_5V |
| A5 | Net-(J1-CC1) |
| A6 | Net-(J1-D+-PadA6) |
| A7 | USB_DM |
| A8 | Not connected |
| A9 | USB_5V |
| A12 | GND |
| B1 | GND |
| B4 | USB_5V |
| B5 | Net-(J1-CC2) |
| B6 | Net-(J1-D+-PadA6) |
| B7 | USB_DM |
| B8 | Not connected |
| B9 | USB_5V |
| B12 | GND |
| SH | GND |
| SH | GND |
| SH | GND |
| SH | GND |

## J3 - AMP_POWER_IN

| Pin | Net |
|---|---|
| 1 | AMP_12V_IN |
| 2 | GND |

## J4 - AMP_POWER_OUT

| Pin | Net |
|---|---|
| 1 | AMP_12V |
| 2 | GND |

## J5 - AMP_AUDIO_OUT

| Pin | Net |
|---|---|
| 1 | AMP_AUDIO |
| 2 | GND |

## J6 - PCM5102_DIGITAL (DAC deferred)

| Pin | Net |
|---|---|
| 1 | +3V3 |
| 2 | GND |
| 3 | I2S_BCLK |
| 4 | I2S_WS |
| 5 | I2S_DOUT |

## J7 - PCM5102_ANALOG (DAC deferred)

| Pin | Net |
|---|---|
| 1 | Net-(J7-Pin_1) |
| 2 | Net-(J7-Pin_2) |
| 3 | GND |

## J8 - SJ1-3533NG

| Pin | Net |
|---|---|
| R | PI_AUDIO_R |
| S | GND |
| T | PI_AUDIO_L |

## J9 - microphone interface

| Pin | Net |
|---|---|
| 1 | +3V3 |
| 2 | GND |
| 3 | I2S_BCLK |
| 4 | I2S_WS |
| 5 | I2S_MIC_DIN |
| 6 | GND |

## J10 - ULTRASONIC_SENSOR

| Pin | Net |
|---|---|
| 1 | BOARD_5V |
| 2 | US_TRIG |
| 3 | US_ECHO_5V |
| 4 | GND |

## J11 - PI_UART_BACKUP

| Pin | Net |
|---|---|
| 1 | GND |
| 2 | PI_UART_RX |
| 3 | PI_UART_TX |

## J12 - I2C_SENSOR_3V3

| Pin | Net |
|---|---|
| 1 | GND |
| 2 | +3V3 |
| 3 | I2C_SDA |
| 4 | I2C_SCL |

## U2 - Pololu D24V10F3 3.3V

| Pin | Net |
|---|---|
| 1 | Not connected |
| 2 | Not connected |
| 3 | BOARD_5V |
| 4 | GND |
| 5 | +3V3 |

## External audio path

Pi 4 or laptop headphone output -> stereo 3.5mm AUX cable -> J8 -> R11/R12 stereo-to-mono network -> SW3 source selector -> RV1 volume -> C8/R16/R17 -> J5 amplifier input.

Future DAC path: ESP32 I2S -> external PCM5102 DAC through J6 -> DAC analog L/R through J7 -> R9/R10 -> the other SW3 input. This requires the deferred DAC and appropriate firmware.

J4 supplies fused, reverse-polarity-protected 12V to the external amplifier. The speaker wires go **directly to the external amplifier SPK+ and SPK-**, never to GND or J5.

## External modules

- Deferred DAC: Adafruit PCM5102 I2S DAC breakout, product 6250. J6 power connects to its VIN, never its regulated 3V output. Connect BCK/WSEL/DIN by label.
- Microphone: Adafruit 3421 SPH0645LM4H breakout powered at 3.3V. Use the mapping above. The earlier INMP441 purchase is superseded; do not buy both microphones.
- Amplifier: ShillehTek TPA3118 PBTL mono module, HW-327 marking in the published photo. Use its labeled power and low-level input terminals. The raw speaker outputs are bridged and are not ground.
- Optional distance sensor: 5V HC-SR04-style sensor with a compatible trigger threshold. ECHO passes through the existing 10k/18k divider. Do not supply the sensor separately while the ESP32 is unpowered.
- J11 is optional 3.3V UART only. RX/TX are from the ESP32 perspective. Cross to the host TX/RX and connect ground; do not connect 5V logic.
- J12 is a 3.3V I2C expansion port. Do not connect 5V sensors or 5V pull-ups.

The amplifier, speaker, DAC, microphone, sensor, cables and enclosure are external system parts, not included in the carrier PCB geometry. The speaker/enclosure and final power adapter have not been physically validated.
