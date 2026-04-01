from pathlib import Path

p = Path(r'C:\Users\leo1.chen\Desktop\机甲战队_0317版本首周报告.html')
text = p.read_text(encoding='utf-8')

def rep(old, new, label):
    cnt = text.count(old)
    print(f'{label}: {cnt} occurrences')
    return text.replace(old, new, 1) if cnt > 0 else text

# chart-wau legend
text = rep(
    "legend:{data:['1209 雷克斯+拳击手','0115 探路者','1030 杜克斯','0210 泰特（春节）','0317 兀鹰'],bottom:0,textStyle:{fontSize:10}},",
    "legend:{data:['1030 杜克斯','1209 雷克斯+拳击手','0115 探路者','0210 泰特（春节）','0317 兀鹰'],bottom:0,textStyle:{fontSize:10}},",
    'chart-wau legend'
)

# chart-wau series (w vars)
text = rep(
    "{name:'1209 雷克斯+拳击手',type:'bar',data:w1209,barMaxWidth:12,itemStyle:{color:'#bdbdbd'}},\n      {name:'0115 探路者',type:'bar',data:w0115,barMaxWidth:12,itemStyle:{color:'#a5d6a7'}},\n      {name:'1030 杜克斯',type:'bar',data:w1030,barMaxWidth:12,itemStyle:{color:'#795548'}},\n      {name:'0210 泰特（春节）',type:'bar',data:w0210,barMaxWidth:12,itemStyle:{color:'#90caf9'}},",
    "{name:'1030 杜克斯',type:'bar',data:w1030,barMaxWidth:12,itemStyle:{color:'#795548'}},\n      {name:'1209 雷克斯+拳击手',type:'bar',data:w1209,barMaxWidth:12,itemStyle:{color:'#bdbdbd'}},\n      {name:'0115 探路者',type:'bar',data:w0115,barMaxWidth:12,itemStyle:{color:'#a5d6a7'}},\n      {name:'0210 泰特（春节）',type:'bar',data:w0210,barMaxWidth:12,itemStyle:{color:'#90caf9'}},",
    'chart-wau series'
)

# chart-active legend (0317 first)
text = rep(
    "legend:{data:['0317 兀鹰','0210 泰特（春节）','0115 探路者','1030 杜克斯','1209 雷克斯+拳击手'],bottom:0,textStyle:{fontSize:10}},",
    "legend:{data:['1030 杜克斯','1209 雷克斯+拳击手','0115 探路者','0210 泰特（春节）','0317 兀鹰'],bottom:0,textStyle:{fontSize:10}},",
    'chart-active/r/dp/dp-arppu legends (first pass)'
)
# Same pattern appears in chart-r, chart-dp, chart-dp-arppu - replace all remaining
remaining = text.count("legend:{data:['0317 兀鹰','0210 泰特（春节）','0115 探路者','1030 杜克斯','1209 雷克斯+拳击手'],bottom:0,textStyle:{fontSize:10}},")
print(f'remaining same legend pattern: {remaining}')
text = text.replace(
    "legend:{data:['0317 兀鹰','0210 泰特（春节）','0115 探路者','1030 杜克斯','1209 雷克斯+拳击手'],bottom:0,textStyle:{fontSize:10}},",
    "legend:{data:['1030 杜克斯','1209 雷克斯+拳击手','0115 探路者','0210 泰特（春节）','0317 兀鹰'],bottom:0,textStyle:{fontSize:10}},"
)

# chart-active series (a0317 -> a1030 first, a vars)
old_act = ("{name:'0317 兀鹰',type:'bar',data:a0317,barMaxWidth:12,itemStyle:{color:'#e53935'},\n"
           "        label:{show:true,position:'right',fontSize:9,formatter:function(p){return p.value.toLocaleString()}}},\n"
           "      {name:'0210 泰特（春节）',type:'bar',data:a0210,barMaxWidth:12,itemStyle:{color:'#90caf9'}},\n"
           "      {name:'0115 探路者',type:'bar',data:a0115,barMaxWidth:12,itemStyle:{color:'#a5d6a7'}},\n"
           "      {name:'1030 杜克斯',type:'bar',data:a1030,barMaxWidth:12,itemStyle:{color:'#795548'}},\n"
           "      {name:'1209 雷克斯+拳击手',type:'bar',data:a1209,barMaxWidth:12,itemStyle:{color:'#bdbdbd'}}")
new_act = ("{name:'1030 杜克斯',type:'bar',data:a1030,barMaxWidth:12,itemStyle:{color:'#795548'}},\n"
           "      {name:'1209 雷克斯+拳击手',type:'bar',data:a1209,barMaxWidth:12,itemStyle:{color:'#bdbdbd'}},\n"
           "      {name:'0115 探路者',type:'bar',data:a0115,barMaxWidth:12,itemStyle:{color:'#a5d6a7'}},\n"
           "      {name:'0210 泰特（春节）',type:'bar',data:a0210,barMaxWidth:12,itemStyle:{color:'#90caf9'}},\n"
           "      {name:'0317 兀鹰',type:'bar',data:a0317,barMaxWidth:12,itemStyle:{color:'#e53935'},\n"
           "        label:{show:true,position:'right',fontSize:9,formatter:function(p){return p.value.toLocaleString()}}}")
text = rep(old_act, new_act, 'chart-active series')

