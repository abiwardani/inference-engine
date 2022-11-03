import json
from forward_chaining import KnowledgeBase, InferenceEngine

def load_mineral_classification_rules():
    f = open("mineral-classification-rule-base.json")
    rulebase_dict = json.load(f)
    f.close()
    rules = rulebase_dict["rules"]
    hardness_points = rulebase_dict["continuous_vars"]["turning_points"][0]
    specific_gravity_points = rulebase_dict["continuous_vars"]["turning_points"][1]

    return rules, hardness_points, specific_gravity_points

rules, hardness_points, specific_gravity_points = load_mineral_classification_rules()

# test initial facts
initial_facts = [["streak", "colorless"], ["luster", "vitreous"], ["hardness", "7"], ["specific-gravity", ">=2.6"], ["specific-gravity", "<=2.7"], ["crystal-system", "hexagonal"], ["diaphaneity", "transparent"], ["fracture", "conchoidal"], ["color", "purple"], ["streak", "white"], ["luster", "pearly"], ["hardness", ">=2.5"], ["hardness", "<=4"], ["specific-gravity", ">=2.8"], ["specific-gravity", "<=3"], ["crystal-system", "pseudohexagonal"], ["fracture", "flaky"], ["cleavage", "almost perfect"]]

KBS = KnowledgeBase(rules)
inferenceEngine = InferenceEngine()
learned_facts, KBS = inferenceEngine.forward_chaining(initial_facts, KBS)

print(list(set(learned_facts)))