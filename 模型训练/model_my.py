'''
训练模型，迁移学习，如要训练请自行下载谷歌的bert-base-chinese模型
'''
import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
import re

# 1. 准备数据
# 假设你有一个包含评论和情感标签的数据集，X是评论文本，y是情感标签

data = pd.read_csv('data.csv') #训练数据集，此处仅提供少量数据集进行测试
X = data['comment'].astype('str').tolist()
#for i in range(len(X)):
#    X[i] = X[i].replace(' ','')
y = data['label'].tolist()
# print(X)
# print(y)

# X = ["This is a positive review.", "Negative experience!", "Neutral feedback."]
# y = [1, 0, 2]  # 1表示正面，0表示负面，2表示中性
# 划分训练集和验证集
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
model_path='moxing'
# 2. 加载预训练的BERT模型和标记器
tokenizer = BertTokenizer.from_pretrained(model_path)
model = TFBertForSequenceClassification.from_pretrained(model_path, num_labels=3)

# 3. 对文本进行标记化和编码
train_encodings = tokenizer(X_train, truncation=True, padding=True, return_tensors='tf')
val_encodings = tokenizer(X_val, truncation=True, padding=True, return_tensors='tf')

# 4. 构建TF数据集
train_dataset = tf.data.Dataset.from_tensor_slices((
    dict(train_encodings),
    np.array(y_train)
))

val_dataset = tf.data.Dataset.from_tensor_slices((
    dict(val_encodings),
    np.array(y_val)
))


# 5. 定义模型训练和评估
optimizer = tf.keras.optimizers.Adam(learning_rate=5e-5)
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
metric = tf.keras.metrics.SparseCategoricalAccuracy('accuracy')

model.compile(optimizer=optimizer, loss=loss, metrics=[metric])
# 6. 模型训练
model.fit(train_dataset.shuffle(100).batch(16), epochs=10, batch_size=16, validation_data=val_dataset.batch(16))
# 7. 模型评估
results = model.evaluate(val_dataset.batch(16))

model.save("model_my", save_format="tf")

# 保存 tokenizer 以便在部署时使用
tokenizer.save_pretrained("model_my/tokenizer")

def predict_sentiment(text, model, tokenizer):
    # 标记化文本
    tokens = tokenizer(text, padding=True, truncation=True, return_tensors="tf")

    # 模型推理
    outputs = model(tokens)
    print(outputs)
    # 获取预测结果
    logits = outputs.logits
    predicted_label = tf.argmax(logits, axis=1).numpy()[0]

    return predicted_label

def predict_function(input_text):
    text = []
    for i in range(len(input_text)):
        text.append(predict_sentiment(input_text[i], model, tokenizer))
    return text
#模型测试
a=['味道口感：第一次点他们家的，味道不错餐品分量：分量足']
print(predict_function(a))
#pinglun = predict_function(raw_data)
