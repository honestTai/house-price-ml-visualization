# -*- coding: utf-8 -*-
import json
from urllib.parse import quote
import requests
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def getlnglat(address):
    """
    获取一个中文地址的经纬度(lat:纬度值,lng:经度值)
    """
    url_base = "http://api.map.baidu.com/geocoding/v3/"
    output = "json"
    ak = "XhQieNzd54cmS5dEPL8cenDWeFTtCDqm" # 浏览器端密钥
    # address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
    url = url_base + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak
    lat = 0.0
    lng = 0.0
    res = requests.get(url)
    temp = json.loads(res.text)
    if temp["status"] == 0:
        lat = temp['result']['location']['lat']
        lng = temp['result']['location']['lng']
    return lat,lng

def main():
    """主函数"""
    #定义加载数据的文件名
    filename = "ershoufang-clean-utf8-v1.1.csv"
    #自定义数据的行列索引（行索引使用pd默认的，列索引使用自定义的）
    names = [
            "id","communityName","areaName","total","unitPriceValue",
            "fwhx","szlc","jzmj","hxjg","tnmj",
            "jzlx","fwcx","jzjg","zxqk","thbl",
            "pbdt","cqnx","gpsj","jyqs","scjy",
            "fwyt","fwnx","cqss","dyxx","fbbj",
            ]
    #自定义需要处理的缺失值标记列表
    miss_value = ["null","暂无数据"]
    #数据类型会自动转换
    #使用自定义的列名，跳过文件中的头行，处理缺失值列表标记的缺失值
    df = pd.read_csv(filename,skiprows=[0],names=names,na_values=miss_value)

    # """2、生成经纬度信息"""
    # idint = []
    # names = []
    # lats = []
    # lngs = []
    # lat_lng_data = {"id":idint,"communityName":names,"lat":lats,"lng":lngs}
    #
    # for idi,name in zip(list(df["id"]),list(df["communityName"])):
    #     name = str(name)
    #     lat,lng = getlnglat("北京市"+name)
    #     if lat != 0 or lng !=0:
    #         idint.append(idi)
    #         names.append(name)
    #         lats.append(lat)
    #         lngs.append(lng)
    #         print(idi)
    #
    # frame_test = pd.DataFrame(lat_lng_data)
    # frame_test.to_csv("latlng.csv")

    """3、合并数据，并按格式输出数据"""
    #合并数据
    df_latlng = pd.read_csv("latlng.csv",skiprows=[0],names=["id","communityName","lat","lng"])
    # del df_latlng["did"]
    del df_latlng["communityName"]
    df_latlng['id'] = df_latlng['id'].astype(str)
    df['id'] = df['id'].astype(str)
    # df_merge = pd.merge(df, df_latlng, on="id")
    df_merge = pd.merge(df,df_latlng,on="id")

    #小于400万
    xiaoyu = df_merge[df_merge["total"]<401]
    xiaoyu2 = df_merge.loc[df_merge["total"]<401]
    xiaoyu2 = xiaoyu2.loc[xiaoyu2["jzmj"] < 80]

    """4、生成需要的格式文件"""
    out_map = "xiaoyu401.js"
    with open(out_map,"w") as file_out:
        for lng,lat,price in zip(list(xiaoyu2["lng"]),list(xiaoyu2["lat"]),list(xiaoyu2["total"])):
            out = '{\"lng\":' + str(lng) + ',\"lat\":' + str(lat) + ',\"count\":' + str(price) + '},'
            file_out.write(out)
            file_out.write("\n")
    out_maps = "total.js"
    with open(out_maps, "w") as file_out:
        for lng, lat, price in zip(list(df_merge["lng"]), list(df_merge["lat"]), list(df_merge["total"])):
            out = '{\"lng\":' + str(lng) + ',\"lat\":' + str(lat) + ',\"count\":' + str(price) + '},'
            file_out.write(out)
            file_out.write("\n")

if __name__ == "__main__":
    main()
