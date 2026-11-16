#!/usr/bin/env python3
"""Build the editable CSI 5137 deck, embedded notes, script, and timing audit.
Requires python-pptx and Pillow. Font files are deliberately not bundled.
"""
from pathlib import Path
import re, csv, json, math, argparse
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.xmlchemy import OxmlElement
from content import SLIDES, SOURCES
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT
C={'g':'8F001A','ink':'2D2D2C','gray':'80746C','blue':'636D77','sage':'67796C','light':'F2F2F2','white':'FFFFFF','rule':'D8D6D3','pale':'F7EEF0'}
FONT='Work Sans'; SERIF='Spectral'
W,H=13.333333,7.5
P=Presentation();P.slide_width=Inches(W);P.slide_height=Inches(H)
P.core_properties.title='Testing databases without an answer key'
P.core_properties.subject='CSI 5137 — Advanced Topics in Databases and Data Management'
P.core_properties.author='CSI 5137 course project'
P.core_properties.keywords='CODDTest, DDLCheck, WriteCheck, Radar, uOttawa, CSI 5137'
P.core_properties.comments='Student course presentation; university branding is not an endorsement. Reproduction evidence is separated from paper evaluation.'
LAYOUTS=[]
def rgb(c):return RGBColor.from_string(C.get(c,c))
def rect(s,x,y,w,h,fill='light',stroke=None,radius=False):
 sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
 sh.fill.solid();sh.fill.fore_color.rgb=rgb(fill)
 sh._element.spPr.append(OxmlElement('a:effectLst'))
 if stroke:sh.line.color.rgb=rgb(stroke);sh.line.width=Pt(1)
 else:sh.line.fill.background()
 if radius:
  try:sh.adjustments[0]=.08
  except:pass
 return sh

def text(s,t,x,y,w,h,size=24,color='ink',bold=False,font=FONT,align=None,margin=0,val=MSO_ANCHOR.TOP):
 sh=s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
 tf=sh.text_frame;tf.clear();tf.word_wrap=True
 tf.margin_left=tf.margin_right=Inches(margin);tf.margin_top=tf.margin_bottom=0;tf.vertical_anchor=val
 for i,line in enumerate(str(t).split('\n')):
  p=tf.paragraphs[0] if i==0 else tf.add_paragraph();p.text=line
  p.font.name=font;p.font.size=Pt(size);p.font.bold=bold;p.font.color.rgb=rgb(color)
  p.space_after=Pt(0);p.space_before=Pt(0);p.line_spacing=1.06
  if align is not None:p.alignment=align
 return sh

def line(s,x1,y1,x2,y2,color='rule',width=1.4,dash=False):
 sh=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2));sh.line.color.rgb=rgb(color);sh.line.width=Pt(width)
 sh._element.spPr.append(OxmlElement('a:effectLst'))
 if dash:
  from pptx.enum.dml import MSO_LINE_DASH_STYLE
  sh.line.dash_style=MSO_LINE_DASH_STYLE.DASH
 return sh

def arrow(s,x1,y1,x2,y2,color='gray',width=2):
 sh=line(s,x1,y1,x2,y2,color,width)
 head=OxmlElement('a:tailEnd');head.set('type','triangle');head.set('w','med');head.set('len','med');sh.line._get_or_add_ln().append(head)
 return sh

def circle(s,label,x,y,d=.48,fill='g',color='white',size=17):
 sh=s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(d), Inches(d));sh.fill.solid();sh.fill.fore_color.rgb=rgb(fill);sh.line.fill.background()
 text(s,label,x,y+.035,d,d-.06,size,color,True,align=PP_ALIGN.CENTER)
 return sh

def label(s,t,x,y,w=5,color='gray',size=13):return text(s,t.upper(),x,y,w,.32,size,color,True)
def foot(s,n,section,source='',dark=False):
 col='white' if dark else 'gray'
 line(s,.68,6.93,12.65,6.93,'9C1C30' if dark else 'rule',.8)
 text(s,'CSI 5137  /  ATDM',.7,7.08,2.45,.2,10,col)
 text(s,section.upper(),3.1,7.08,2.65,.2,10,col)
 text(s,source,5.9,7.04,6.13,.35,9.5,col,align=PP_ALIGN.RIGHT)
 text(s,f'{n:02}',12.2,7.07,.45,.22,11,col,True,align=PP_ALIGN.RIGHT)

def base(n,title,section,source='',dark=False,kicker=None):
 s=P.slides.add_slide(P.slide_layouts[6]);s.background.fill.solid();s.background.fill.fore_color.rgb=rgb('g' if dark else 'white')
 if not dark:
  label(s,kicker or section,.72,.43,10,'g',12)
  text(s,title,.7,.97,11.98,.75,33,'ink',True)
 foot(s,n,section,source,dark)
 # Manual advance only; no autoplay. Progressive method steps are separate slides.
 tr=OxmlElement('p:transition');tr.set('spd','fast');tr.set('advClick','1');tr.append(OxmlElement('p:fade'));s._element.append(tr)
 return s

def band(s,t,y=6.12,color='g'):
 rect(s,.7,y,11.95,.58,'pale' if color=='g' else 'light')
 text(s,t,.92,y+.12,11.5,.35,18,color,True)

def node(s,t,x,y,w=2.2,h=.75,active=False):
 rect(s,x,y,w,h,'g' if active else 'light')
 text(s,t,x+.14,y+.15,w-.28,h-.25,23,'white' if active else 'ink',True,align=PP_ALIGN.CENTER)

def result(s,title,values,x,y,w=4.5,accent=False):
 label(s,title,x,y,w,'g' if accent else 'gray',13)
 rect(s,x,y+.47,w,2.15,'pale' if accent else 'light')
 text(s,values,x+.25,y+.8,w-.5,1.6,43,'g' if accent else 'ink',font=FONT,align=PP_ALIGN.CENTER)

