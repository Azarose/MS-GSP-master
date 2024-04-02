def parse_input(input_str):
    # 移除输入字符串开头和结尾的尖括号
    trimmed_str = input_str[2:-2]
    # 分割字符串为多个段，这些段原先由大括号包围
    segments = trimmed_str.split('}{')
    parsed_data = []
    for segment in segments:
        # 将每个段中的数字字符串转换为整数，形成元组
        numbers = tuple(map(int, segment.split(',')))
        parsed_data.append(numbers)
        print(parsed_data)
    return parsed_data



def generate_initial_candidates(data):
    """生成长度为1的所有候选序列"""
    candidates = set()
    for sequence in data:
        for item in sequence:
            candidates.add((item,))
            # print(candidates)
    return candidates


def find_support(candidate, data):
    """计算候选序列在数据中的支持度（出现次数）"""
    count = 0
    for sequence in data:
        i = 0
        for item in sequence:
            if i < len(candidate) and candidate[i] == item:
                i += 1
            if i == len(candidate):
                count += 1
                break
    return count


def generate_next_candidates(prev_candidates):
    """根据前一轮的候选序列生成下一轮的候选序列"""
    next_candidates = set()
    for seq1 in prev_candidates:
        for seq2 in prev_candidates:
            if seq1[:-1] == seq2[:-1] and seq1[-1] != seq2[-1]:
                next_candidates.add(seq1 + (seq2[-1],))
                # print(next_candidates)
    return next_candidates


def gsp(input_str, least_count=1):
    data = parse_input(input_str)
    candidates = generate_initial_candidates(data)
    all_patterns = []

    while candidates:
        current_patterns = []
        for candidate in candidates:
            count = find_support(candidate, data)
            if count >= least_count:
                current_patterns.append((candidate, count))
        all_patterns.append(current_patterns)
        candidates = generate_next_candidates(candidates)

    return all_patterns


# 测试用例
input_str = "<{3}{1}{4}{4}{3}{1}{4}{4}{4}{3}{4}{4,4,4,4}{4}{4}>"
all_patterns = gsp(input_str, least_count=1)

# 打印结果
for i, patterns in enumerate(all_patterns, 1):
    if patterns:  # 只有当存在模式时才打印
        print(f"The number of length {i} sequential pattern is {len(patterns)}")
        for pattern, count in patterns:
            print(f"Pattern : <{{{''.join(map(str, pattern))}}}>: Count = {count}")
