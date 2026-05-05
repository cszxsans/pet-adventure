# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

content = open(r'D:\game_dev\pet-adventure\index.html','r',encoding='utf-8').read()

# Replace the entire rCapturePanel function with a responsive version
old_fn = '''function rCapturePanel(){
  X.fillStyle='rgba(0,0,0,.85)';
  X.fillRect(160,280,400,420);
  
  X.strokeStyle='#ffd700';
  X.lineWidth=3;
  rr(160,280,400,420,15);
  X.stroke();
  
  X.fillStyle='#ffd700';
  X.font='bold 32px sans-serif';
  X.textAlign='center';
  X.fillText('ѵ�������',W/2,330);
  
  const balls=[
    {t:'normal',n:'��ͨ��',c:G.player.balls.normal,ap:4,rt:'30%'},
    {t:'super',n:'������',c:G.player.balls.super,ap:3,rt:'50%'},
    {t:'master',n:'��ʦ��',c:G.player.balls.master,ap:1,rt:'85%'}
  ];
  
  balls.forEach(function(b,i){
    const by=380+i*90;
    const ok=b.c>0&&G.battle.ap>=b.ap;
    btn(b.n+' x'+b.c+' ('+b.rt+' AP'+b.ap+')',180,by,360,70,ok?'#2a4a2a':'#333','#fff',ok?'#44ff44':'#666');
  });
  
  btn('ȡ��',W/2-80,680,160,50,'#4a2a2a','#fff','#666');
}'''

new_fn = '''function rCapturePanel(){
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
  X.fillText('\u9009\u62e9\u5ba0\u7269\u7403',W/2,py+40);
  
  var balls=[
    {t:'normal',n:'\u666e\u901a\u7403',c:G.player.balls.normal,ap:4,rt:'30%'},
    {t:'super',n:'\u8d85\u7ea7\u7403',c:G.player.balls.super,ap:3,rt:'50%'},
    {t:'master',n:'\u5927\u5e08\u7403',c:G.player.balls.master,ap:1,rt:'85%'}
  ];
  
  var itemH=Math.min(65,Math.max(45,(ph-130)/3));
  balls.forEach(function(b,i){
    var by=py+70+i*(itemH+8);
    var ok=b.c>0&&G.battle.ap>=b.ap;
    var bf=Math.max(12,Math.min(16,W*0.04));
    btn(b.n+' x'+b.c+' (AP'+b.ap+'|'+b.rt+')',px+10,by,pw-20,itemH,ok?'#2a4a2a':'#333','#fff',ok?'#44ff44':'#666',bf);
  });
  
  var bh=Math.min(50,Math.max(36,(ph-130)-3*(itemH+8)-15));
  btn('\u53d6\u6d88',px+pw/2-80,py+ph-bh-10,160,bh,'#4a2a2a','#fff','#666');
}'''

if old_fn in content:
    content = content.replace(old_fn, new_fn)
    print('rCapturePanel replaced successfully')
else:
    print('ERROR: old function not found, searching...')
    idx = content.find('function rCapturePanel')
    if idx >= 0:
        end = content.find('function rResult', idx)
        print('Found at', idx, 'to', end)
        print(repr(content[idx:end]))

# Also fix hBattle capture panel hit detection
old_hc = '''  if(G.ui.capturePanel){
    const balls=[{t:'normal',ap:4},{t:'super',ap:3},{t:'master',ap:1}];
    balls.forEach(function(b,i){
      const by=380+i*90;
      if(mx>=180&&mx<=540&&my>=by&&my<=by+70){
        doCapture(b.t,b.ap);return;
      }
    });
    if(mx>=W/2-80&&mx<=W/2+80&&my>=680&&my<=730)
      G.ui.capturePanel=false;
    return;
  }'''

new_hc = '''  if(G.ui.capturePanel){
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

if old_hc in content:
    content = content.replace(old_hc, new_hc)
    print('hBattle capture panel hit detection replaced successfully')
else:
    print('ERROR: old hBattle capture code not found')

with open(r'D:\game_dev\pet-adventure\index.html','w',encoding='utf-8') as f:
    f.write(content)
print('File saved!')