def tbl(s,headers,rows,x,y,w=3,rowh=.58,highlight=None,muted=False,size=24):
 cw=w/len(headers)
 rect(s,x,y,w,rowh,'ink')
 for j,h in enumerate(headers):text(s,h,x+j*cw,y+.1,cw,rowh-.12,size,'white',True,align=PP_ALIGN.CENTER)
 for i,row in enumerate(rows):
  for j,v in enumerate(row):
   hot=(highlight and (i,j) in highlight);fill='pale' if hot else ('light' if i%2==0 else 'white')
   rect(s,x+j*cw,y+(i+1)*rowh,cw,rowh,fill)
   text(s,str(v),x+j*cw,y+(i+1)*rowh+.1,cw,rowh-.12,size,'g' if hot else ('gray' if muted else 'ink'),hot,align=PP_ALIGN.CENTER)
  line(s,x,y+(i+2)*rowh,x+w,y+(i+2)*rowh,'rule',.6)
 return y+(len(rows)+1)*rowh

def section(n,num,name,question,full,byline):
 s=base(n,'',name,dark=True)
 text(s,num,.78,.85,2,1.6,89,'white',font=FONT)
 label(s,name,3.0,1.17,7,'white',17)
 text(s,question,3.0,1.92,9.4,2.15,47,'white',font=SERIF)
 text(s,full,3.02,4.66,8.9,1.13,21,'white')
 text(s,byline,3.02,6.13,8.9,.35,16,'white')
 return s

def step_strip(s,active):
 for k,t in enumerate(['READ QUERY','EVALUATE','SUBSTITUTE']):
  x=.76+k*4.08
  rect(s,x,1.99,3.66,.45,'g' if active==k else 'light')
  text(s,f'0{k+1}  {t}',x+.18,2.09,3.3,.22,13,'white' if active==k else 'gray',True)

def toy(s,active):
 step_strip(s,active)
 label(s,'t',.83,2.91,2);tbl(s,['x'],[[10],[30],[60]],.83,3.35,1.4,.56,size=25)
 label(s,'s',2.54,2.91,2);tbl(s,['y'],[[10],[30]],2.54,3.35,1.4,.56,size=25)
 if active==0:
  label(s,'ORIGINAL QUERY',5.0,2.93,6)
  text(s,'SELECT x FROM t\nWHERE x >',5.0,3.42,7.0,1.0,29)
  rect(s,5.0,4.53,7.1,.65,'pale');text(s,'(SELECT AVG(y) FROM s)',5.16,4.64,6.8,.43,27,'g',True)
  band(s,'A teaching example—not a reported bug.')
 elif active==1:
  label(s,'AUXILIARY QUERY',5.0,2.93,6)
  text(s,'SELECT AVG(y) FROM s',5,3.43,7,.54,29,'g',True)
  arrow(s,6.28,4.26,7.16,4.26,'g');text(s,'20',7.4,3.93,2.7,1.0,70,'g',font=SERIF)
  band(s,'One row-independent subquery → one substitution value.')
 else:
  label(s,'CONSTANT FORM',4.55,2.91,6)
  text(s,'SELECT x FROM t\nWHERE x > 20',4.55,3.36,7.7,1.12,32,'g',True)
  label(s,'ORIGINAL',4.56,5.00,2);text(s,'30, 60',4.56,5.4,2.9,.65,34,font=SERIF)
  text(s,'=',8.0,5.32,.8,.7,38,'g')
  label(s,'CONSTANT FORM',9.17,5.00,3);text(s,'30, 60',9.17,5.4,2.9,.65,34,font=SERIF)

def fk(s,after):
 label(s,'CHILD',1.2,2.04,3);label(s,'PARENT',8.55,2.04,3)
 node(s,'t1',1.2,2.61,3.1,.87)
 node(s,'t2' if after else 't0',8.6,2.61,3.1,.87,after)
 text(s,'c1  /  foreign key',1.2,3.66,3.8,.5,22)
 text(s,'c2  /  primary key',8.6,3.66,3.8,.5,22)
 arrow(s,4.47,3.02,8.26,3.02,'g');label(s,'REFERENCES',5.15,2.48,2.6,'g')
 if after:
  text(s,'parent contains 1',8.6,4.48,3.8,.5,23,'g',True)
  label(s,'SHOW CREATE TABLE t1',1.2,4.68,5)
  rect(s,1.2,5.18,10.5,.78,'pale');text(s,'FOREIGN KEY (c1) REFERENCES t2(c2)',1.4,5.38,10,.45,27,'g',True)
 else:
  label(s,'SCHEMA CHANGE',1.2,4.8,4)
  rect(s,1.2,5.28,10.5,.72,'pale');text(s,'ALTER TABLE t0 RENAME AS t2, ALGORITHM COPY;',1.4,5.47,10,.45,24,'g',True)

def timeline(s,stage):
 x1,x2=1.03,5.0
 label(s,'T1',x1,1.99,2,'g',19);label(s,'T2',x2,1.99,2,'g',19)
 line(s,x1+.12,2.55,x1+.12,6.44,'rule',2);line(s,x2+.12,2.55,x2+.12,6.44,'rule',2)
 events=[(x1,2.63,'BEGIN'),(x1,3.27,'UPDATE a = 10'),(x2,3.81,'BEGIN'),(x2,4.43,'UPDATE b = 20')]
 if stage==2:events += [(x1,5.35,'COMMIT'),(x2,5.96,'resume + COMMIT')]
 for x,y,t in events:
  circle(s,'',x-.02,y+.1,.3,'g');text(s,t,x+.4,y,3.38,.52,21,'ink',True)
 text(s,'WHERE a',x2+.4,4.88,3.2,.4,19,'gray')
 if stage==1:
  rect(s,5.4,5.54,2.9,.6,'pale');text(s,'WAIT',5.58,5.66,2.55,.4,23,'g',True)
  text(s,'uncommitted',1.43,4.48,3.3,.48,19,'gray')
  text(s,'Result\npending',9.77,3.38,2.82,1.24,29,'gray',font=SERIF)
 else:
  arrow(s,3.36,5.69,4.79,5.69,'g',2)
  label(s,'OBSERVED',9.45,2.58,3,'g',13)
  tbl(s,['a','b'],[[10,1],[10,20],[10,20]],9.43,3.06,2.9,.59,[(0,1)],size=24)

