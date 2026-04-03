import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\leo1.chen\Desktop\Analysis-Report-WR-CN\dp_js_payload.json', encoding='utf-8') as f:
    payload = f.read()

with open(r'C:\Users\leo1.chen\Desktop\机甲战队_0317版本首周报告.html', encoding='utf-8') as f:
    content = f.read()

dp_card_start = content.find('<div class="card-sub" style="margin-top:12px">3.5 数据板（DP）各档位')
dp_card_end = content.find('<div class="card-sub" style="margin-top:12px">3.5 各DP ARPPU')

parts = []
parts.append('<div class="card-sub" style="margin-top:12px">3.5 数据板（DP）各档位收入详析 · 分R交互看板</div>\n')
parts.append('  <div style="font-size:11px;color:#888;margin-bottom:6px">点击版本标签切换选中/取消；<strong>双击</strong>只保留该版本。按分R筛选后图表与表格实时联动。</div>\n')

# R filter buttons
parts.append('  <div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:6px;align-items:center">\n')
parts.append('    <span style="font-size:11px;color:#555">分R筛选：</span>\n')
for r_val, r_lbl in [("ALL","全部"),("0-100","0-100元"),("100-1000","100-1000元"),("1000-5000","1000-5000元"),("5000-20000","5000-2万元"),("20000+","2万元+")]:
    if r_val == "ALL":
        parts.append(f'    <button class="dp-rbtn" data-r="{r_val}" style="font-size:10px;padding:2px 9px;border:1px solid #37474f;border-radius:3px;background:#37474f;color:#fff;cursor:pointer">{r_lbl}</button>\n')
    else:
        parts.append(f'    <button class="dp-rbtn" data-r="{r_val}" style="font-size:10px;padding:2px 9px;border:1px solid #bbb;border-radius:3px;background:#f5f5f5;cursor:pointer">{r_lbl}</button>\n')
parts.append('    <span id="dp-r-lbl" style="font-size:10px;color:#e53935;margin-left:4px"></span>\n')
parts.append('  </div>\n')

# Version filter buttons
parts.append('  <div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px;align-items:center">\n')
parts.append('    <span style="font-size:11px;color:#555">版本：</span>\n')
ver_info = [("0317","0317 兀鹰","#e53935"),("0210","0210 泰特(春节)","#1976d2"),("0115","0115 探路者","#43a047"),("1209","1209 雷克斯+拳击手","#757575"),("1030","1030 杜克斯","#795548")]
for v, vn, vc in ver_info:
    parts.append(f'    <button class="dp-vbtn" data-ver="{v}" style="font-size:10px;padding:2px 10px;border:2px solid {vc};border-radius:3px;background:{vc};color:#fff;cursor:pointer">{vn}</button>\n')
parts.append('    <span style="font-size:10px;color:#aaa;margin-left:2px">单击切换 · 双击仅选该版本</span>\n')
parts.append('  </div>\n')

parts.append('  <div id="chart-dp-r" style="width:100%;height:300px"></div>\n')
parts.append('  <table id="dp-tbl" style="margin-top:8px;font-size:11px">\n')
parts.append('    <thead><tr><th>DP</th><th>类型</th><th>0317投放内容</th>')
for v, vn, vc in ver_info:
    parts.append(f'<th class="tr" id="dth-{v}" style="color:{vc}">{v}</th>')
parts.append('<th class="tr">vs 0210</th></tr></thead>\n')
parts.append('    <tbody id="dp-tbody"></tbody>\n  </table>\n')
parts.append('  <div id="dp-insight" class="ins b" style="margin-top:8px"></div>\n\n')

