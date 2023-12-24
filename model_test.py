'''
本程序用于测试模型，根据提示输入外卖评论，模型进行分析
'''
import tensorflow as tf
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

    return predicted_label


if __name__ == '__main__':
    review=['']
    print("输入退出终止")
    while True:
        review=[input("输入评论：\n")]
        if review==['退出']:
            break
        label=predict_sentiment(review, model, tokenizer)
        if label==2:
            print('好评\n')
        elif label==1:
            print('中评\n')
        elif label==0:
            print('差评\n')
        else:
            print('请检查您的输入\n')
                  