# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

content = open(r'D:\game_dev\pet-adventure\index.html','r',encoding='utf-8').read()

# Find and replace rCapturePanel using binary search on raw UTF-8 bytes
raw = content.encode('utf-8')
start = raw.find(b'function rCapturePanel')
end = raw.find(b'\nfunction rResult', start)
print(f'Found rCapturePanel at byte {start} to {end} (len={end-start})')

new_fn_utf8 = b'''function rCapturePanel(){
  var pw=Math.min(400,W-40);
  var ph=450;
  var px=(W-pw)/2;
  var py=Math.max(80,(H-ph)/2-20);
  
  X.fillStyle='rgba(0,0,0,.9)';
  X.fillRect(px,py,pw,ph);
  
  X.strokeStyle='#ffd700';
  X.lineWidth=3;
  rr(px,py,pw,ph,15);
  X.stroke();
  
  var fs=Math.min(28,Math.max(18,W*0.07));
  X.fillStyle='#ffd700';
  X.font='bold '+fs+'px sans-serif';
  X.textAlign='center';
  X.fillText('\xe9\x80\x89\xe6\x8b\xa9\xe5\xae\xb6\xe7\x89\xa9\xe7\x90\x83',W/2,py+40);
  
  var balls=[
    {t:'normal',n:'\xe6\x99\xae\xe9\x80\x9a\xe7\x90\x83',c:G.player.balls.normal,ap:4,rt:'30%'},
    {t:'super',n:'\xe8\xb6\x85\xe7\xba\xa7\xe7\x90\x83',c:G.player.balls.super,ap:3,rt:'50%'},
    {t:'master',n:'\xe5\xa4\xa7\xe5\xb8\x88\xe7\x90\x83',c:G.player.balls.master,ap:1,rt:'85%'}
  ];
  
  var itemH=Math.min(65,Math.max(45,(ph-130)/3));
  balls.forEach(function(b,i){
    var by=py+70+i*(itemH+8);
    var ok=b.c>0&&G.battle.ap>=b.ap;
    var bf=Math.max(12,Math.min(16,W*0.04));
    btn(b.n+' x'+b.c+' (AP'+b.ap+'|'+b.rt+')',px+10,by,pw-20,itemH,ok?'#2a4a2a':'#333','#fff',ok?'#44ff44':'#666',bf);
  });
  
  var bh=Math.min(50,Math.max(36,(ph-130)-3*(itemH+8)-15));
  btn('\xe5\x8f\x96\xe6\xb6\x88',px+pw/2-80,py+ph-bh-10,160,bh,'#4a2a2a','#fff','#666');
}'''

new_content = raw[:start] + new_fn_utf8 + raw[end:]
content = new_content.decode('utf-8')

# Now fix hBattle capture panel detection
# Find: old fixed coords for capture panel click detection
old_hc = raw.find(b'if(G.ui.capturePanel){')
if old_hc >= 0:
    old_hc_end = raw.find(b'}\n  \n  // \ufffd\ufffd\ufffd\ufffd\ufffd', old_hc)
    if old_hc_end < 0:
        old_hc_end = raw.find(b'return;', old_hc + 20) + 7
    print(f'hBattle capturePanel old code: {old_hc} to {old_hc_end}')
    
    # Replacement using relative coords
    new_hc_utf8 = b'''  if(G.ui.capturePanel){
    var pw=Math.min(400,W-40);
    var ph=450;
    var px=(W-pw)/2;
    var py=Math.max(80,(H-ph)/2-20);
    var itemH=Math.min(65,Math.max(45,(ph-130)/3));
    var balls=[{t:'normal',ap:4},{t:'super',ap:3},{t:'master',ap:1}];
    balls.forEach(function(b,i){
      var by=py+70+i*(itemH+8);
      if(mx>=px+10&&mx<=px+pw-10&&my>=by&&my<=by+itemH){
        doCapture(b.t,b.ap);return;
      }
    });
    var bh=Math.min(50,Math.max(36,(ph-130)-3*(itemH+8)-15));
    if(mx>=px+pw/2-80&&mx<=px+pw/2+80&&my>=py+ph-bh-10&&my<=py+ph-bh-10+bh)
      G.ui.capturePanel=false;
    return;
  }'''
    
    new_content = content.encode('utf-8')
    new_content = new_content[:old_hc] + new_hc_utf8 + new_content[old_hc_end:]
    content = new_content.decode('utf-8')
    print('hBattle capture panel detection replaced!')

with open(r'D:\game_dev\pet-adventure\index.html','w',encoding='utf-8') as f:
    f.write(content)
print('Done!')