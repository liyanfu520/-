import requests
import json
from parse import parse_url
import time
from pyecharts.charts import Map
from pyecharts import options as opts 
import requests
import json
global data_json
#抓起数据
def get_virus_data():
    virus_confirm_dict={}
    virus_nowconfirm_dict={}
    dataurl="https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    # data = json.loads(requests.get(url=url).json()['data'])
    response_data=requests.get(dataurl,timeout=5).json()["data"]
    data_json=json.loads(response_data)
    china_data_list=data_json["areaTree"][0]["children"]
    for province_data in china_data_list:
        virus_confirm_dict[province_data["name"]]=province_data["total"]["confirm"]
        virus_nowconfirm_dict[province_data["name"]]=province_data["total"]["nowConfirm"]
    # print(virus_confirm_dict)
    return data_json,virus_confirm_dict,virus_nowconfirm_dict,china_data_list

#累计确诊
def confirm_map(data_json,virus_confirm_dict):
    map = Map(init_opts=opts.InitOpts(width="1900px", height="900px"))
    map.set_global_opts(
    title_opts=opts.TitleOpts(title="实时疫情地图 %s\n\n累计确诊 %d\n现有确诊 %d\n现有疑似 %d\n输入病例 %d\n累计治愈 %d\n累计死亡 %d" \
                            %(data_json['lastUpdateTime'],data_json['chinaTotal']['confirm'],data_json['chinaTotal']['nowConfirm'], \
                                data_json['chinaTotal']['suspect'],data_json['chinaTotal']['importedCase'], \
                                data_json['chinaTotal']['heal'],data_json['chinaTotal']['dead'])),
    visualmap_opts=opts.VisualMapOpts(max_=3600, is_piecewise=True,
            pieces=[
            {"max": 1999999, "min": 10000, "label": "10000人及以上", "color": "#8A0808"},
            {"max": 9999, "min": 1000, "label": "1000-9999人", "color": "#B40404"},
            {"max": 999, "min": 500, "label": "500-999人", "color": "#DF0101"},
            {"max": 499, "min": 100, "label": "100-499人", "color": "#F78181"},
            {"max": 99, "min": 10, "label": "10-99人", "color": "#F5A9A9"},
            {"max": 9, "min": 0, "label": "1-9人", "color": "#FFFFCC"},
            ], ) #最大数据范围，分段
    )
    virus_confirm = list(virus_confirm_dict.items())
    # {names[i]:v[i] for i in range(len(names))}
    map.add("累计确诊", data_pair=virus_confirm, maptype="china", is_roam=True)
    map.render('html\全国实时累计确诊疫情地图.html')

#现有确诊
def nowconfirm_map(data_json,virus_nowconfirm_dict):
    map = Map(init_opts=opts.InitOpts(width="1900px", height="900px"))
    map.set_global_opts(
    title_opts=opts.TitleOpts(title="实时疫情地图 %s\n\n累计确诊 %d\n现有确诊 %d\n现有疑似 %d\n输入病例 %d\n累计治愈 %d\n累计死亡 %d" \
                            %(data_json['lastUpdateTime'],data_json['chinaTotal']['confirm'],data_json['chinaTotal']['nowConfirm'], \
                                data_json['chinaTotal']['suspect'],data_json['chinaTotal']['importedCase'], \
                                data_json['chinaTotal']['heal'],data_json['chinaTotal']['dead'])),
    visualmap_opts=opts.VisualMapOpts(max_=3600, is_piecewise=True,
            pieces=[
            {"max": 1999999, "min": 1000, "label": "10000人及以上", "color": "#8A0808"},
            {"max": 999, "min": 200, "label": "200-999人", "color": "#B40404"},
            {"max": 199, "min": 50, "label": "50-199人", "color": "#DF0101"},
            {"max": 49, "min": 30, "label": "30-49人", "color": "#F78181"},
            {"max": 29, "min": 10, "label": "10-29人", "color": "#F5A9A9"},
            {"max": 9, "min": 0, "label": "1-9人", "color": "#FFFFCC"},
            ], ) #最大数据范围，分段
    )
    virus_nowconfirm = list(virus_nowconfirm_dict.items())
    # {names[i]:v[i] for i in range(len(names))}
    map.add("现有确诊", data_pair=virus_nowconfirm, maptype="china", is_roam=True)
    map.render('html\全国实时现有确诊疫情地图.html')