def stats(s,nums,labels,xs=None):
 xs=xs or [.86,5.02,9.18]
 for x,n,l in zip(xs,nums,labels):
  text(s,n,x,2.25,3.45,1.5,79,'g',font=FONT)
  text(s,l,x,3.94,3.4,1.01,24,'ink',True)

# --- Main slides -----------------------------------------------------------
for i,d in enumerate(SLIDES,1):
 title=d['title'];sec=d['section']
 src={'OPENING':'Research synthesis · [C, D, W, A]','CODDTEST':'[C] §3–4 · PACMMOD 2025','DDLCHECK':'[D] §3–6 · PVLDB 2025','WRITECHECK':'[W] §2–6 · PVLDB 2025','RADAR':'[A] §3–4 · PVLDB 2024','SYNTHESIS':'Research synthesis · [C, D, W, A]'}.get(sec,'')
 if i in [10,11]:src='[R] MySQL #111241 · project replay'
 if i in [17,18,19]:src='[D] Listing 4 · [R] MySQL #114904'
 if i in [24,25,26,27]:src='[R, T] MySQL #104833 · Troc replay'
 if i==31:src='[R] MySQL #110125 · project replay'
 if i==33:src='[R, T] Project evidence · not full evaluations'
 if i==1:
  s=base(i,'','OPENING','CSI 5137 · Student course project',kicker=' ')
  rect(s,0,0,.22,7.5,'g');s.shapes.add_picture(str(ROOT/'assets/uottawa_logo.png'),Inches(10.1),Inches(.65),width=Inches(2.35))
  label(s,'CSI 5137  /  ATDM',.8,.76,8,'g',16)
  text(s,'Testing databases\nwithout an\nanswer key.',.8,1.9,10.9,3.25,57,'ink',font=SERIF)
  rect(s,.82,5.62,.72,.09,'g')
  text(s,'CODDTest  /  DDLCheck  /  WriteCheck  /  Radar',.82,5.98,11.4,.42,23,'g',True)
  text(s,'Advanced Topics in Databases and Data Management',.82,6.49,11.5,.3,16,'gray')
 elif i==2:
  s=base(i,title,sec,src)
  text(s,'42',.8,2.05,6.4,3.5,178,'g',font=SERIF)
  text(s,'Did it finish?\nOr is it correct?',7.25,2.84,4.9,1.8,38,font=SERIF)
  label(s,'THE TEST-ORACLE PROBLEM',7.28,5.11,5,'g',14)
 elif i==3:
  s=base(i,title,sec,src)
  label(s,'ORIGINAL',.87,2.23,3);label(s,'TRANSFORMED',.87,4.23,3)
  for y,q,r in [(2.84,'execution A','result A'),(4.84,'execution B','result B')]:
   node(s,q,.88,y,2.9);arrow(s,3.93,y+.36,4.68,y+.36);node(s,'DBMS',4.87,y,2.03,active=True);arrow(s,7.08,y+.36,7.8,y+.36);node(s,r,8.03,y,2.33)
  line(s,10.67,3.2,11.24,3.2,'g');line(s,11.24,3.2,11.24,5.2,'g');line(s,10.67,5.2,11.24,5.2,'g');text(s,'=',11.42,3.78,1,.8,48,'g')
  band(s,'Different execution. Same expected semantics.')
 elif i==4:
  s=base(i,title,sec,src)
  for j,(num,name,target) in enumerate([('01','CODDTest','expression'),('02','DDLCheck','schema history'),('03','WriteCheck','transaction schedule'),('04','Radar','metadata')]):
   y=2.2+j*1.1;text(s,num,.9,y,1.1,.7,38,'g',font=SERIF);text(s,name,2.4,y+.04,4.4,.6,31,'ink',True);arrow(s,7.0,y+.35,7.87,y+.35);text(s,target,8.2,y+.06,4.1,.6,25,'gray');line(s,2.4,y+.88,12.4,y+.88)
 elif i==5:s=section(i,'01','CODDTest',title,'Constant Optimization Driven\nDatabase System Testing','Chi Zhang & Manuel Rigger  ·  PACMMOD / SIGMOD 2025')
 elif i in [6,7,8]:s=base(i,title,sec,src);toy(s,i-6)
 elif i==9:
  s=base(i,title,sec,'[C] §3.2 · dependent-expression mapping')
  tbl(s,['row','b','b + 5'],[['A',7,12],['B',12,17]],.9,2.7,5.6,.81,[(0,2),(1,2)],size=29)
  arrow(s,6.85,3.85,7.65,3.85,'g');text(s,'a mapping',8.0,2.88,4.2,.8,39,'g',font=SERIF);text(s,'CASE … THEN 12\n          … THEN 17',8.02,4.04,4.5,1.2,25)
  band(s,'A single replacement value would create an invalid oracle.')
 elif i==10:
  s=base(i,title,sec,src)
  label(s,'AUXILIARY VALUE',.9,2.22,5);text(s,'MIN(c0) → 1',.9,2.7,10,.8,44,'g',font=SERIF)
  rect(s,.9,4.00,11.5,.82,'light');text(s,'c0 IN (SELECT MIN(c0) FROM t0)',1.12,4.21,11,.45,29)
  arrow(s,2.35,5.0,2.35,5.51,'g');text(s,'c0 IN (1)',3.02,5.18,8.5,.7,36,'g',True)
  text(s,'Changing fragment only; the surrounding predicate stays unchanged.',.92,6.32,11.5,.3,16,'gray')
 elif i==11:
  s=base(i,title,sec,src)
  result(s,'ORIGINAL / SUBQUERY','no rows',.92,2.3,4.73)
  result(s,'FOLDED / CONSTANT','1',7.59,2.3,4.73,True)
  text(s,'≠',6.01,3.35,1.1,1,55,'g',font=SERIF,align=PP_ALIGN.CENTER)
  band(s,'Observed on MySQL 8.0.32 · auxiliary value = 1')
 elif i==12:
  s=base(i,title,sec,'[C] Table 1 & §4.2 · counts as reported')
  stats(s,['45','24','11'],['new bugs','logic bugs','not detected by\ncompared oracles'])
  text(s,'5 DBMSs',.94,5.6,3,.5,24,'gray',True);text(s,'SQLite · MySQL · CockroachDB · DuckDB · TiDB',4.13,5.64,8.2,.5,19,'gray')
  band(s,'Manual comparison on found cases—not universal dominance.',6.21)
 elif i==13:s=section(i,'02','DDLCheck',title,'Detecting Schema-Related Logic Bugs\nvia Equivalent Database Construction','Jiansen Song et al.  ·  PVLDB 2025')
 elif i==14:
  s=base(i,title,sec,src)
  label(s,'EVOLVED',.86,2.12,4)
  for x,t in [(1,'CREATE'),(4.25,'ALTER'),(7.5,'RENAME')]:node(s,t,x,2.68,2.24,.78)
  arrow(s,3.43,3.07,4.07,3.07);arrow(s,6.67,3.07,7.31,3.07);arrow(s,9.93,3.07,11.45,3.07,'g')
  label(s,'DIRECT',.86,4.09,4);node(s,'CREATE',1,4.63,2.24,.78);arrow(s,3.44,5.01,11.45,5.01,'g');line(s,11.8,3.07,11.8,5.01,'g',2)
  text(s,'same schema',8.4,5.8,4.2,.65,33,'g',font=SERIF);text(s,'+ same relevant state',8.4,6.4,4.2,.28,16,'gray')
 elif i==15:
  s=base(i,title,sec,src)
  labs=[('Generate','DDL history'),('Extract','final schema'),('Synthesise','direct history'),('Compare','same workload')]
  for j,(a,b) in enumerate(labs):
   x=.85+j*3.12;circle(s,str(j+1),x,2.5,.57);text(s,a,x,3.43,2.7,.61,31,'ink',True);text(s,b,x,4.28,2.6,.83,23,'gray')
   if j<3:arrow(s,x+.72,2.78,x+2.76,2.78,'g',1.8)
  band(s,'The second construction path is the control.')
 elif i==16:
  s=base(i,title,sec,'[D] DDL sequence optimisation & ablation')
  label(s,'REDUNDANT HISTORIES',.9,2.19,5);label(s,'DISTINCT TEST STATES',7.38,2.19,5)
  for j in range(3):
   y=3.0+j*.79
   for k in range(3):rect(s,1.05+k*1.38,y,1.06,.37,'rule')
  arrow(s,5.58,4.04,6.73,4.04,'g',2)
  for j,n in enumerate([2,3,4]):
   y=3.0+j*.79
   for k in range(n):rect(s,7.45+k*1.14,y,.83,.37,'g' if k==n-1 else 'rule')
  text(s,'same end state',1.03,5.72,4.7,.4,20,'gray');text(s,'different end states',7.44,5.72,4.75,.4,20,'gray')
  band(s,'Vary the histories—not just their length.')
 elif i in [17,18]:s=base(i,title,sec,src);fk(s,i==18)
 elif i==19:
  s=base(i,title,sec,src)
  result(s,'EVOLVED SCHEMA','ERROR 1452',.91,2.3,5.2,True)
  result(s,'DIRECT SCHEMA','inserted: 1',7.18,2.3,5.2)
  text(s,'error still references t0',.93,5.26,5.2,.8,25,'g',True)
  text(s,'foreign key is satisfied',7.2,5.26,5.2,.8,25,'ink')
  text(s,'Visible metadata in the evolved schema references t2.',.93,6.35,11.5,.32,17,'gray')
 elif i==20:
  s=base(i,title,sec,'[D] Table 2 & §6 · counts as reported')
  text(s,'34',.9,2.15,3.3,1.5,93,'gray',font=FONT);text(s,'submitted',.96,3.95,3.3,.7,27,'gray')
  arrow(s,4.0,3.05,5.23,3.05,'g',2.5)
  text(s,'29',5.65,2.15,4,1.5,93,'g',font=FONT);text(s,'confirmed new',5.7,3.95,5.4,.7,27,'ink',True)
  text(s,'21 schema-related  +  8 crashes',5.7,5.13,6.85,.8,26,'g');label(s,'6 DBMSs · 9 fixed at reporting point',.95,6.33,11,'gray',14)
 elif i==21:s=section(i,'03','WriteCheck','Change the schedule.\nCompare the writes.','Simple Testing Can Expose\nMost Critical Transaction Bugs','Ziyu Cui et al.  ·  PVLDB 2025')
 elif i==22:
  s=base(i,title,sec,'[W] §2.2 · transaction scope')
  label(s,'IN SCOPE',.94,2.32,5,'g',15);label(s,'OUTSIDE THE CENTRAL SETTING',7.12,2.32,5.3,'gray',15)
  rect(s,.94,3.08,5.26,1.61,'pale');text(s,'UPDATE t\nSET a = a + 1',1.18,3.37,4.8,1.13,30,'g',True)
  text(s,'SELECT → application logic\n       → dependent write',7.13,3.21,5.27,1.58,27)
  line(s,6.61,2.3,6.61,5.85,'rule')
  band(s,'A write may read rows internally; a prior separate read is the issue.')
 elif i==23:
  s=base(i,title,sec,'[W] §3.3–4 · FCRFS reference construction')
  node(s,'concurrent run',.96,2.5,3.17,.85);arrow(s,4.35,2.92,5.0,2.92)
  text(s,'finish order',5.31,2.5,3.1,.72,29,'g',True)
  arrow(s,8.25,2.92,9.06,2.92);node(s,'T1 → T2',9.3,2.5,2.9,.85,True)
  text(s,'recreate initial state',2.74,4.27,4.5,.6,26,'gray');arrow(s,7.42,4.55,8.47,4.55);text(s,'serial replay',8.76,4.22,3.65,.62,29,'g',True)
  band(s,'First commit / rollback → first scheduled. Compare final writes.')
 elif i==24:
  s=base(i,title,sec,src);tbl(s,['a','b'],[['NULL',1],[2,2],['NULL',3]],.96,2.63,3.43,.69,size=28)
  label(s,'T1',5.08,2.4,2,'g',16);text(s,'UPDATE t SET a = 10',5.08,2.97,7.2,.7,30,'ink',True)
  label(s,'T2',5.08,4.11,2,'g',16);text(s,'UPDATE t SET b = 20\nWHERE a',5.08,4.66,7.3,1.14,30,'ink',True)
  label(s,'Both transactions: READ COMMITTED',.98,6.33,11,'gray',14)
 elif i==25:s=base(i,title,sec,src);timeline(s,1)
 elif i==26:s=base(i,title,sec,src);timeline(s,2)
 elif i==27:
  s=base(i,title,sec,src)
  label(s,'OBSERVED',.96,2.14,5,'g',15);label(s,'TROC MVCC ORACLE',7.76,2.14,5,'gray',15)
  tbl(s,['a','b'],[[10,1],[10,20],[10,20]],.96,2.69,4.51,.71,[(0,1)],size=28)
  tbl(s,['a','b'],[[10,20],[10,20],[10,20]],7.76,2.69,4.51,.71,[(0,1)],size=28)
  text(s,'≠',6.14,3.65,1,.9,49,'g',font=SERIF)
  band(s,'Replayed with Troc—not a run of the WriteCheck tool.')
 elif i==28:
  s=base(i,title,sec,'[W] historical study & Table 2 · distinct populations')
  label(s,'HISTORICAL STUDY',.97,2.22,5);label(s,'NEW TESTING CAMPAIGN',7.1,2.22,5)
  text(s,'32 / 35',.94,2.77,5.5,1.31,77,'g',font=FONT);text(s,'studied bugs violate WSS',1.01,4.22,5.36,.95,25,'ink',True)
  text(s,'22',7.12,2.77,2.4,1.24,77,'g',font=FONT);text(s,'unique\nviolations',9.46,3.22,3.0,1,24)
  text(s,'11 new bugs',7.13,4.65,5.3,.53,30,'ink',True);text(s,'9 false positives',7.13,5.36,5.3,.48,27,'gray')
  line(s,6.42,2.16,6.42,6.03)
  text(s,'Not “91.4% of all database bugs”.',1.0,6.31,10.9,.39,19,'gray')
 elif i==29:s=section(i,'04','Radar',title,'Detecting Metadata-Related Logic Bugs\nvia Raw Database Construction','Jiansen Song et al.  ·  PVLDB 2024')
 elif i==30:
  s=base(i,title,sec,src)
  label(s,'INDEXED COPY',.9,2.15,4);label(s,'RAW COPY',.9,4.15,4)
  node(s,'data + metadata',.9,2.62,3.3);node(s,'data only',.9,4.62,3.3)
  for y,r in [(2.62,'result A'),(4.62,'result B')]:
   arrow(s,4.35,y+.36,5.1,y+.36);node(s,'same query',5.3,y,2.7,.75);arrow(s,8.15,y+.36,8.9,y+.36);node(s,r,9.1,y,2.2,.75)
  line(s,11.5,3.0,12.0,3.0,'g');line(s,12.0,3.0,12.0,5.0,'g');line(s,11.5,5.0,12.0,5.0,'g');text(s,'=',12.1,3.62,.5,.7,40,'g')
  band(s,'Same data. Same query. Only the metadata differs.')
 elif i==31:
  s=base(i,title,sec,src)
  label(s,'INDEXED COPY',.92,2.02,5,'g',13);label(s,'RAW COPY',7.1,2.02,5,'gray',13)
  code1='CREATE TABLE t0 (c0 DOUBLE ZEROFILL);\nCREATE INDEX i0 ON t0 (c0 DESC);\nINSERT INTO t0 VALUES (0);'
  code2='CREATE TABLE t0 (c0 DOUBLE ZEROFILL);\n\nINSERT INTO t0 VALUES (0);'
  rect(s,.92,2.4,5.6,1.55,'pale');text(s,code1,1.05,2.52,5.4,1.35,15,'g',True)
  rect(s,7.1,2.4,5.6,1.55,'light');text(s,code2,7.23,2.52,5.4,1.35,15)
  text(s,'SELECT COUNT(*) FROM t0 WHERE\n  (IFNULL(-1123870957, \'\')) IN (t0.c0);',.92,4.13,11.7,.7,18,'ink')
  text(s,'1',1.5,4.78,1.5,1.3,66,'g',font=SERIF);text(s,'matching row',3.0,5.4,3.3,.4,17,'g',True)
  text(s,'0',7.7,4.78,1.5,1.3,66,font=SERIF);text(s,'matching rows · correct',9.0,5.4,3.7,.4,17,'ink',True)
  text(s,'≠',6.38,4.95,.9,.9,46,'g',font=SERIF,align=PP_ALIGN.CENTER)
  band(s,'MySQL 8.0.32 · the indexed copy is the bug',6.16)
 elif i==32:
  s=base(i,title,sec,'[A] §4 Tables 2–3 · counts as reported')
  for x,n,l in zip([.86,4.95,9.04],['19 vs 12','22 vs 14','30 of 38'],['TiDB, 12 hours\nwith vs without metadata guidance','five DBMSs, unique bugs\nwith vs without guidance','confirmed new bugs\nare metadata-related']):
   text(s,n,x,2.35,4.0,1.3,52,'g',font=FONT);text(s,l,x,3.95,3.9,1.0,20,'ink',True)
  band(s,'One study, one generator—not a general rate.',6.12)
 elif i==33:
  s=base(i,title,sec,src)
  label(s,'WHAT WE REPLAYED',.94,2.1,7,'g',14)
  rows=[('CODDTest case','query-result mismatch','direct SQL'),('DDLCheck case','schema-history mismatch','direct SQL'),('Transaction case','final-state mismatch','Troc harness'),('Radar case','indexed vs raw count','direct SQL')]
  for j,(a,b,c) in enumerate(rows):
   y=2.6+j*.8;text(s,a,.96,y,3.58,.52,25,'ink',True);text(s,b,4.82,y,4.45,.52,23);text(s,c,9.6,y,2.8,.55,22,'g',True);line(s,.95,y+.64,12.36,y+.64)
  band(s,'One MySQL release. Selected symptoms. No coverage ranking.')
 elif i==34:
  s=base(i,title,sec,src)
  label(s,'PAPER',.95,2.15,3);label(s,'CHANGE',4.64,2.15,3);label(s,'COMPARE',8.74,2.15,3)
  for j,row in enumerate([('CODDTest','expression','query results'),('DDLCheck','schema history','later behaviour'),('WriteCheck','schedule','write effects'),('Radar','metadata','query results')]):
   y=2.7+j*.8
   text(s,row[0],.95,y,3.4,.57,27,'g',True);text(s,row[1],4.64,y,3.73,.57,27);text(s,row[2],8.74,y,3.7,.57,27);line(s,.95,y+.66,12.4,y+.66)
  text(s,'Complementary—not interchangeable.',.96,6.35,11.3,.38,22,'gray')
 elif i==35:
  s=base(i,title,sec,src)
  for j,(a,b) in enumerate([('CODDTest','values · types · row dependence'),('DDLCheck','schema · constraints · state'),('WriteCheck','transaction scope · DBMS semantics'),('Radar','metadata that must not alter results')]):
   y=2.2+j*1.0;text(s,a,.97,y,3.46,.63,28,'g',True);text(s,b,4.65,y+.05,7.64,.6,26);line(s,.97,y+.8,12.4,y+.8)
 elif i==36:
  s=base(i,'',sec,'Questions',dark=True)
  label(s,'TAKEAWAY',.84,.76,8,'white',15)
  text(s,'When you cannot\npredict the answer,',.82,1.55,11.8,1.81,48,'white',font=SERIF)
  text(s,'specify what must\nstay the same.',.82,3.35,11.8,1.87,48,'white',font=SERIF)
  text(s,'Substitute.   Reconstruct.   Reschedule.   Strip.',.87,6.11,11.8,.51,25,'white',True)
 LAYOUTS.append(s)

