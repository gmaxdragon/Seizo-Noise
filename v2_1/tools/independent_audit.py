#!/usr/bin/python3.12
"""Independent schematic/net/geometry release audit; excludes physical compatibility claims."""
import json,xml.etree.ElementTree as ET
from pathlib import Path
import pcbnew as pcb
ROOT=Path(__file__).resolve().parent.parent
xml=ET.parse(ROOT/'validation/netlist.xml').getroot()
comps={c.get('ref') for c in xml.findall('./components/comp')}
assert len(comps)==14,comps
nodes={}
for net in xml.findall('./nets/net'):
    for node in net.findall('node'):
        key=node.get('ref'),node.get('pin')
        assert key not in nodes,key
        nodes[key]=net.get('name')
assert len(nodes)==29
b=pcb.LoadBoard(str(ROOT/'Seizo_Noise_v2.kicad_pcb'))
fp={f.GetReference():f for f in b.GetFootprints()}
assert len(fp)==18
found={}
for ref,foot in fp.items():
    for pad in foot.Pads():
        key=(ref,pad.GetNumber())
        if key in nodes:
            assert key not in found,key
            found[key]=pad.GetNetname()
        else:
            assert pad.GetNetname() in ('',None),(key,pad.GetNetname())
assert found==nodes,{'not_in_board':sorted(set(nodes)-set(found)),'not_in_netlist':sorted(set(found)-set(nodes)),'mismatched':[(k,v,found.get(k)) for k,v in nodes.items() if found.get(k)!=v]}
assert len(xml.findall('./nets/net'))==8
assert len({k[0] for k in nodes})==14
assert len({n for n in nodes.values()})==8
assert len([x for x in fp if x.startswith('H')])==4
mm=lambda a:round(pcb.ToMM(a),3)
def loc(obj):
    a=obj.GetPosition();return [mm(a.x),mm(a.y)]
print("DEBUG RV1",loc(fp['RV1'])); assert loc(fp['RV1'])==[78,26]
assert loc(fp['J4'])==[30,6]
mp=sorted([p for p in fp['RV1'].Pads() if p.GetNumber()=='MP'],key=lambda p:loc(p)[1]);assert len(mp)==2
coords=[loc(p) for p in mp]
assert abs(coords[1][1]-coords[0][1]-8.2)<0.001,coords
assert all(abs(mm(p.GetDrillSize().x)-3.3)<0.001 for p in mp)
assert abs(coords[0][0]-74.7)<0.001,coords
j4=[p for p in fp['J4'].Pads() if p.GetNumber()];assert len(j4)==3
assert all(sorted([mm(p.GetDrillSize().x),mm(p.GetDrillSize().y)])==[1.1,2.2] for p in j4)
assert {(p.GetNumber(),p.GetNetname()) for p in fp['J3'].Pads()}=={('1','/+5V_AUDIO'),('2','GND'),('3','/AMP_IN'),('4','GND')}
assert {(p.GetNumber(),p.GetNetname()) for p in fp['J4'].Pads()}=={('S','GND'),('T','Net-(J4-PadT)'),('R','Net-(J4-PadR)')}
assert {(p.GetNumber(),p.GetNetname()) for p in fp['D1'].Pads()}=={('1','/+5V_AUDIO'),('2','Net-(D1-A)')}
bbox=b.GetBoardEdgesBoundingBox()
assert abs(mm(bbox.GetWidth())-85)<0.1 and abs(mm(bbox.GetHeight())-60)<0.1
assert b.GetCopperLayerCount()==2
assert len(list(b.GetTracks()))>=100
assert any(z.GetNetname()=='GND' for z in b.Zones())
assert all(f.GetFPID().GetLibNickname()=='Seizo_Noise_v2' for f in fp.values())
assert '0  Errors 0  Warnings 0' in (ROOT/'validation/ERC_independent.rpt').read_text()
assert 'Found 0 DRC violations' in (ROOT/'validation/DRC_independent.rpt').read_text()
assert 'Found 0 unconnected pads' in (ROOT/'validation/DRC_independent.rpt').read_text()
PTH=(ROOT/'fabrication/DRAFT_ONLY/Seizo_Noise_v2-PTH.drl').read_text()
assert PTH.count('G85')==3
assert 'T7C3.300' in PTH or 'T7C3.300' in PTH.replace(' ','')
report={'schematic_component_refs':len(comps),'board_footprints':len(fp),'electrical_pad_to_net_assignments':len(found),'electrical_nets':8,'independent_pad_net_parity':'PASS','native_ERC_errors':0,'native_ERC_warnings':0,'native_DRC_violations':0,'native_DRC_unconnected':0,'native_DRC_schematic_parity_issues':0,'board_width_mm':85,'board_height_mm':60,'copper_layers':2,'track_segments':len(list(b.GetTracks())),'ground_zone':True,'volume_center_mm':loc(fp['RV1']),'volume_metal_tab_spacing_mm':8.2,'volume_tab_hole_diameter_mm':3.3,'jack_center_mm':loc(fp['J4']),'jack_plated_slot_mm':[1.1,2.2],'drill_slot_commands':PTH.count('G85'),'manufacturer_mechanical_fit_physically_tested':False,'supply_loaded_verified':False,'acoustic_tested':False,'Pi_USB_microphone_recorded':False,'fabrication_released':False}
(ROOT/'validation/INDEPENDENT_RELEASE_AUDIT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