#分省现有确诊数据
def get_areavirus_data(china_datas):
    virus_areaconfirm_dict={}
    virus_areanowconfirm_dict={}
    # areadata_json={}
    for china_data in china_datas:
        # areadata_json[china_data["name"]]=china_data["total"]["nowConfirm"]   #现有确诊数

        virus_areanowconfirm_dict={}
        for children_data in china_data['children']:
            if china_data["name"]=='北京' or china_data["name"]=='香港'or china_data["name"]=='上海' or china_data["name"]=='澳门' \
                or china_data["name"]=='重庆' :
                virus_areanowconfirm_dict[children_data["name"]+'区']=children_data["total"]["nowConfirm"]
            else:
                virus_areanowconfirm_dict[children_data["name"]+'市']=children_data["total"]["nowConfirm"]
            
            virus_areaconfirm_dict[children_data["name"]+'市']=children_data["total"]["confirm"]
        
        #分省现有确诊地图
        areanowconfirm_map(china_data,virus_areanowconfirm_dict)
    return china_data,virus_areaconfirm_dict,virus_areanowconfirm_dict

#分省现有确诊地图
def areanowconfirm_map(china_data,virus_areanowconfirm_dict):
    map = Map(init_opts=opts.InitOpts(width="1900px", height="900px"))
    map.set_global_opts(
    title_opts=opts.TitleOpts(title="实时疫情地图 %s\n\n累计确诊 %d\n现有确诊 %d\n现有疑似 %d\n累计治愈 %d\n累计死亡 %d" \
                            %(data_json['lastUpdateTime'],china_data['total']['confirm'],china_data['total']['nowConfirm'], \
                                china_data['total']['suspect'], \
                                china_data['total']['heal'],china_data['total']['dead'])),
    visualmap_opts=opts.VisualMapOpts(max_=3600, is_piecewise=True,
            pieces=[
            {"max": 1999999, "min": 1000, "label": "10000人及以上", "color": "#8A0808"},
            {"max": 999, "min": 200, "label": "200-999人", "color": "#B40404"},
            {"max": 199, "min": 50, "label": "50-199人", "color": "#DF0101"},
            {"max": 49, "min": 30, "label": "30-49人", "color": "#F78181"},
            {"max": 29, "min": 10, "label": "10-29人", "color": "#F5A9A9"},
            {"max": 9, "min": 0, "label": "1-9人", "color": "#FFFFCC"},
            ], ) #最大数据范围，分段
    )

    virus_nowconfirm = list(virus_areanowconfirm_dict.items())
    # {names[i]:v[i] for i in range(len(names))}
    map.add("现有确诊", data_pair=virus_nowconfirm, maptype=china_data['name'], is_roam=True)
    map.render('html\{}.html'.format(china_data['name']))

def catch_daily():
    """抓取每日确诊和死亡数据"""
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_cn_day_counts&callback=&_=%d'%int(time.time()*1000)
    data = json.loads(requests.get(url=url).json()['data'])
    data.sort(key=lambda x:x['date'])
    
    date_list = list() # 日期
    confirm_list = list() # 确诊
    suspect_list = list() # 疑似
    dead_list = list() # 死亡
    heal_list = list() # 治愈
    for item in data:
        month, day = item['date'].split('.')
        date_list.append(datetime.strptime('2020-%s-%s'%(month, day), '%Y-%m-%d'))
        confirm_list.append(int(item['confirm']))
        suspect_list.append(int(item['suspect']))
        dead_list.append(int(item['dead']))
        heal_list.append(int(item['heal']))
    
    return date_list, confirm_list, suspect_list, dead_list, heal_list

if __name__ == "__main__":
    data_json,virus_confirm_dict,virus_nowconfirm_dict,china_datas=get_virus_data()
    
    #累计确诊
    confirm_map(data_json,virus_confirm_dict)
    #现有确诊
    nowconfirm_map(data_json,virus_nowconfirm_dict)

    #分省现有确诊地图
    get_areavirus_data(china_datas)

