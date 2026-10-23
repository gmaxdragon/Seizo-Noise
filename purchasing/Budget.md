# Initial build budget

The revised purchase list totals **$72.98 for 31 component rows**, compared with $85.64 previously. This is a component subtotal, not a complete delivered build price.

| Change | Previous | Selected | Saving |
| --- | ---: | ---: | ---: |
| Microphone: ShillehTek INMP441 to Adafruit 3421 I2S breakout | $9.99 | $6.95 | $3.04 |
| Adapter: Mean Well GST36U12-P1J to Tri-Mag L6R30-120 | $15.20 | $10.53 | $4.67 |
| External Adafruit PCM5102 DAC 6250 | $4.95 | Deferred | $4.95 |
| Total saving | | | $12.66 |

The first build uses the Pi or laptop's analog AUX output. Set SW3 to AUX. The amplifier, speaker and microphone remain in the purchase list. Standalone ESP32 digital audio playback through the DAC is deferred, not claimed to work without a DAC. No PCB traces, component values, fuses or protection devices were removed.

## Budget boundary

| Budget line | USD |
| --- | ---: |
| Selected components | 72.98 |
| Board allowance supplied by owner | 4.00 |
| Parts plus board allowance | 76.98 |
| Remaining before the owner's $80 pre-delivery target | 3.02 |

The $4 board figure is the owner's allowance, not a new fabrication checkout quote. Required AUX/USB cables, the barrel-to-terminal connection, signal and speaker wiring, and the enclosure/mounting arrangement are not priced in that subtotal or confirmed already owned. They must be covered before calling the whole build under $80. No missing cost has been assigned zero. Optional extra sensors and the deferred DAC are not part of the first purchase.

The owner set aside about $20 for shipping and tax. This is a spending allowance, not a carrier or tax quote. Pololu is a DigiKey Marketplace seller and may ship separately. The ESP32 and Phoenix terminals were listed on backorder in the prior check. A lower parts subtotal does not promise a delivery date or a fully funded $65 tier submission.

## Files and imports

- `../BOM.csv`: 31 priced initial-build rows with Quantity, Unit Price, Vendor, URL and Purpose columns. No shipping or order-total row is imported as a part.
- `Selected_components.csv`: identical durable copy of the initial-build list.
- `Seizo_Noise_DigiKey.csv`: 30 DigiKey lines, excluding the ShillehTek amplifier. Map DigiKey Part Number, Quantity and Customer Reference in Upload a List. Check exact matches, quantities, stock, shipping and taxes before ordering.
- `Selected_components_previous.csv`: the previous $85.64 selection, retained for comparison rather than purchase.
- `BOM_engineering.csv`: original wider engineering requirements. It is not a current priced checkout list.

The CSV values and arithmetic were checked locally. Half-Life's live importer and a real DigiKey cart have not been run by this update. In Half-Life, reopen Import from repo and verify the 31 rows total $72.98 before saving. Do not add this list on top of already imported duplicate rows. Root BOM.csv can be overwritten by platform sync; use the durable copy for recovery.

## Replacement microphone wiring

The Adafruit 3421 module is a wired external replacement, not a direct plug-in match to J9. Solder the breakout's header as instructed by its manufacturer. Connect carrier J9 pin 1 to 3V, pin 2 to GND, pin 3 to BCLK, pin 4 to LRCLK, pin 5 to DOUT, and pin 6 to SEL (left channel). Configure firmware for SPH0645LM4H I2S timing and data format; the manufacturer's guide specifies a 2-4 MHz bit clock. This connection and firmware still need physical verification. The saved carrier's INMP441 label is historical; do not use it to infer breakout pin order.

## Sources for the changes

- [Adafruit 3421 DigiKey listing](https://www.digikey.com/en/products/detail/adafruit-industries-llc/3421/6691114): $6.95, part 1528-1908-ND, listing checked October 22, 2026.
- [Adafruit microphone pinouts](https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/pinouts): supply, I2S signals and channel selection.
- [Tri-Mag L6R30-120 DigiKey listing](https://www.digikey.com/en/products/detail/tri-mag-llc/L6R30-120/7682642): $10.53, part 364-1279-ND, 12V 2.5A, positive-center 5.5x2.1mm output, listing checked October 22, 2026.
- [Tri-Mag manufacturer data](https://www.tri-mag.com/wp-content/uploads/2021/05/L6R24-L6R30_Series_2021-02.pdf).

Other prices are carried forward from the previous selection rather than represented as newly checked live prices. No purchase or funding submission was made.
