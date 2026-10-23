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

Download the complete repository and open `hardware/speakerpcb.kicad_pro`. Keep the local symbol, footprint, and model folders with it. The native ERC and DRC reports were rerun during this publication, including copper refill and schematic-to-PCB comparison. These CAD checks do not replace assembly inspection or physical power/audio testing. Firmware has not been added just to satisfy the optional repository recommendation.

## Hardware reference

| Item | Saved design |
| --- | --- |
| Carrier PCB | 100 x 80 mm, two layers, 1.6 mm FR-4, nominal 1 oz copper |
| Controller | ESP32-S3-WROOM-1-N8R8 |
| 3.3 V supply | Pololu D24V10F3, product 2830, not the earlier RECOM regulator |
| Wired audio input | PCB-mounted 3.5 mm stereo AUX socket; source selector and volume control |
| Microphone | External INMP441 breakout wired to J9; the microphone IC is not soldered onto this carrier |
| DAC | External Adafruit PCM5102 breakout wired to J6/J7 |
| Amplifier and speaker | External amplifier connected to J4/J5; speaker connects directly to amplifier outputs |
| Other interfaces | Ultrasonic sensor connector, 3.3 V UART and 3.3 V I2C |
| Build status | CAD design files exist; no manufactured, assembled or powered board is documented here |

## Bill of materials

The board quantities and specifications below come from the saved Seizo Audio v1 design package. [BOM.csv](BOM.csv) includes references, sources, available prices and open purchasing details. Prices shown are USD catalog prices checked on October 21, 2026, not a delivered order quote. A dash means the price has not been verified; it does not mean the item is free.

### Components fitted to the carrier

