from pathlib import Path
import cadquery as cq, shutil
local=Path(__file__).resolve().parents[1]/'hardware/models/Seizo_Mechanical';local.mkdir(parents=True,exist_ok=True)
# Datasheet-derived envelopes, not manufacturer production models. CAD units are mm.
black=cq.Color(0.08,0.09,0.10);metal=cq.Color(.68,.69,.7);grey=cq.Color(.3,.3,.3)
def box(dx,dy,dz,x,y,z):return cq.Workplane('XY').box(dx,dy,dz,centered=(False,False,False)).translate((x,y,z))
# Bourns PTV09A-2020F-A103: 20 mm L measured from the mounting-tab plane.
pot=cq.Assembly(name='PTV09A_2020F_A103_envelope')
pot.add(box(5,9.7,12.0,-1.5,-2.35,3.5),name='body',color=grey)
pot.add(box(.8,6.8,9.2,3.5,-.9,5.4),name='front',color=black)
shaft=cq.Solid.makeCylinder(3,12.4,cq.Vector(4.3,2.5,10),cq.Vector(1,0,0))
# Flat over final 7 mm, at 1.5 mm above shaft axis.
shaft=shaft.cut(box(8,8,5,9.7,-1.5,11.5).val())
pot.add(shaft,name='shaft_L20',color=black)
for i,y in enumerate([0,2.5,5]):pot.add(box(.8,.3,6.9,-.4,y-.15,-3.4),name='lead'+str(i),color=metal)
for i,y in enumerate([-2.5,7.5]):pot.add(box(1.2,.8,7.2,-3.9,y-.4,-3.4),name='tab'+str(i),color=metal)
pot.save(str(local/'PTV09A_2020F_A103_envelope.step'))
# Same Sky SJ1-3533NG: body 8.2 x 14 x 12.5, 4 mm nose, 3.6 mm bore.
jack=cq.Assembly(name='SJ1_3533NG_envelope')
body=box(8.2,14,12.5,-4,-12.8,0).val()
bore=cq.Solid.makeCylinder(1.8,18.2,cq.Vector(.9,5.21,7),cq.Vector(0,-1,0))
body=body.cut(bore);jack.add(body,name='housing',color=black)
nose=cq.Solid.makeCylinder(3,4,cq.Vector(.9,1.2,7),cq.Vector(0,1,0)).cut(bore)
jack.add(nose,name='socket_nose',color=metal)
for n,x,y in [('sleeve',0,0),('tip',2,-2.4),('ring',2,-7.9)]:jack.add(box(.9,.3,3.4,x-.45,y-.15,-3.4),name=n,color=metal)
jack.save(str(local/'SJ1_3533NG_envelope.step'))
