# Seizo-Noise

## What I made

Seizo Noise is a PCB I designed for my robotic arm. The main reason I made it was that I wanted the arm to be able to talk and take in voice commands. I thought it would be really cool to say, “Hey, Seizo,” and have it respond with something like, “Yeah, what’s up?” I also want it to be able to play music.

It’s a big PCB with USB-C and connections for a separate microphone module and amplifier module. It also has more connectors for sensors and other parts of my robotic arm. The goal is to bring these connections together and make the whole setup simpler.

## What it does

The board is designed to receive audio from my Raspberry Pi or laptop through the headphone output, using an AUX cable plugged directly into the PCB. It has a switch to choose the audio source and a knob to adjust the volume.

It also connects to a microphone module, an amplifier module, and additional sensors. The amplifier connects to the speaker. Eventually, I want the microphone and software to let me talk to the robotic arm and have it respond. That voice interaction is still something I need to make work and test.

## Why I made it

I made it because constantly running motor commands and being on my phone to train the arm has gotten really annoying. I wanted to simplify that so I could eventually give it instructions by talking instead.

I also wanted one board to bring the audio and sensor connections together instead of having everything spread out. Making the robot easier to use is the main reason, but having it talk back would also be way cooler, in my opinion.

The AUX input also means it isn’t only for the arm. I want to connect my laptop and use the speaker setup for that too.

## My work and what I learned

I worked on the schematic, added components and connections, arranged the PCB, and routed it. I worked through a ton of errors, especially when ERC and DRC kept failing. That got really annoying at some points, but figuring out what the errors meant helped me learn.

Week 1 was mostly about messing around and learning how KiCad works. This project was more about understanding specific design rules, footprints, trace widths, and filling areas of the PCB with ground copper.

I learned that getting the schematic connected is only part of the work. I also had to think about where the components go, whether the footprints match, and whether the routing follows the rules. Working through those problems made me understand the whole process much better.

## Parts and current progress

I haven’t personally checked many of the individual parts yet. The connections I’m most familiar with are the headphone outputs on my laptop and Raspberry Pi. I chose an AUX input because those are simple to reuse, and it lets the board work with either device instead of being only for the robotic arm.

The schematic and routing work are finished in KiCad. I still need to finish checking the parts and purchasing choices, get the PCB made, solder it, and test the actual hardware. Nothing has been manufactured or assembled yet, so I haven’t tested the finished board playing audio or recording through the microphone.

## Help and sources

I used tutorials, datasheets, and KiCad’s tools throughout the project. I also talked to friends at school for help understanding things like different modules, voltage requirements, capacitor selection, and how to make the design safer.

ERC and DRC were especially helpful because they pointed out errors that I would have struggled to find myself. I used them a ton while working through the schematic and routing.

I also used AI to help plan the project, research components, explain errors, and give me instructions. ChatGPT directly edited project files too, including changes to the layout, routing, footprints, and labels when I got stuck. I did hands-on schematic and routing work myself, but the final files also include those AI-made changes.

## Project screenshots

![PCB layout screenshot supplied by the project owner](images/pcb-layout.png)

![3D PCB view supplied by the project owner](images/pcb-3d.png)

These are the owner's CAD screenshots, not photos of assembled hardware. The layout screenshot includes an earlier review-stage label; the editable design files below are Seizo Audio v1.0.

## Design files

| File | Link |
| --- | --- |
| KiCad schematic | [speakerpcb.kicad_sch](hardware/speakerpcb.kicad_sch) |
| PCB layout | [speakerpcb.kicad_pcb](hardware/speakerpcb.kicad_pcb) |
| Complete KiCad project | [speakerpcb.kicad_pro](hardware/speakerpcb.kicad_pro) |
| Board rules | [speakerpcb.kicad_dru](hardware/speakerpcb.kicad_dru) |
| Included footprints | [Seizo_Audio.pretty](hardware/Seizo_Audio.pretty) |
| Included symbols | [Seizo_Audio.kicad_sym](hardware/Seizo_Audio.kicad_sym) |
| Assembly instructions | [Assembly.md](docs/Assembly.md) |
| Connector pin maps | [Connections.md](docs/Connections.md) |
| Native schematic check | [ERC.rpt](validation/ERC.rpt) |
| Native board and schematic-parity check | [DRC.rpt](validation/DRC.rpt) |
| Gerbers and drills | [Seizo_Audio_Gerbers.zip](fabrication/Seizo_Audio_Gerbers.zip) |

Download the complete repository and open `hardware/speakerpcb.kicad_pro`. Keep the local symbol, footprint, and model folders with it. The native ERC and DRC reports were rerun during the CAD publication, including copper refill and schematic-to-PCB comparison. These CAD checks do not replace assembly inspection or physical power/audio testing. The purchasing revision below did not change the PCB or schematic.

## Hardware reference

