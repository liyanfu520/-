# -
用爬虫和echarts工具实现疫情地图的显示，地图包括全国地图和分省地图

1、安装pyecharts以及相关的包
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  pyecharts==1.7.1

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  echarts-countries-pypkg

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  echarts-china-provinces-pypkg

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  echarts-china-cities-pypkg

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  echarts-china-counties-pypkg

pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple echarts-china-misc-pypkg

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  echarts-united-kingdom-pypkg


2、如果顺利的话，程序可以直接运行成功，运行结果包括全国疫情地图和分省疫情地图

3、当然，因为echarts底图的省市级名称和爬取的省市名称有些不一致，导致分省疫情地图某些市的数据没法正常显示


