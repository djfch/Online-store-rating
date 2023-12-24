
import tensorflow as tf
import pandas as pd
import re
from transformers import BertTokenizer


# 指定 tokenizer 的路径
tokenizer_path = "model_my/tokenizer"
# 加载 tokenizer
tokenizer = BertTokenizer.from_pretrained(tokenizer_path)
# 加载模型
model = tf.keras.models.load_model('model_my')


def predict_sentiment(text, model, tokenizer):
    # 标记化文本
    tokens = tokenizer(text, padding=True, truncation=True, return_tensors="tf")

    # 模型推理
    outputs = model(tokens)
    # 获取预测结果
    logits = outputs['logits']
    predicted_label = tf.argmax(logits, axis=1).numpy()
    predicted_label = pd.Series(predicted_label)
    counts = predicted_label.value_counts().tolist()
    return counts

#计算评分
def calculate_rating(good_reviews, neutral_reviews, bad_reviews,total_size): #好评，中评，差评，总数

    # 定义权重
    GOOD_WEIGHT = 5
    NEUTRAL_WEIGHT = 3
    BAD_WEIGHT = 1

    # 计算总权重
    total_weight = (GOOD_WEIGHT * good_reviews) + (NEUTRAL_WEIGHT * neutral_reviews) + (BAD_WEIGHT * bad_reviews)

    # 确保评分在0-5之间
    rating = total_weight/total_size

    return rating

def mark_test():
    raw_data = pd.read_csv(r'test3.csv')
    # raw_data.head()
    # raw_data = raw_data[['rating_text','rating']]
    print(raw_data['rating'].value_counts()) 
    raw_data = raw_data['rating_text']
    #数据预处理，去除颜文字等
    info = re.compile('[0-9a-zA-Z]|#|[^\\u0000-\\uFFFF]|\s|(\ud83c[\udf00-\udfff])|(\ud83d[\udc00-\ude4f\ude80-\udeff])|[\u2600-\u2B55]/g')

    raw_data = raw_data.apply(lambda x:info.sub('',x))
    # for i in range(35,40):
    #     print(raw_data[i])
    raw_data = raw_data.tolist()
    zj=predict_sentiment(raw_data,model, tokenizer)
    #print(zj)
    #print(type(zj[0]))
    rating=calculate_rating( zj[0], zj[1], zj[2],zj[0]+zj[1]+zj[2])
    #print(rating)
    return rating,zj[0],zj[1],zj[2]