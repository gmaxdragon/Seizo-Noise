# Half-Life BOM price import recovery (2026-10-24)

The project owner verified that Half-Life rendered all 17 parts as **no price**, despite numeric values in the GitHub BOM. Thus the earlier claim that the importer was fixed was incorrect.

## CSV fix

The original file used header `Cost/item`. It was replaced with explicit numeric fields `Unit Price` and `Price`, while retaining a separate `Total Cost` value for quantity >1. These are distinct: R1/R2 quantity 2, unit $0.10, total $0.20. The columns are deliberately ordered **Total Cost before Price** because an older public Hack Club Stasis import UI looks for the first matching extended-cost header and recognises `Total Cost`; that importer is NOT verified to be the live Half-Life importer.

Header in updated root `BOM.csv`:

```csv
Item,Qty,Supplier,Total Cost,Unit Price,Price,link
J1: 2-pin 5.08mm screw terminal,1,DigiKey,0.58,0.58,0.58,https://www.digikey.com/en/products/detail/on-shore-technology-inc/OSTTC022162/614558
```

The 17 saved prices total **$34.46**, including a provisional $4 PCB estimate, before shipping, taxes and unquoted supplies. Prices are saved estimates, not a verified live supplier cart. The complete engineering BOM lists omitted expenses.

## Validation and limitations

- Arithmetic recomputed for all 17 line items: PASS.
- Explicit unit price field and numeric values: PASS.
- Matching purchasing backup: PASS.
- Live authenticated Half-Life import: **NOT VERIFIED**. Updating GitHub does not force the platform to reparse a previously imported snapshot. The account holder may need to choose Re-import from repo or upload the new CSV and check that at least J1 shows $0.58, R1/R2 shows $0.10 each, and subtotal is $34.46. If it still shows "no price" after re-import, the website importer may require manual column mapping or may not ingest price metadata from repositories. Do not claim otherwise.

Source: https://github.com/hackclub/blueprint/blob/main/docs/resources/bom.md (public Hack Club BOM format guidance, not Half-Life's private parser).
