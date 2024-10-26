import pandas as pd
import numpy as np
import re
import nltk
from sklearn.model_selection import train_test_split

# Tải dữ liệu
df = pd.read_csv('sentiment140/training.1600000.processed.noemoticon.csv', encoding='ISO-8859-1', header=None)

# Đặt tên cho các cột dữ liệu
df.columns = ['target', 'ids', 'date', 'flag', 'user', 'text']

# Chuyển nhãn 4 thành 1 (tích cực)
df['target'] = df['target'].apply(lambda x: 1 if x == 4 else 0)

# Lấy cột văn bản (tweets) và nhãn
X = df['text'].values
y = df['target'].values

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tiền xử lý văn bản
nltk.download('stopwords')
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)  # Xóa các URL
    text = re.sub(r'@\w+', '', text)  # Xóa các mentions (@user)
    text = re.sub(r'#\w+', '', text)  # Xóa các hashtag
    text = re.sub(r'[^\w\s]', '', text)  # Xóa dấu câu
    text = text.lower()  # Chuyển sang chữ thường
    text = ' '.join([word for word in text.split() if word not in STOPWORDS])  # Xóa stopwords
    return text

X_train = [preprocess_text(tweet) for tweet in X_train]
X_test = [preprocess_text(tweet) for tweet in X_test]
print("Dữ liệu huấn luyện đầu tiên sau khi tiền xử lý:", X_train[:5])
print("Số lượng mẫu huấn luyện:", len(X_train))
print("Số lượng mẫu kiểm tra:", len(X_test))