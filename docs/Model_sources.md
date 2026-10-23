# CAD model sources

The board and component placement images are native KiCad renders of the supplied design, not photographs of an assembled board.

Most component models are from the official KiCad Packages3D library. Source URLs are in `kicad_model_sources.json`; its CC BY-SA license with design-use exception is included in `hardware/models/KICAD_LICENSE.md`. Existing authorship notices in STEP files are retained.

The Pololu regulator model comes from the manufacturer:
https://www.pololu.com/file/0J1375/pololu-1a-step-down-voltage-regulator-d24v10fx.step

J8 and RV1 use simplified, dimension-based mechanical envelopes, because their referenced standard-library model files were unavailable. These are explicitly visual/envelope models, not manufacturer production CAD or evidence of physical fit tests. Their editable CadQuery source is `cad/model_sources.py`. Dimensions were checked against:
- Same Sky SJ1-353XNG mechanical drawing, dated March 10, 2025: https://www.sameskydevices.com/product/resource/sj1-353xng.pdf
- Bourns PTV09 series drawing: https://www.bourns.com/docs/product-datasheets/ptv09.pdf

The selected potentiometer's shaft length is 20mm. The board placement and courtyard include that length, not only the smaller generic footprint sketch. External amplifier, speaker, DAC, microphone, cables and enclosure are not represented as assembled hardware in this STEP file.
