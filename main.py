'''
UI界面部署，调用模型相关函数在mask中
'''
from mask import mark_test

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def user():
    return render_template('index.html')

@app.route('/addUser', methods=['POST'])
def login():
    data = request.json
    # print('recv:', json)
    #测试店铺链接
   #https://h5.ele.me/2021001185671035/pages/ele-takeout-index/ele-takeout-index?storeTransmit=%7B%22trace_id%22%3A%222135e80d17034033023058783e3ad1%22%2C%22anchorScene%22%3A%22BLANK%22%2C%22subsubchannel%22%3A%22mobile.default.alsc-rec-data-center%3ATpp-26736%22%7D&menu_extra_info=%7B%22is_anchor%22%3Afalse%2C%22name_desc%22%3A%22%E5%88%9A%E5%88%9A%E7%9C%8B%E8%BF%87%22%2C%22skip_select_sku%22%3Atrue%2C%22group_name%22%3A%22%E5%88%9A%E5%88%9A%E7%9C%8B%E8%BF%87%22%2C%22sku_ids%22%3A%5B%22300000948291610936%22%5D%2C%22popularity%22%3A0%2C%22type%22%3A%22CUSTOM%22%7D&shopId=E8340370433263296704&cartTransmit=%7B%22trace_id%22%3A%222135e80d17034033023058783e3ad1%22%2C%22type%22%3A1%2C%22scheme_type%22%3A%22ITEM_STICKY_CATEGORY_SCHEME%22%2C%22subsubchannel%22%3A%22mobile.default.alsc-rec-data-center%3ATpp-26736%22%7D&geohash=uxuzvpgrcrz&brandId=848643&o2o_extra_param=%7B%22rank_id%22%3A%223a6c91965c554e56820ca15a64b67742%22%7D&spm=a2f6g.13154471.searchFoodList.1&keyword=%E7%89%9B%E7%BA%A6%E5%A0%A1&rank_id=3a6c91965c554e56820ca15a64b67742&refer=%E7%9B%B4%E6%8E%A5%E6%90%9C%E7%B4%A2&content_track=%257B%2522traceId%2522%253A%25222135e80d17034033023058783e3ad1%2522%252C%2522rank_id%2522%253A%25223a6c91965c554e56820ca15a64b67742%2522%252C%2522openingShopAmount%2522%253A215%252C%2522lbehavor_biztype%2522%253A%2522waimai%2522%252C%2522statusWeight%2522%253A5%252C%2522aoi_id%2522%253A3637497%252C%2522restingShopAmount%2522%253A43%252C%2522tpp_buckets%2522%253A%252226551%25230%2523235060%252318_26551%252314808%2523468845%252390_26551%252322935%2523470538%252319%2522%252C%2522scene%2522%253A%2522SEARCH_BROWSER%2522%257D&page_type=0&from=mobile.default&fromVersion=11.5.1&guideTrack=%257B%2522search_tpp_buckets%2522%253A%252219907%25230%2523331454%25235_19907%252323929%2523472663%25235_18536%25230%2523366272%25230_18536%252311865%2523444408%25235_18536%252311759%2523444204%2523338_18536%252310700%2523439646%25239_26556%25230%2523318107%252310%2522%252C%2522algoExtends%2522%253A%2522%25255B%25257B%252522full_name%252522%25253A%252522%2525E5%2525B0%25258A%2525E5%2525AE%25259D%2525E6%2525AF%252594%2525E8%252590%2525A8%252522%25252C%252522entityType%252522%25253A%252522query%252522%25252C%252522entityId%252522%25253A%252522-5456059578008725565%252522%25257D%25255D%2522%252C%2522alscJointAbTag%2522%253A%2522domain_search_temp_base%2522%252C%2522personalizedDisable%2522%253Afalse%252C%2522search_rank_id%2522%253A%2522843b618d4b5941c6ab3577c66ea36096%2522%257D&longitude=106.542348&latitude=29.403941&spm-pre=a2f6g.12507204.search.1
    if data=="店铺3":
        rating,a,b,c=mark_test()
        print(rating)
        str="欢迎使用我们的评分程序！ 您正在查看的店铺当前的综合评分为：%.2f分  ； 其中店铺评论共有：%d  ; 好评：%d， 中评：%d，差评：%d  ;   (注：此评分仅供您参考，希望您根据我们提供的建议有一段美好的体验。同时我们鼓励您根据自己的需求和体验，为该店铺提供宝贵的评分和反馈，以帮助他们持续改进并为您提供更优质的服务。）"%(rating,a+b+c,a,b,c)
        return str
    else:
                
        return "输入有误"

'''
欢迎使用我们的评分程序！
您正在查看的店铺当前的综合评分为：
xxxx
其中店铺销量：xxx
好评：xxx，中评：xxx，差评：xxx
此评分仅供您参考，希望您根据我们提供的建议有一段美好的体验。
同时我们鼓励您根据自己的需求和体验，为该店铺提供宝贵的评分和反馈，以帮助他们持续改进并为您提供更优质的服务。

'''

if __name__ == '__main__':
      
    app.run(debug=True)
    
    