| References | Qty | Component / part specification | Unit price | Line cost | Source |
| --- | ---: | --- | ---: | ---: | --- |
| U1 | 1 | ESP32-S3-WROOM-1-N8R8 | $6.32 | $6.32 | [DigiKey](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N8R8/15295891) |
| U2 | 1 | Pololu D24V10F3, product 2830 | $12.95 | $12.95 | [Pololu](https://www.pololu.com/product/2830) |
| U3 | 1 | ST USBLC6-2SC6, SOT-23-6 | — | — | [ST](https://www.st.com/en/protection-devices/usblc6-2.html) |
| J1 | 1 | GCT USB4085-GF-A USB-C receptacle | $0.91 | $0.91 | [DigiKey](https://www.digikey.com/en/products/detail/gct/USB4085-GF-A/9859733) |
| J8 | 1 | Same Sky SJ1-3533NG AUX input jack | $1.69 | $1.69 | [DigiKey](https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/SJ1-3533NG/738701) |
| J3, J4 | 2 | Phoenix Contact 1715721, 2-position, 5.08 mm terminal block | $1.16 | $2.32 | [DigiKey](https://www.digikey.com/en/products/detail/phoenix-contact/1715721/260631) |
| F1 | 1 | Littelfuse 1206L050/15YR, 0.5 A hold, 15 V PTC | $0.68 | $0.68 | [DigiKey](https://www.digikey.com/en/products/detail/littelfuse-inc/1206L050-15YR/2486168) |
| F2 holder | 1 | Keystone 3568 MINI blade fuse holder | $1.31 | $1.31 | [DigiKey](https://www.digikey.com/en/products/detail/keystone-electronics/3568/2137306) |
| D1 | 1 | 1N5822, DO-201AD, 3 A, 40 V | — | — | Manufacturer suffix and purchasing source remain to select |
| RV1 | 1 | Bourns PTV09A-2020F-A103, 10 kΩ audio taper, 20 mm shaft | $1.23 | $1.23 | [DigiKey](https://www.digikey.com/en/products/detail/bourns-inc/PTV09A-2020F-A103/3781098) |
| SW3 | 1 | C&K OS102011MS2QN1 nonshorting SPDT switch | — | — | [C&K drawing](https://www.ckswitches.com/media/1428/os.pdf) |
| SW1, SW2 | 2 | 6 x 6 mm normally-open THT buttons; 6.5 x 4.5 mm terminal pattern | — | — | Match pin pairing and the saved footprint |
| C1, C5 | 2 | 10 µF ceramic, 1206, X5R/X7R, at least 16 V | — | — | Exact purchasing part remains to select |
| C2, C7, C9, C10 | 4 | 100 nF ceramic, 1206, X7R, 50 V | — | — | Exact purchasing part remains to select |
| C3, C4 | 2 | 1 µF ceramic, 1206, X5R/X7R, at least 16 V | — | — | Exact purchasing part remains to select |
| C6 | 1 | Panasonic EEUFR1E471, 470 µF, 25 V, 10 mm diameter, 5 mm pitch | — | — | [Panasonic](https://industrial.panasonic.com/sa/products/pt/aluminum-cap-lead/models/EEUFR1E471) |
| C8 | 1 | 2.2 µF nonpolar ceramic, 1206, X7R, at least 25 V | — | — | Exact purchasing part remains to select |
| R1, R2, R13, R17 | 4 | 10 kΩ, 1206, 1%, at least 0.25 W | — | — | Exact purchasing part remains to select |
| R3, R4 | 2 | 5.1 kΩ, 1206, 1%, at least 0.25 W | — | — | Exact purchasing part remains to select |
| R5, R6 | 2 | 22 Ω, 1206, 1%, at least 0.25 W | — | — | Exact purchasing part remains to select |
| R9, R10, R11, R12, R18, R19 | 6 | 4.7 kΩ, 1206, 1%, at least 0.25 W | — | — | Exact purchasing part remains to select |
| R14 | 1 | 18 kΩ, 1206, 1%, at least 0.25 W | — | — | Exact purchasing part remains to select |
| R15 | 1 | 100 kΩ, 1206, 1%, at least 0.25 W | — | — | Exact purchasing part remains to select |
| R16 | 1 | 6.8 kΩ, 1206, 1%, at least 0.25 W | — | — | Exact purchasing part remains to select |
| J5 | 1 | 1 x 2 vertical male header, 2.54 mm | — | — | Carrier signal connector |
| J7, J11 | 2 | 1 x 3 vertical male header, 2.54 mm | — | — | Carrier signal connectors |
| J10, J12 | 2 | 1 x 4 vertical male header, 2.54 mm | — | — | Carrier signal connectors |
| J6 | 1 | 1 x 5 vertical male header, 2.54 mm | — | — | Carrier signal connector |
| J9 | 1 | 1 x 6 vertical male header, 2.54 mm | — | — | Carrier signal connector |

These rows account for all **48 fitted electrical components** in the saved carrier schematic. The ESP32 and Phoenix terminal blocks showed out of stock at the checked supplier; a listed price does not guarantee immediate availability.

### Assembly and external hardware

| Item | Qty | Selected part or required specification | Unit price | Line cost | Source / remaining check |
| --- | ---: | --- | ---: | ---: | --- |
| F2 removable fuse | 1 | Littelfuse 0297002.WXNV, 2 A, 32 V MINI | $0.39 | $0.39 | [DigiKey](https://www.digikey.com/en/products/detail/littelfuse-inc/0297002-WXNV/124900) |
| Regulator mating socket | 1 | 1 x 5 female, 2.54 mm; match module mounting | — | — | Select matching connector; module male header is included by Pololu |
| Mounting sets | 4 | M3 screws, insulating standoffs and matching hardware | — | — | Check existing stock and mechanical fit |
| Custom carrier PCB | 1 | 100 x 80 mm, 2 layers, 1.6 mm FR-4, 1 oz copper | — | — | Week 3 fabrication quote not verified; no Week 1 price carried over |
| DAC breakout | 1 | Adafruit PCM5102, product 6250 | $4.95 | $4.95 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/6250/26249971) |
| Microphone breakout | 1 | ShillehTek pre-soldered INMP441, ST-PKNE27OF3ENZ | $9.99 | $9.99 | [Supplier](https://shillehtek.com/products/inmp441-i2s-omnidirectional-microphone-module-with-soldering) |
| Amplifier module | 1 | ShillehTek TPA3118 PBTL mono, ST-HLHQRTMBQEIH | $6.99 | $6.99 | [Supplier](https://shillehtek.com/products/tpa3118-pbtl-single-digital-amplifier-board-1x60w); intended 12 V supply, not a claim of 60 W at 12 V |
| Loudspeaker | 1 | 4 Ω full-range driver, at least 20 W rating | — | — | Exact driver and enclosure match not selected |
| Amplifier power supply | 1 | Regulated 12 V DC supply with suitable current capacity and connector | — | — | Exact supply not selected |
| AUX cable | 1 | 3.5 mm stereo TRS male-to-male | — | — | Check owned cable first |
| USB cable | 1 | Host-compatible USB data cable to USB-C | — | — | Check owned cable first; not charge-only |
| Module and speaker wiring | 1 set | Signal leads plus appropriately rated power and speaker wires | — | — | Lengths and purchase quantity remain to select |
| Speaker enclosure | 1 | Match selected driver and acoustic design | — | — | Not included in PCB geometry |
| Optional distance sensor | 1 | Compatible HC-SR04-style 5 V module | — | — | Check owned sensor and trigger/ECHO compatibility before buying |

**Subtotal of the 12 priced rows only: $49.73. This is not the full project cost.** Unpriced rows, fabrication, delivery, tax and any duties are excluded. Shipping is not recorded as $0.00. No complete checkout total or funding approval is claimed.

## Sources and records

- [Original development journal](JOURNAL.md), synced by Half-Life. The entries and hours were not changed in this documentation update.
- [Bill of materials](BOM.csv), with source links and explicit pricing status.
- The schematic, PCB, libraries and design records are now available under `hardware/`, `docs/` and `validation/`. Import provenance is recorded in [import_provenance.json](docs/import_provenance.json). [purchasing/BOM_engineering.csv](purchasing/BOM_engineering.csv) preserves the engineering BOM independently of platform sync; unpriced items remain unresolved.
- The description at the top is the repository owner's existing text. This update used AI assistance to transfer and format the BOM, research catalog prices, and link the existing project images. It does not claim that this research or earlier AI-assisted CAD changes were completed unaided.
