from pathlib import Path

p = Path(r'C:\Users\leo1.chen\Desktop\机甲战队_0317版本首周报告.html')
text = p.read_text(encoding='utf-8')

# ===== 1. Version overview boxes: reorder to 0317->0210->0115->1209->1030 =====
old_vergrid = '''    <div class="ver-box cur">
      <div class="ver-box-lbl">🎯 0317 兀鹰（本期）</div>
      <div class="ver-content">
        <span class="vc mech">兀鹰</span><span class="vc sp">竞速兀鹰 ★限量</span>
        <span class="vc weapon">咆哮者</span><span class="vc weapon">低吼者</span><span class="vc weapon">呼啸者</span>
      </div>
      <div style="font-size:10px;color:#999">无新泰坦 · DP11复刻旧泰坦</div>
    </div>
    <div class="ver-box">
      <div class="ver-box-lbl" style="color:#1565c0">0210 泰特（春节版）</div>
      <div class="ver-content">
        <span class="vc mech">泰特</span><span class="vc sp">钢铁泰特 ★限量</span>
        <span class="vc weapon">双冠</span><span class="vc weapon">红冠</span><span class="vc weapon">白冠</span>
        <span class="vc titan">神枪手</span><span class="vc weapon">报复者</span>
      </div>
      <div style="font-size:10px;color:#999">春节假期加成</div>
    </div>
    <div class="ver-box">
      <div class="ver-box-lbl" style="color:#555">0115 探路者</div>
      <div class="ver-content">
        <span class="vc mech">探路者</span>
        <span class="vc weapon">约顿</span><span class="vc weapon">奇永</span><span class="vc weapon">莫拉纳</span>
      </div>
      <div style="font-size:10px;color:#999">辅助型机甲 · 无新泰坦</div>
    </div>
    <div class="ver-box">
      <div class="ver-box-lbl" style="color:#555">1030 杜克斯</div>
      <div class="ver-content">
        <span class="vc mech">杜克斯</span>
        <span class="vc weapon">戒律</span><span class="vc weapon">重击</span>
      </div>
      <div style="font-size:10px;color:#999">输出型机甲 · 无新泰坦</div>
    </div>
    <div class="ver-box">
      <div class="ver-box-lbl" style="color:#555">1209 雷克斯+拳击手</div>
      <div class="ver-content">
        <span class="vc mech">雷克斯</span><span class="vc sp">烈焰雷克斯 ★限量</span>
        <span class="vc weapon">埃洛克斯</span><span class="vc weapon">穆瑞克斯</span>
        <span class="vc titan">拳击手</span><span class="vc weapon">悲恸者</span><span class="vc weapon">毁灭者</span>
      </div>
    </div>'''

new_vergrid = '''    <div class="ver-box cur">
      <div class="ver-box-lbl">🎯 0317 兀鹰（本期）</div>
      <div class="ver-content">
        <span class="vc mech">兀鹰</span><span class="vc sp">竞速兀鹰 ★限量</span>
        <span class="vc weapon">咆哮者</span><span class="vc weapon">低吼者</span><span class="vc weapon">呼啸者</span>
      </div>
      <div style="font-size:10px;color:#999">无新泰坦 · DP11复刻旧泰坦</div>
    </div>
    <div class="ver-box">
      <div class="ver-box-lbl" style="color:#1565c0">0210 泰特（春节版）</div>
      <div class="ver-content">
        <span class="vc mech">泰特</span><span class="vc sp">钢铁泰特 ★限量</span>
        <span class="vc weapon">双冠</span><span class="vc weapon">红冠</span><span class="vc weapon">白冠</span>
        <span class="vc titan">神枪手</span><span class="vc weapon">报复者</span>
      </div>
      <div style="font-size:10px;color:#999">春节假期加成</div>
    </div>
    <div class="ver-box">
      <div class="ver-box-lbl" style="color:#555">0115 探路者</div>
      <div class="ver-content">
        <span class="vc mech">探路者</span>
        <span class="vc weapon">约顿</span><span class="vc weapon">奇永</span><span class="vc weapon">莫拉纳</span>
      </div>
      <div style="font-size:10px;color:#999">辅助型机甲 · 无新泰坦</div>
    </div>
    <div class="ver-box">
      <div class="ver-box-lbl" style="color:#555">1209 雷克斯+拳击手</div>
      <div class="ver-content">
        <span class="vc mech">雷克斯</span><span class="vc sp">烈焰雷克斯 ★限量</span>
        <span class="vc weapon">埃洛克斯</span><span class="vc weapon">穆瑞克斯</span>
        <span class="vc titan">拳击手</span><span class="vc weapon">悲恸者</span><span class="vc weapon">毁灭者</span>
      </div>
    </div>
    <div class="ver-box">
      <div class="ver-box-lbl" style="color:#555">1030 杜克斯</div>
      <div class="ver-content">
        <span class="vc mech">杜克斯</span>
        <span class="vc weapon">戒律</span><span class="vc weapon">重击</span>
      </div>
      <div style="font-size:10px;color:#999">输出型机甲 · 无新泰坦</div>
    </div>'''