# JS
js = """<script>
(function(){
var D=__PAYLOAD__;
var DORDER=["DP1","DP2","DP3","DP4","DP5","DP7","DP8","DP10","DP11","DP12","DPPass"];
var DTYPE={DP1:"入门混池",DP2:"白银武器",DP3:"白银机甲",DPPass:"数据板通行证",DP4:"黄金武器",DP5:"黄金机甲",DP7:"老泰坦",DP8:"活动纯净",DP10:"本期机武",DP11:"新泰坦",DP12:"限量版"};
var RSEGS=["0-100","100-1000","1000-5000","5000-20000","20000+"];
var aV={"0317":1,"0210":1,"0115":1,"1209":1,"1030":1};
var aR="ALL";
var dpC=null;
var dbt=null;

function gV(ver,dp){
  if(aR==="ALL")return RSEGS.reduce(function(s,r,i){return s+D.rev[ver][dp][i];},0);
  var i=RSEGS.indexOf(aR);return i>=0?D.rev[ver][dp][i]:0;
}
function gP(ver,dp){
  if(aR==="ALL")return RSEGS.reduce(function(s,r,i){return s+D.pu[ver][dp][i];},0);
  var i=RSEGS.indexOf(aR);return i>=0?D.pu[ver][dp][i]:0;
}
function fw(v){return (v/10000).toFixed(1)+"万";}

function rClick(b){
  aR=b.dataset.r;
  document.querySelectorAll(".dp-rbtn").forEach(function(x){
    var on=x.dataset.r===aR;
    x.style.background=on?"#37474f":"#f5f5f5";
    x.style.color=on?"#fff":"#333";
    x.style.borderColor=on?"#37474f":"#bbb";
  });
  upAll();
}

function vClick(e,b){
  if(dbt)return;
  dbt=setTimeout(function(){
    dbt=null;
    var v=b.dataset.ver;aV[v]=aV[v]?0:1;
    sBtn(b,aV[v]);upAll();
  },220);
}
function vDbl(b){
  if(dbt){clearTimeout(dbt);dbt=null;}
  var v=b.dataset.ver;
  Object.keys(aV).forEach(function(k){aV[k]=0;});aV[v]=1;
  document.querySelectorAll(".dp-vbtn").forEach(function(x){sBtn(x,x.dataset.ver===v?1:0);});
  upAll();
}
var VCOLS={"0317":"#e53935","0210":"#1976d2","0115":"#43a047","1209":"#757575","1030":"#795548"};
function sBtn(b,on){
  var c=VCOLS[b.dataset.ver];
  b.style.background=on?c:"#f5f5f5";b.style.color=on?"#fff":c;b.style.borderColor=c;
}

function upChart(){
  var vers=D.vers.filter(function(v){return aV[v];});
  var dps=DORDER.filter(function(d){return d!=="DP9";});
  var series=vers.map(function(ver){
    return {name:D.verNames[ver],type:"bar",barMaxWidth:14,
      itemStyle:{color:D.verColors[ver]},
      data:dps.map(function(dp){return +(gV(ver,dp)/10000).toFixed(2);}),
      label:ver==="0317"?{show:true,position:"top",fontSize:9,
        formatter:function(p){return p.value>0?p.value+"":"";}
      }:{show:false}};
  });
  var opt={
    tooltip:{trigger:"axis",
      formatter:function(ps){
        var dp=dps[ps[0].dataIndex];
        var rl=aR==="ALL"?"全部":aR+"元";
        var s=ps[0].axisValue+"&nbsp;<span style='color:#888;font-size:10px'>"+DTYPE[dp]+"</span><br>";
        s+="<span style='color:#aaa;font-size:9px'>分R："+rl+"</span><br>";
        ps.forEach(function(p){
          var v=D.vers.find(function(x){return D.verNames[x]===p.seriesName;});
          var pu=gP(v,dp),ar=pu>0?Math.round(gV(v,dp)/pu):0;
          s+=p.marker+p.seriesName+": "+p.value+"万";
          if(pu>0)s+=" | "+pu+"人 | ARPPU ¥"+ar;
          s+="<br>";
        });
        var it=D.dpContent[dp]["0317"];if(it)s+="<span style='color:#888;font-size:9px'>0317投放："+it+"</span>";
        return s;
      }
    },
    legend:{data:vers.map(function(v){return D.verNames[v];}),bottom:0,textStyle:{fontSize:10}},
    grid:{top:10,bottom:50,left:36,right:10},
    xAxis:{type:"category",data:dps,axisLabel:{fontSize:10}},
    yAxis:{type:"value",name:"万元",nameTextStyle:{fontSize:9},axisLabel:{fontSize:9},splitLine:{lineStyle:{type:"dashed"}}},
    series:series
  };
  if(!dpC)dpC=echarts.init(document.getElementById("chart-dp-r"));
  dpC.setOption(opt,true);
}

function upTable(){
  var dps=DORDER.filter(function(d){return d!=="DP9";});
  var html="";
  dps.forEach(function(dp){
    var v0=gV("0317",dp),v1=gV("0210",dp);
    var pct=v1>0?((v0-v1)/v1*100):0;
    var ps=v1>0?(pct>=0?"+":"")+pct.toFixed(1)+"%":"-";
    var pc=pct>=0?"#2e7d32":"#c62828";
    var ct=D.dpContent[dp]["0317"]||"-";
    html+="<tr><td><strong>"+dp+"</strong></td><td style='color:#555'>"+DTYPE[dp]+"</td><td style='color:#666;font-size:10px'>"+ct+"</td>";
    ["0317","0210","0115","1209","1030"].forEach(function(v){
      var b=v==="0317"?"font-weight:600;":"";
      var disp=aV[v]?"":"display:none;";
      html+="<td class='tr' style='"+b+disp+"'>"+fw(gV(v,dp))+"</td>";
    });
    html+="<td class='tr' style='color:"+pc+"'>"+ps+"</td></tr>";
  });
  document.getElementById("dp-tbody").innerHTML=html;
}

var INS={
  "ALL":"📌 <strong>DP10（+63%）+ DP8（+14%）是0317核心增长点</strong>，兀鹰强度驱动大R集中于DP10/DP8；DP12（竞速兀鹰）49.3万接近0210钢铁泰特（52.3万），限量定位成功。DP11拖累最大（-85%）：无新泰坦，下版本若上新泰坦预计可恢复30-40万量级。",
  "20000+":"📌 <strong>2万元+大R：DP12绝对主导</strong>，0317大R 43.9万全部集中在限量版；DP10（8.6万）第二，强度驱动大R追求整机。DP11大R从0210的26.5万跌至0317的3.1万——无新泰坦是大R流失最核心原因，大R对泰坦新内容极度敏感。",
  "5000-20000":"📌 <strong>5000-2万元中大R：DP12+DP10双驱动</strong>，该段对限量版和本期机甲池消费最积极；DP11中大R下滑显著，说明中大R对新泰坦投放高度敏感，建议新泰坦周期不超过3个版本。",
  "1000-5000":"📌 <strong>1000-5000元中R：DP10是最大驱动力</strong>，兀鹰吸引中R优先购买本期纯净机甲；DP1-DP3老混池在该段依然有稳定基本盘，中R同时补齐新机甲和旧内容，消费行为多样。",
  "100-1000":"📌 <strong>100-1000元小R：各池均衡分布</strong>，无明显单池集中，说明小R消费随机性强；DP12在该段几乎为零——限量版价格门槛有效将小R隔离，定价策略合理。",
  "0-100":"📌 <strong>0-100元超低消费：DP1老机甲混池为主</strong>，以试探性消费为主；DP10/DP12在该段贡献极低，该段主要价值在培养付费习惯，不应作为内容设计重点目标受众。"
};

function upInsight(){
  document.getElementById("dp-insight").innerHTML=INS[aR]||INS["ALL"];
  document.getElementById("dp-r-lbl").textContent=aR==="ALL"?"":"↑ 当前："+aR+"元视角";
}

function upAll(){upChart();upTable();upInsight();}

document.querySelectorAll(".dp-rbtn").forEach(function(b){b.addEventListener("click",function(){rClick(b);});});
document.querySelectorAll(".dp-vbtn").forEach(function(b){
  b.addEventListener("click",function(e){vClick(e,b);});
  b.addEventListener("dblclick",function(){vDbl(b);});
});

window.addEventListener("load",function(){upAll();});
window.addEventListener("resize",function(){if(dpC)dpC.resize();});
})();
</script>

"""
js = js.replace("__PAYLOAD__", payload)
parts.append(js)

new_section = "".join(parts)

new_content = content[:dp_card_start] + new_section + content[dp_card_end:]

with open(r'C:\Users\leo1.chen\Desktop\机甲战队_0317版本首周报告.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"Done! {len(new_section)} chars injected")
