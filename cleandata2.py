import pandas as pd

# 读取数据
df = pd.read_csv('baby_trade.csv', encoding='GBK')

# 选择所需列，并去除 label 为 0 的行
df = df[['cat_id', 'day', 'label']]
df = df[df['label'] != 0]

# 提取月份
df['month'] = df['day'].astype(str).str[:-2].astype(int)
import pandas as pd

# 读取数据
df = pd.read_csv('baby_trade.csv', encoding='GBK')

# 选择所需列，并去除 label 为 0 的行
df = df[['cat_id', 'day', 'label']]
df = df[df['label'] != 0]

# 提取月份
df['month'] = df['day'].astype(str).str[:-2].astype(int)

# 创建一个空字典，用于跟踪每个组的元素
grouped_elements = {}

# 遍历每个组
for _, group_df in df.groupby(['cat_id', 'month']):
    cat_id, month = group_df.iloc[0]['cat_id'], group_df.iloc[0]['month']
    key = f"({cat_id},{month})"
    grouped_elements[key] = {}
    # 将每个组中的元素按照 day 值进行分组
    for day, label in group_df[['day', 'label']].values:
        if day not in grouped_elements[key]:
            grouped_elements[key][day] = []
        grouped_elements[key][day].append(label)

# 构建输出字符串
output_lines = []
for key, value in grouped_elements.items():
    output_lines.append(f"{key}:<{{")
    # 将每个 day 的元素按照 day 值排序后输出
    for day, labels in sorted(value.items()):
        output_lines.append(f"    ({day}):{{{','.join(map(str, labels))}}}")
    output_lines.append("}>")

# 在每个">"后换行
output = '\n'.join(output_lines)

# 写入文件
with open('output.txt', 'w') as file:
    file.write(output)