# --- Backup slides: not part of the 25-minute route -------------------------
BACKUPS=[
 dict(title='The complete changing-predicate context',section='BACKUP · CODDTEST',spoken=['The membership fragment is not a standalone reproducer. These two predicate forms keep the regular expression, like comparison, and case expression unchanged. Refer to the repository script for an executable copy.',''],pause=0,cue='Use only if asked. Do not read every SQL token.',source='C,R',takeaway='Full context matters.',backup=True,wpm=120),
 dict(title='The foreign-key case in six lines',section='BACKUP · DDLCHECK',spoken=['This is the compact schema-history sequence. The directly created control starts with the renamed parent table and skips the alteration. These statements are representative SQL from the reproduced case.',''],pause=0,cue='Point to ALGORITHM COPY; it is part of this case.',source='D,R',takeaway='Same final schema; different construction.',backup=True,wpm=120),
 dict(title='Two WSS variants—not full serializability',section='BACKUP · WRITECHECK',spoken=['The paper defines transaction-level and statement-level WSS. The first compares with a corresponding serial transaction execution. The latter removes aborted transactions and transaction boundaries from committed work before the reference execution. These variants are not a statement that every read observation is serializable. Savepoint and rollback details require the paper’s full definitions.',''],pause=0,cue='Use the table to distinguish the property from the reference generator and from our Troc replay.',source='W',takeaway='Keep the property, the generator and the harness distinct.',backup=True,wpm=120),
 dict(title='What the evaluations establish',section='BACKUP · EVIDENCE',spoken=['The reported bug totals measure different populations, tool scopes, and experiments. CODDTest compares other oracles on found cases; DDLCheck investigates schema coverage and a generator ablation; WriteCheck combines a historical study with new testing; Radar reports a TiDB and five-system ablation. Raw bug totals are not a reliability ranking of the tested databases.',''],pause=0,cue='Answer the methodological question, rather than reading all the counts.',source='C,D,W,A',takeaway='Do not rank DBMS reliability from these totals.',backup=True,wpm=120),
 dict(title='Research sources',section='BACKUP · REFERENCES',spoken=['These are the four primary papers, with links in the notes and in the project’s papers folder. Our evidence files and the Troc artifact are cited separately.',''],pause=0,cue='Keep this slide available during questions.',source='C,D,W,A,R,T',takeaway='Primary papers and reproduction evidence are separate sources.',backup=True,wpm=120),
 dict(title='Delivery and visual-design sources',section='BACKUP · REFERENCES',spoken=['The typography and palette follow uOttawa’s public Horizon guidance. The timing model counts the spoken words and adds explicit pauses and slide changes. The gesture and pause cues support comprehension; they are not a requirement to perform mechanically. A real rehearsal is needed to calibrate the duration.',''],pause=0,cue='Not a spoken main-route slide. Use the speaker script for calibration details.',source='B,P',takeaway='Model timing; measure actual delivery.',backup=True,wpm=120),
]
for k,d in enumerate(BACKUPS,37):
 s=base(k,d['title'],d['section'],'Backup · outside the main talk')
 if k==37:
  text(s,'t0(c0 BOOL) contains TRUE;  MIN(c0) = 1',.85,1.96,11.7,.48,23,'g',True)
  label(s,'SAME SURROUNDING PREDICATE',.87,2.68,11)
  code="('0') NOT REGEXP (\n  c0 NOT LIKE (CASE c0 WHEN 76 THEN 0.7 ELSE c0 END)\n) AND c0 IN ( … )"
  rect(s,.85,3.12,11.55,1.83,'light');text(s,code,1.05,3.35,11.13,1.5,23)
  text(s,'original:  SELECT MIN(c0) FROM t0',.89,5.35,11.2,.5,26)
  text(s,'folded:   1',.89,6.02,11.2,.5,26,'g',True)
 elif k==38:
  code='CREATE TABLE t0(c2 FLOAT8 PRIMARY KEY);\nCREATE TABLE t1(c1 FLOAT8 UNIQUE,\n  FOREIGN KEY(c1) REFERENCES t0(c2) ON UPDATE CASCADE);\nALTER TABLE t0 RENAME AS t2, ALGORITHM COPY;\nINSERT INTO t2 VALUES(1);\nINSERT INTO t1 VALUES(1);   -- rejected on the evolved path'
  rect(s,.87,2.08,11.57,3.91,'light');text(s,code,1.08,2.42,11.1,3.4,23)
  text(s,'Control: create t2 directly, then create t1 referencing t2.',.89,6.28,11.3,.46,21,'g',True)
 elif k==39:
  rows=[('tx-WSS','serial transaction reference'),('stmt-WSS','statement-level reference construction'),('Troc replay','MVCC-based oracle; a different harness')]
  for j,(a,b) in enumerate(rows):
   y=2.36+j*1.26;text(s,a,.97,y,3.38,.72,29,'g',True);text(s,b,4.65,y+.06,7.61,.98,26);line(s,.96,y+.99,12.4,y+.99)
 elif k==40:
  for j,(a,b) in enumerate([('CODDTest','5 systems; oracle comparison on found cases'),('DDLCheck','6 systems; schema coverage + ablation'),('WriteCheck','35 historical bugs + a new testing campaign'),('Radar','5 systems; metadata-guidance ablation')]):
   y=2.0+j*1.0;text(s,a,.94,y,3.7,.7,29,'g',True);text(s,b,4.79,y+.02,7.5,.88,25);line(s,.94,y+.82,12.38,y+.82)
  text(s,'Different campaigns and scopes → no apples-to-apples leaderboard.',.95,6.3,11.5,.51,21,'gray')
 elif k==41:
  entries=[('C / CODDTest','Zhang & Rigger · PACMMOD 3(1), Article 24, 2025','doi.org/10.1145/3709674'),('D / DDLCheck','Song et al. · PVLDB 18(7), 2281–2294, 2025','vldb.org/pvldb/vol18/p2281-song.pdf'),('W / WriteCheck','Cui et al. · PVLDB 18(8), 2547–2560, 2025','vldb.org/pvldb/vol18/p2547-cui.pdf'),('A / Radar','Song et al. · PVLDB 17(8), 1884–1897, 2024','vldb.org/pvldb/vol17/p1884-song.pdf')]
  for j,(a,b,c) in enumerate(entries):
   y=1.95+j*1.2;text(s,a,.94,y,3.5,.55,25,'g',True);text(s,b,4.61,y,7.71,.55,23);text(s,c,4.61,y+.56,7.71,.46,19,'gray');line(s,.94,y+1.08,12.39,y+1.08)
 elif k==42:
  for j,(a,b) in enumerate([('Visual identity','uOttawa Horizon · colours, typography, logo'),('Pace + rehearsal','Microsoft Speaker Coach · Trent Academic Skills'),('Purposeful delivery','Trent Academic Skills · Toastmasters')]):
   y=2.15+j*1.18;text(s,a,.94,y,3.65,.75,26,'g',True);text(s,b,4.79,y+.03,7.49,.86,24);line(s,.94,y+.98,12.39,y+.98)
  band(s,'Pause lengths and gesture placements are rehearsal choices.')
 LAYOUTS.append(s)
