# Purchasing and import corrections

## Active files

- `../BOM.csv` and `Selected_components.csv`: the same 32-line priced component list for the wired-regulator assembly option.
- `Seizo_Noise_DigiKey.csv`: 30 DigiKey product lines. The NEW 4-ohm speaker is the first row. There is no ESP32, Pololu 2830, Phoenix 1715721, or five-pin regulator socket in this cart file.
- `Other_suppliers.csv`: the exact ESP32 module from LCSC and the amplifier from ShillehTek.
- `BOM_engineering.csv` and `Selected_components_previous.csv`: earlier records, not current shopping lists.

## What changed

| Change | Previous USD | Revised USD |
| --- | ---: | ---: |
| Required ESP32-S3-WROOM-1-N8R8 | 6.32 at backordered DigiKey listing | 5.04 at LCSC, C2913201 |
| Regulator module | 12.95 Pololu 2830 | 3.95 Adafruit 4711, wired to existing U2 pads |
| Two power terminal blocks | 2.32 Phoenix | 1.16 On Shore OSTTC022162 |
| Regulator socket | 0.45 | Not used with wired regulator |
| Same Tri-Mag 12V supply | 10.53 | 10.33 refreshed listing |
| Wire pack and barrel adapter | Previously excluded | 6.25 now included |

The lower-cost regulator is NOT a drop-in replacement. Follow [the assembly option](../docs/Low_cost_assembly.md), including the three-wire mapping and insulation. No PCB copper, schematic nets, fuse values, USB protection, or speaker power rating was changed.

## Estimated price boundary

| Line | USD |
| --- | ---: |
| DigiKey component list, including new speaker, wire and barrel adapter | 55.11 |
| LCSC ESP32 module | 5.04 |
| ShillehTek amplifier | 6.99 |
| Selected-parts subtotal | 67.14 |
| Owner's separate PCB allowance | 4.00 |
| Selected parts plus that allowance | 71.14 |

The subtotal before the newly included wire and adapter is $60.89. The previous $72.98 estimate did not include those two items. The user's reported $83 cart has not been inspected, so no claim is made that the subtotal reconciles that live cart.

Regulator, terminal, speaker, supply, microphone, amplifier, wire and barrel-adapter listings were reviewed for this update. The LCSC result lists $5.0436 per module, rounded here to $5.04; its indexed stock display is not a reserved quantity. Other small-part prices are carried forward from the previous catalog checks. Actual checkout prices control.

Tax, tariff, delivery, an AUX cable, a USB data cable, the speaker enclosure, insulation and mounting hardware are not included or assumed free. The owner's approximately $20 tax/shipping allowance is not a quote and may not cover three suppliers plus PCB delivery. The $4 board allowance is owner-provided, not a fabrication checkout. This is not a complete delivered-cost guarantee or a $65 funding approval.

## ESP32 source

Buy **one bare ESP32-S3-WROOM-1-N8R8**, LCSC **C2913201**:
https://www.lcsc.com/product-detail/C2913201.html

Do not substitute a DevKit, ESP32-WROOM-32, N8-only module, or external-antenna 1U variant. Check actual stock, shipping and landed price before paying. The ESP32 remains required and included in the full BOM; it is removed only from the DigiKey order.

## DigiKey import

Use Upload a List with `Seizo_Noise_DigiKey.csv`. Map **DigiKey Part Number**, **Quantity**, and **Customer Reference** to their matching fields.

Use an empty project cart or replace the old affected lines first. Importing a new list does not prove that an existing cart's obsolete items were removed. In an existing cart, remove the old ESP32, Pololu regulator, Phoenix terminals and regulator socket before adding their replacements. Do not import the complete list on top of itself.

The first row must be:
`2056-FR10F-4OHM-ND,1,SPEAKER_4OHM_20W`

That is the actual Visaton loudspeaker. The separate `ST-HLHQRTMBQEIH` amplifier is not a speaker and is ordered from ShillehTek. If the speaker row fails to match, search DigiKey for the exact part number above and add quantity 1 manually. The earlier CSV already contained this SKU, so the reason for its absence from the user's cart has not been established.

## Half-Life import

Reopen Import from repo and check for 32 parts with readable prices and purposes. The expected component subtotal is $67.14, before any platform tax/shipping fields. Do not create duplicate entries. Root `BOM.csv` can be overwritten by platform sync; `Selected_components.csv` preserves the corrected data.

These files were validated for CSV syntax, row counts, unique DigiKey SKUs, speaker inclusion, ESP32 sourcing and arithmetic. Neither a live DigiKey cart nor the authenticated Half-Life importer was operated in this update.
