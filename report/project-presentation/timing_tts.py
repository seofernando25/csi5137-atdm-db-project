import sys,re,wave,json
sys.path.insert(0,'/home/fer/Documents/csi5137-atdm-db-project/presentation/v2/source')
import content
from piper import PiperVoice
v=PiperVoice.load('en_US-lessac-medium.onnx')
tot=0;n=0;hold=0;words=0
for i,s in enumerate([x for x in content.SLIDES if not x['backup']],1):
    txt=' '.join(x for x in s['spoken'] if x)
    w=wave.open('/tmp/claude-1000/voice/s.wav','wb')
    v.synthesize_wav(txt,w); w.close()
    r=wave.open('/tmp/claude-1000/voice/s.wav'); d=r.getnframes()/r.getframerate(); r.close()
    tot+=d;hold+=s['pause'];n+=1;words+=len(txt.split())
adv=n-1
print('slides',n,'words',words,'speech_s',round(tot),'holds',hold,'adv',adv)
T=tot+hold+adv
print('total %d:%02d'%(T//60,T%60),'wpm_effective',round(words/(tot/60)))