ALL=SLIDES+BACKUPS

# --- Timing audit, embedded notes, script -----------------------------------
WORD_RE=re.compile(r"[A-Za-z]+(?:[’'-][A-Za-z]+)*|\d+(?:\.\d+)*")
def words(t):return len(WORD_RE.findall(t))
def clock(sec):
 sec=int(round(sec));return f'{sec//60:02}:{sec%60:02}'
rows=[];cumulative=0
script=['# CSI 5137 — Speaker script and delivery plan','',
'**Deck:** Testing databases without an answer key. 36 main slides; 6 backup slides. Student course project, not an official university presentation.','',
'## Timing model — estimate, not a stopwatch guarantee','',
'The main-route count includes spoken prose only. Cues, titles, citations and backup answers are excluded. English words are counted by the regular expression in `source/build_deck.py`; contractions/hyphenated compounds count as one. SQL is explained, not read token by token.','',
'For each main slide: `seconds = 60 × spoken words / 120 + explicit silent hold + 1 second to advance`. The last main slide has no advance allowance. Gestures and gaze changes happen during speech and are not double-counted. Ordinary phrasing is absorbed into the gross speaking-rate assumption; the extra holds below are intentionally silent.','',
'The 120-wpm planning rate is an authored choice. Microsoft suggests a broad 100–165-wpm range, while Trent recommends roughly 100–120 for formal delivery. Neither source guarantees a duration for this talk. Exact holds of 2–4 seconds are reading/rehearsal choices, not scientifically optimal constants.','',
'## Cue conventions','',
'- `[SHOW]`: direct attention to content already visible. No hidden object animations are required.','- `[PAUSE Ns]`: deliberate silence; do not fill it with extra commentary.','- `[LOOK]`, `[GESTURE]`, `[MOVE]`: optional delivery guidance, performed during speech unless inside the marked pause. Stay seated or at a lectern when appropriate; movement is not mandatory.','- `[NEXT]`: advance once at the end of the slide. Slides 6–8, 17–19 and 24–27 form progressive visual sequences. Do not click midway through a sentence.','',
'## Rehearsal procedure','',
'Record a two-minute representative method section, including its prescribed pauses. Calculate actual spoken wpm using the transcript and subtract only the explicit holds from the recording time. Rehearse the full talk next; a formula is not a substitute. Aim to finish the main route at roughly 23–24 minutes and use the remaining time for recovery or questions. If your pace is nearer 110 wpm, shorten the script before presenting; do not simply rush the technical parts.','',
'Use natural pauses and meaningful gestures rather than acting every instruction. Point briefly, return your gaze to the audience, and move only at the four section changes. No continuous pacing, laser-pointer circling, or turning your back to read slides. For remote delivery, remain seated and gesture within camera view.','',
'## Main-route checkpoints','']
sections={}
for idx,(d,sld) in enumerate(zip(ALL,LAYOUTS),1):
 n=words(' '.join(d['spoken']));advance=0 if d['backup'] or idx==36 else 1
 dur=n/d['wpm']*60+d['pause']+advance
 start=cumulative
 if not d['backup']:cumulative+=dur;sections[d['section']]=cumulative
 r=dict(slide=idx,title=d['title'],route='backup' if d['backup'] else 'main',spoken_words=n,wpm=d['wpm'],silent_seconds=d['pause'],advance_seconds=advance,model_seconds=round(dur,1),start=clock(start) if not d['backup'] else '',end=clock(cumulative) if not d['backup'] else '')
 rows.append(r)
 note=[f"SLIDE {idx:02} — {d['title']}",f"{'BACKUP: not budgeted' if d['backup'] else 'MODEL '+r['start']+'–'+r['end']} | {n} spoken words | 120 wpm | {d['pause']}s hold | {advance}s advance",'',f"[PACE] {d['wpm']} words per minute; articulate rather than rush.",f"[SHOW] {d['takeaway']}",'[LOOK] Briefly check the highlighted element, then return your gaze to the audience.',('[GESTURE] One open-hand contrast or one directional trace; then return to neutral.' if idx in [3,4,6,7,8,9,10,11,14,15,16,17,18,19,22,23,24,25,26,27,30,34] else '[GESTURE] Hands relaxed; a small emphasis gesture is enough.'),('[MOVE] Optional single position change at this section boundary; then stand still. Stay seated if appropriate.' if idx in [5,13,21,29] else '[MOVE] Stay in place; do not pace.'),f"[DELIVERY] {d['cue']}",'',d['spoken'][0]]
 if d['pause']:note.extend(['',f"[PAUSE {d['pause']}s] Read/compare the visual silently."])
 if d['spoken'][1]:note.extend(['',d['spoken'][1]])
 note.extend(['', '[NEXT] Advance one slide.' if idx<36 else ('[STOP] Invite questions; do not enter the appendix automatically.' if idx==36 else '[BACKUP] Return to the main discussion.'),'','SOURCE / SCOPE NOTES'])
 for key in d['source'].split(','):
  if key:note.append(f'[{key}] {SOURCES[key]}')
 sld.notes_slide.notes_text_frame.text='\n'.join(note)
 d['notes']='\n'.join(note)