| Item | Saved design and initial purchase plan |
| --- | --- |
| Carrier PCB | 100 x 80 mm, two layers, 1.6 mm FR-4, nominal 1 oz copper |
| Controller | ESP32-S3-WROOM-1-N8R8 |
| 3.3 V supply | Pololu D24V10F3, product 2830 |
| Playback for first build | Pi/laptop analog AUX output through the source selector and volume control |
| Microphone | External Adafruit 3421 SPH0645LM4H, wired to J9 by signal labels; replaces the earlier INMP441 selection |
| DAC | Adafruit PCM5102 6250 is deferred; J6/J7 remain for later addition |
| Amplifier and speaker | External TPA3118 module at J4/J5; Visaton FR 10 F 4-ohm speaker at amplifier outputs |
| Amplifier supply | Tri-Mag L6R30-120 enclosed 12V 2.5A adapter; barrel connection to J3 still required |
| Other interfaces | Ultrasonic connector, 3.3V UART and 3.3V I2C; extra sensors are not in the first purchase |
| Build status | CAD files exist; no manufactured, assembled or powered board is documented here |

## Bill of materials

**Initial-build component subtotal: $72.98.** The list contains 31 priced purchasing lines, with 30 available through DigiKey listings and the amplifier through ShillehTek. The external DAC is deferred so playback initially uses the Pi/laptop AUX output. No carrier protection parts were cut.

The table is a component purchasing plan, not a complete delivered-project total. The owner's $4 PCB allowance brings parts plus that allowance to $76.98, leaving $3.02 before the $80 target. Required cabling, the barrel adapter, enclosure/mounting costs, shipping and tax are not included or assumed free. See [budget scope](purchasing/Budget.md).

Microphone and adapter listing prices were rechecked on October 22, 2026. Other prices are retained from the previous catalog check. Actual cart prices and availability control; the ESP32 and Phoenix terminals previously showed backorder, and the Pololu module can ship separately.