# chart-r series
old_r = ("{name:'0317 兀鹰',type:'bar',data:r0317,barMaxWidth:12,itemStyle:{color:'#e53935'},\n"
         "        label:{show:true,position:'right',fontSize:9,formatter:'{c}万'}},\n"
         "      {name:'0210 泰特（春节）',type:'bar',data:r0210,barMaxWidth:12,itemStyle:{color:'#90caf9'}},\n"
         "      {name:'0115 探路者',type:'bar',data:r0115,barMaxWidth:12,itemStyle:{color:'#a5d6a7'}},\n"
         "      {name:'1030 杜克斯',type:'bar',data:r1030,barMaxWidth:12,itemStyle:{color:'#795548'}},\n"
         "      {name:'1209 雷克斯+拳击手',type:'bar',data:r1209,barMaxWidth:12,itemStyle:{color:'#bdbdbd'}}")
new_r = ("{name:'1030 杜克斯',type:'bar',data:r1030,barMaxWidth:12,itemStyle:{color:'#795548'}},\n"
         "      {name:'1209 雷克斯+拳击手',type:'bar',data:r1209,barMaxWidth:12,itemStyle:{color:'#bdbdbd'}},\n"
         "      {name:'0115 探路者',type:'bar',data:r0115,barMaxWidth:12,itemStyle:{color:'#a5d6a7'}},\n"
         "      {name:'0210 泰特（春节）',type:'bar',data:r0210,barMaxWidth:12,itemStyle:{color:'#90caf9'}},\n"
         "      {name:'0317 兀鹰',type:'bar',data:r0317,barMaxWidth:12,itemStyle:{color:'#e53935'},\n"
         "        label:{show:true,position:'right',fontSize:9,formatter:'{c}万'}}")
text = rep(old_r, new_r, 'chart-r series')

# chart-dp series
old_dp = ("{name:'0317 兀鹰',type:'bar',data:d0317,barMaxWidth:12,itemStyle:{color:'#e53935'},\n"
          "        label:{show:true,position:'top',fontSize:8,formatter:'{c}'}},\n"
          "      {name:'0210 泰特（春节）',type:'bar',data:d0210,barMaxWidth:12,itemStyle:{color:'#90caf9'}},\n"
          "      {name:'0115 探路者',type:'bar',data:d0115,barMaxWidth:12,itemStyle:{color:'#a5d6a7'}},\n"
          "      {name:'1030 杜克斯',type:'bar',data:d1030,barMaxWidth:12,itemStyle:{color:'#795548'}},\n"
          "      {name:'1209 雷克斯+拳击手',type:'bar',data:d1209,barMaxWidth:12,itemStyle:{color:'#bdbdbd'}}")
new_dp = ("{name:'1030 杜克斯',type:'bar',data:d1030,barMaxWidth:12,itemStyle:{color:'#795548'}},\n"
          "      {name:'1209 雷克斯+拳击手',type:'bar',data:d1209,barMaxWidth:12,itemStyle:{color:'#bdbdbd'}},\n"
          "      {name:'0115 探路者',type:'bar',data:d0115,barMaxWidth:12,itemStyle:{color:'#a5d6a7'}},\n"
          "      {name:'0210 泰特（春节）',type:'bar',data:d0210,barMaxWidth:12,itemStyle:{color:'#90caf9'}},\n"
          "      {name:'0317 兀鹰',type:'bar',data:d0317,barMaxWidth:12,itemStyle:{color:'#e53935'},\n"
          "        label:{show:true,position:'top',fontSize:8,formatter:'{c}'}}")
text = rep(old_dp, new_dp, 'chart-dp series')

# chart-dp-arppu series (a0317 15px version)
old_dpa = ("{name:'0317 兀鹰',type:'bar',data:a0317,barMaxWidth:15,itemStyle:{color:'#e53935'},\n"
           "        label:{show:true,position:'top',fontSize:9,formatter:'{c}'}},\n"
           "      {name:'0210 泰特（春节）',type:'bar',data:a0210,barMaxWidth:15,itemStyle:{color:'#90caf9'}},\n"
           "      {name:'0115 探路者',type:'bar',data:a0115,barMaxWidth:15,itemStyle:{color:'#a5d6a7'}},\n"
           "      {name:'1030 杜克斯',type:'bar',data:a1030,barMaxWidth:15,itemStyle:{color:'#795548'}},\n"
           "      {name:'1209 雷克斯+拳击手',type:'bar',data:a1209,barMaxWidth:15,itemStyle:{color:'#bdbdbd'}}")
new_dpa = ("{name:'1030 杜克斯',type:'bar',data:a1030,barMaxWidth:15,itemStyle:{color:'#795548'}},\n"
           "      {name:'1209 雷克斯+拳击手',type:'bar',data:a1209,barMaxWidth:15,itemStyle:{color:'#bdbdbd'}},\n"
           "      {name:'0115 探路者',type:'bar',data:a0115,barMaxWidth:15,itemStyle:{color:'#a5d6a7'}},\n"
           "      {name:'0210 泰特（春节）',type:'bar',data:a0210,barMaxWidth:15,itemStyle:{color:'#90caf9'}},\n"
           "      {name:'0317 兀鹰',type:'bar',data:a0317,barMaxWidth:15,itemStyle:{color:'#e53935'},\n"
           "        label:{show:true,position:'top',fontSize:9,formatter:'{c}'}}")
text = rep(old_dpa, new_dpa, 'chart-dp-arppu series')

p.write_text(text, encoding='utf-8')
print('ALL DONE. Saved.')