# Add model checkpoints before slide-by-slide notes.
for sec,end in sections.items():script.append(f'- End of {sec.title()}: **{clock(end)}** (model).')
mainwords=sum(r['spoken_words'] for r in rows if r['route']=='main');holds=sum(d['pause'] for d in SLIDES)
script+=['',f'**Main-route total: {mainwords:,} spoken words + {holds}s explicit silence + 35s transitions = {clock(cumulative)} at 120 wpm.**',f'**Remaining to 25:00: {clock(1500-cumulative)}.** This is contingency, not a promise of exact delivery.','', '| Assumed speaking rate | Model duration |','|---|---|']
for rate in [110,115,120,125,130]:script.append(f'| {rate} wpm | {clock(mainwords/rate*60+holds+35)} |')
script+=['','If the 25 minutes must include a full question period, shorten the main route further. The current reserve is not a five-minute Q&A allocation.','','## Main script','']
for idx,d in enumerate(ALL,1):
 if idx==37:script+=['','## Backup answers — outside the timed route','']
 r=rows[idx-1]
 script+=['',f"### {idx:02} · {d['title']}",'',f"**{'Backup / outside timed route' if d['backup'] else r['start']+'–'+r['end']} · {r['spoken_words']} spoken words · {d['pause']}s silent hold**",'',f"[PACE] 120 wpm. [SHOW] {d['takeaway']}",'']
 cue_lines=d['notes'].split('[LOOK]',1)[1].split(d['spoken'][0],1)[0].strip()
 script+=['[LOOK]'+cue_lines,'',d['spoken'][0],'']
 if d['pause']:script += [f"**[PAUSE {d['pause']}s]** Let the audience read or compare the visual.",'']
 if d['spoken'][1]:script += [d['spoken'][1],'']
 script += [('**[NEXT]** Advance once.' if idx<36 else ('**[STOP]** Invite questions. Do not enter the appendix automatically.' if idx==36 else '**[BACKUP]** Return to the discussion.')),'',f"Sources: [{d['source'].replace(',', '], [')}]. See the reference list below.",'']
