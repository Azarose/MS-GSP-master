import re

def parse_data(data):
    """
    Parse the given data string into a list of transactions.
    Each transaction is a list of items.
    """
    # Removing leading and trailing angle brackets
    data = data.strip('<>').strip("{}")
    # Splitting transactions based on '}{'
    transactions = [t.split(',') for t in re.split(r'}{', data)]
    # Converting each item to integer
    transactions = [[int(item) for item in transaction] for transaction in transactions]
    return transactions

def generate_candidates(prev_candidates, length):
    """
    Generate candidates of given length from previous candidates.
    """
    candidates = []
    for i in range(len(prev_candidates)):
        for j in range(i + 1, len(prev_candidates)):
            if prev_candidates[i][:-1] == prev_candidates[j][:-1]:
                candidates.append(prev_candidates[i] + [prev_candidates[j][-1]])
    return candidates

def filter_candidates(transactions, candidates, min_support):
    """
    Filter candidates by min_support, returning only those with enough support.
    """
    filtered_candidates = []
    candidate_counts = {tuple(candidate): 0 for candidate in candidates}
    for transaction in transactions:
        for candidate in candidates:
            if all(item in transaction for item in candidate):
                candidate_counts[tuple(candidate)] += 1
    for candidate, count in candidate_counts.items():
        if count >= min_support:
            filtered_candidates.append(list(candidate))
    return filtered_candidates

def gsp(transactions, min_support):
    """
    Perform the GSP algorithm on the given transactions.
    """
    single_items = sorted({item for transaction in transactions for item in transaction})
    single_candidates = [[item] for item in single_items]
    result = filter_candidates(transactions, single_candidates, min_support)
    k = 2
    while True:
        candidates = generate_candidates(result[-1], k)
        candidates = filter_candidates(transactions, candidates, min_support)
        if not candidates:
            break
        result.extend(candidates)
        k += 1
    return result

# Example usage
min_support = 2  # Example min_support value, adjust as needed
data = "<{3}{1}{3}{3}{3}{3}{1,4,1}{1}{1}{3,4}{3}{1}{1,1}{1}{1,3}{1}{3}{1,1,1,1}>"  # Example data
transactions = parse_data(data)
patterns = gsp(transactions, min_support)
print("Frequent Sequences:")
for pattern in patterns:
    print(pattern)