| References | Qty | Part / function | Unit USD | Line USD | Vendor |
| --- | ---: | --- | ---: | ---: | --- |
| U1 | 1 | ESP32-S3-WROOM-1-N8R8 | 6.32 | 6.32 | [DigiKey](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N8R8/15295891) |
| U2 | 1 | Pololu D24V10F3, product 2830 | 12.95 | 12.95 | [DigiKey Marketplace](https://www.digikey.com/en/products/detail/pololu/2830/10451161) |
| U3 | 1 | USBLC6-2SC6 ESD protection | 0.54 | 0.54 | [DigiKey](https://www.digikey.com/en/products/detail/stmicroelectronics/USBLC6-2SC6/1040559) |
| J1 | 1 | GCT USB4085-GF-A USB-C | 0.91 | 0.91 | [DigiKey](https://www.digikey.com/en/products/detail/gct/USB4085-GF-A/9859733) |
| J8 | 1 | SJ1-3533NG AUX input | 1.69 | 1.69 | [DigiKey](https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/SJ1-3533NG/738701) |
| J3, J4 | 2 | Phoenix 1715721 power terminals | 1.16 | 2.32 | [DigiKey](https://www.digikey.com/en/products/detail/phoenix-contact/1715721/260631) |
| F1 | 1 | 1206L050/15YR USB resettable fuse | 0.68 | 0.68 | [DigiKey](https://www.digikey.com/en/products/detail/littelfuse-inc/1206L050-15YR/2486168) |
| F2 | 1 | Keystone 3568 MINI fuse holder | 1.31 | 1.31 | [DigiKey](https://www.digikey.com/en/products/detail/keystone-electronics/3568/2137306) |
| F2 insert | 1 | 0297002.WXNV 2A MINI fuse | 0.39 | 0.39 | [DigiKey](https://www.digikey.com/en/products/detail/littelfuse-inc/0297002-WXNV/124900) |
| D1 | 1 | Taiwan Semiconductor 1N5822 diode | 0.71 | 0.71 | [DigiKey](https://www.digikey.com/en/products/detail/taiwan-semiconductor-corporation/1N5822/7366597) |
| RV1 | 1 | PTV09A-2020F-A103 10k volume control | 1.23 | 1.23 | [DigiKey](https://www.digikey.com/en/products/detail/bourns-inc/PTV09A-2020F-A103/3781098) |
| SW3 | 1 | OS102011MS2QN1 audio selector | 0.80 | 0.80 | [DigiKey](https://www.digikey.com/en/products/detail/c-k/OS102011MS2QN1/411602) |
| SW1, SW2 | 2 | B3F-1000 RESET/BOOT buttons | 0.35 | 0.70 | [DigiKey](https://www.digikey.com/en/products/detail/aratas-america-llc/B3F-1000/33150) |
| C1, C5 | 2 | CL31A106KAHNFNE 10uF 1206 | 0.25 | 0.50 | [DigiKey](https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL31A106KAHNFNE/3888696) |
| C2, C7, C9, C10 | 4 | CL31B104KBCNNNC 100nF 1206 | 0.14 | 0.56 | [DigiKey](https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL31B104KBCNNNC/3886675) |
| C3, C4 | 2 | CL31B105KBHSNNE 1uF 1206 | 0.24 | 0.48 | [DigiKey](https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL31B105KBHSNNE/3891179) |
| C6 | 1 | EEU-FR1E471 470uF 25V | 1.06 | 1.06 | [DigiKey](https://www.digikey.com/en/products/detail/panasonic-industry/EEU-FR1E471/2433553) |
| C8 | 1 | CL31B225KAHNNNE 2.2uF 1206 | 0.21 | 0.21 | [DigiKey](https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL31B225KAHNNNE/3886730) |
| R1, R2, R13, R17 | 4 | RC1206FR-0710KL 10k | 0.11 | 0.44 | [DigiKey](https://www.digikey.com/en/products/detail/yageo/RC1206FR-0710KL/731430) |
| R3, R4 | 2 | RC1206FR-075K1L 5.1k | 0.10 | 0.20 | [DigiKey](https://www.digikey.com/en/products/detail/yageo/RC1206FR-075K1L/728947) |
| R5, R6 | 2 | RC1206FR-0722RL 22 ohm | 0.11 | 0.22 | [DigiKey](https://www.digikey.com/en/products/detail/yageo/RC1206FR-0722RL/728687) |
| R9, R10, R11, R12, R18, R19 | 6 | RC1206FR-074K7L 4.7k | 0.10 | 0.60 | [DigiKey](https://www.digikey.com/en/products/detail/yageo/RC1206FR-074K7L/728887) |
| R14 | 1 | RC1206FR-0718KL 18k | 0.10 | 0.10 | [DigiKey](https://www.digikey.com/en/products/detail/yageo/RC1206FR-0718KL/731539) |
| R15 | 1 | RC1206FR-07100KL 100k | 0.10 | 0.10 | [DigiKey](https://www.digikey.com/en/products/detail/yageo/RC1206FR-07100KL/728492) |
| R16 | 1 | RC1206FR-076K8L 6.8k | 0.10 | 0.10 | [DigiKey](https://www.digikey.com/en/products/detail/yageo/RC1206FR-076K8L/729028) |
| J5, J6, J7, J9, J10, J11, J12 | 1 strip | PRPC040SAAN-RC, cut into seven headers | 1.23 | 1.23 | [DigiKey](https://www.digikey.com/en/products/detail/sullins-connector-solutions/PRPC040SAAN-RC/2775214) |
| U2 socket | 1 | PPPC051LFBN-RC five-pin socket | 0.45 | 0.45 | [DigiKey](https://www.digikey.com/en/products/detail/sullins-connector-solutions/PPPC051LFBN-RC/810177) |
| External J9 | 1 | Adafruit 3421 I2S microphone breakout | 6.95 | 6.95 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/3421/6691114) |
| External J4/J5 | 1 | ShillehTek TPA3118 mono amplifier | 6.99 | 6.99 | [ShillehTek](https://shillehtek.com/products/tpa3118-pbtl-single-digital-amplifier-board-1x60w) |
| External speaker | 1 | Visaton FR 10 F, 4 ohm | 11.71 | 11.71 | [DigiKey](https://www.digikey.com/en/products/detail/visaton-gmbh-co-kg/FR-10-F-4-OHM/10650582) |
| External supply | 1 | Tri-Mag L6R30-120, 12V 2.5A | 10.53 | 10.53 | [DigiKey](https://www.digikey.com/en/products/detail/tri-mag-llc/L6R30-120/7682642) |
| **Selected component subtotal** | | | | **72.98** | |

[Half-Life import CSV](BOM.csv) uses explicit Quantity, Unit Price, Vendor, URL and Purpose columns. [DigiKey upload CSV](purchasing/Seizo_Noise_DigiKey.csv) contains 30 DigiKey lines; the amplifier is a separate purchase. These files have been checked for row counts and arithmetic, not imported into a live checkout by this update. Check the Half-Life import preview before saving; do not duplicate an existing import.

## Sources and records

- [Original development journal](JOURNAL.md), synced by Half-Life. Entries and hours were not changed.
- [Current component selection](purchasing/Selected_components.csv) and [budget scope](purchasing/Budget.md).
- [Earlier engineering requirements](purchasing/BOM_engineering.csv), retained as a wider requirements record, not the active purchase list.
- [Previous priced selection](purchasing/Selected_components_previous.csv), retained for comparison, not purchase.
- [CAD import provenance](docs/import_provenance.json) and native checks under `validation/`.
- AI assistance was used to format the parts lists, research replacement options and update technical wiring notes. The six owner-approved narrative sections above remain unchanged. This does not claim unaided research or completed physical tests.