script+=['','## Research and delivery references','']
for key,v in SOURCES.items():script.append(f'[{key}] {v}\n')
(OUT/'speaker_script.md').write_text('\n'.join(script),encoding='utf-8')
with (OUT/'timing.csv').open('w',newline='',encoding='utf-8') as f:
 writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
(OUT/'timing_summary.json').write_text(json.dumps({'main_slides':36,'backup_slides':6,'spoken_words':mainwords,'explicit_hold_seconds':holds,'advance_seconds':35,'base_wpm':120,'model_seconds':cumulative,'reserve_to_25_minutes_seconds':1500-cumulative,'checkpoints':{k:clock(v) for k,v in sections.items()}},indent=2),encoding='utf-8')
cue=['# At-a-glance cue sheet','','The full script is in `speaker_script.md`; these are prompts, not extra spoken words.','']
for i,d in enumerate(SLIDES,1):cue += [f"**{i:02} · {rows[i-1]['start']}–{rows[i-1]['end']} · {d['title']}**",f"{d['takeaway']}  | Silent hold: {d['pause']}s",f"Delivery: {d['cue']}",'']
(OUT/'cue_sheet.md').write_text('\n'.join(cue),encoding='utf-8')
for slide in P.slides:
 for sh in slide.shapes:
  for el in sh._element.xpath('.//a:effectRef'):
   el.set('idx','0')
P.save(OUT/'CSI5137_ATDM_visual_deck_v2.pptx')
print(json.dumps({'slides':len(P.slides),'words':mainwords,'seconds':cumulative,'reserve':1500-cumulative}))