cnt = text.count(old_vergrid)
print('ver-grid found:', cnt)
if cnt:
    text = text.replace(old_vergrid, new_vergrid, 1)

# ===== 2. KPI comparison cards: reorder to 0317->0210->0115->1209->1030 =====
old_kpi = ('    <div class="vcc cur"><div class="vcc-ver">0317 兀鹰（本期）</div><div class="vcc-amt">431.9万</div><div class="vcc-sub">WAU 18.5万 · DAU 8.6万</div></div>\n'
           '    <div class="vcc"><div class="vcc-ver">0210 泰特+神枪手（春节）</div><div class="vcc-amt">530.7万</div><div class="vcc-sub">WAU 23.0万 · DAU 9.9万</div></div>\n'
           '    <div class="vcc"><div class="vcc-ver">0115 探路者</div><div class="vcc-amt">337.1万</div><div class="vcc-sub">WAU 17.7万 · DAU 7.7万</div></div>\n'
           '    <div class="vcc"><div class="vcc-ver">1030 杜克斯</div><div class="vcc-amt">406.1万</div><div class="vcc-sub">WAU 16.2万 · DAU 6.2万</div></div>\n'
           '    <div class="vcc"><div class="vcc-ver">1209 雷克斯+拳击手</div><div class="vcc-amt">446.5万</div><div class="vcc-sub">WAU 16.4万 · DAU 6.4万</div></div>')

new_kpi = ('    <div class="vcc cur"><div class="vcc-ver">0317 兀鹰（本期）</div><div class="vcc-amt">431.9万</div><div class="vcc-sub">WAU 18.5万 · DAU 8.6万</div></div>\n'
           '    <div class="vcc"><div class="vcc-ver">0210 泰特+神枪手（春节）</div><div class="vcc-amt">530.7万</div><div class="vcc-sub">WAU 23.0万 · DAU 9.9万</div></div>\n'
           '    <div class="vcc"><div class="vcc-ver">0115 探路者</div><div class="vcc-amt">337.1万</div><div class="vcc-sub">WAU 17.7万 · DAU 7.7万</div></div>\n'
           '    <div class="vcc"><div class="vcc-ver">1209 雷克斯+拳击手</div><div class="vcc-amt">446.5万</div><div class="vcc-sub">WAU 16.4万 · DAU 6.4万</div></div>\n'
           '    <div class="vcc"><div class="vcc-ver">1030 杜克斯</div><div class="vcc-amt">406.1万</div><div class="vcc-sub">WAU 16.2万 · DAU 6.2万</div></div>')

cnt2 = text.count(old_kpi)
print('kpi cards found:', cnt2)
if cnt2:
    text = text.replace(old_kpi, new_kpi, 1)

# ===== 3. chart-rev4 and chart-dau4 legends: newest->oldest =====
# Currently: ['1030 杜克斯','1209 雷克斯+拳击手','0115 探路者','0210 泰特（春节）','0317 兀鹰']
old_rev_legend = "legend:{data:['1030 杜克斯','1209 雷克斯+拳击手','0115 探路者','0210 泰特（春节）','0317 兀鹰'],bottom:0,textStyle:{fontSize:10}},"
new_rev_legend = "legend:{data:['0317 兀鹰','0210 泰特（春节）','0115 探路者','1209 雷克斯+拳击手','1030 杜克斯'],bottom:0,textStyle:{fontSize:10}},"
cnt3 = text.count(old_rev_legend)
print('rev/dau legend found:', cnt3)
text = text.replace(old_rev_legend, new_rev_legend)  # replace all (rev4 + dau4)

p.write_text(text, encoding='utf-8')
print('Saved.')
