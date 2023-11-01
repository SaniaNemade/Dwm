#Agglomerative
from itertools import combinations

# Function to generate candidate sets
def generate_candidate_sets(item_sets, k):
    candidates = []
    for item_set1 in item_sets:
        for item_set2 in item_sets:
            if item_set1 != item_set2:
                candidate = sorted(list(set(item_set1) | set(item_set2)))
                if len(candidate) == k and candidate not in candidates:
                    candidates.append(candidate)
    return candidates

# Function to calculate support for item sets
def calculate_support(dataset, item_set):
    count = 0
    for transaction in dataset:
        if all(item in transaction for item in item_set):
            count += 1
    return count / len(dataset)

# Function to prune candidate sets based on minimum support
def prune_candidates(dataset, candidates, min_support):
    pruned_candidates = []
    for candidate in candidates:
        support = calculate_support(dataset, candidate)
        if support >= min_support:
            pruned_candidates.append(candidate)
    return pruned_candidates

# Function to find frequent item sets
def apriori(dataset, min_support, min_confidence):
    item_sets = [[item] for item in set(item for transaction in dataset for item in transaction)]
    frequent_item_sets = []
    k = 2
    while item_sets:
        candidates = generate_candidate_sets(item_sets, k)
        candidates = prune_candidates(dataset, candidates, min_support)
        
        if len(candidates) == 0:
            break
        
        frequent_item_sets = candidates
        item_sets = candidates
        k += 1

    return frequent_item_sets
# Function to generate association rules
def generate_association_rules(frequent_item_sets, dataset, min_confidence):
    association_rules = []
    for item_set in frequent_item_sets:
        if len(item_set) > 1:
            for i in range(1, len(item_set)):
                antecedent_combinations = combinations(item_set, i)
                for antecedent in antecedent_combinations:
                    antecedent = sorted(list(antecedent))
                    consequent = sorted(list(set(item_set) - set(antecedent)))
                    support_item_set = calculate_support(dataset, item_set)
                    support_antecedent = calculate_support(dataset, antecedent)
                    confidence = support_item_set / support_antecedent
                    if confidence >= min_confidence:
                        association_rules.append((antecedent, consequent, round(confidence * 100, 2)))
    return association_rules

#  dataset for transactions
dataset = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

# Input minimum support and confidence as percentages
min_support_percent = float(input("Enter minimum support (in percentage): "))
min_confidence_percent = float(input("Enter minimum confidence (in percentage): "))

min_support = min_support_percent / 100
min_confidence = min_confidence_percent / 100

frequent_item_sets = apriori(dataset, min_support, min_confidence)

# Display only the final frequent item sets
print("\nFrequent Item Sets:")
for item_set in frequent_item_sets:
    print(item_set)

# Generate and display association rules
association_rules = generate_association_rules(frequent_item_sets, dataset, min_confidence)
print("\nAssociation Rules:")
for rule in association_rules:
    antecedent, consequent, confidence = rule
    print(f"{antecedent} -> {consequent}, Confidence = {confidence:.2f}%")