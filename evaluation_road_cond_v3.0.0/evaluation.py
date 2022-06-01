import pandas as pd
import cv2

path = '../_Prediction.csv'
path_data = '/Users/macone/Documents/3_dataset/ReleaseVer/'


df = pd.read_csv(path)

# print(df.head())
# print(df.info())

cols = df.columns

image_names = df['img']
for image_name in image_names:
    print(type(image_name))
    # print(image_name)

# print(type(cols))

# df_new = df['day_night_preds'].values.tolist()
# print(type(df_new))
# for col in cols:
#     print(col)

# print(df.info())
# vis_es_preds = list(df['day_night_preds'].values)
# print(vis_es_preds)

# print('This is the evaluation for program v3.0.0')
