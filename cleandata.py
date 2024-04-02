import pandas as pd

df = pd.read_csv('baby_trade.csv', encoding='GBK')

df = df[['cat_id', 'day', 'label']]
df = df[df['label'] != 0]

df['month'] = df['day'].astype(str).str[:-2].astype(int)

output_lines = []
for _, group_df in df.groupby(['cat_id', 'month']):
    cat_id, month = group_df.iloc[0]['cat_id'], group_df.iloc[0]['month']
    for _, row in group_df.iterrows():
        output_lines.append(f"{cat_id}:{row['day']}, {row['label']}")
    output_lines.append('')

with open('output2.txt', 'w') as file:
    file.write('\n'.join(output_lines))
