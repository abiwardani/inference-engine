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

def clean_int_float(num):
    if (int(float(num)) == float(num)):
        num = int(num)
    else:
        num = float(num)

    return num

class MineralClassificationEngine:
    def __init__(self):
        rules, hardness_points, specific_gravity_points = load_mineral_classification_rules()

        self.KBS = KnowledgeBase(rules)
        self.hardness_points = hardness_points
        self.specific_gravity_points = specific_gravity_points
        self.inferenceEngine = InferenceEngine()
    
    def get_hardness_facts(self, hardness):
        hardness = clean_int_float(hardness)
        
        hardnesses = [["hardness", str(hardness)]]

        for point in self.hardness_points:
            hardness_limit = clean_int_float(point)
            if hardness <= hardness_limit:
                hardnesses.append(["hardness", "<="+str(hardness_limit)])
            if hardness >= hardness_limit:
                hardnesses.append(["hardness", ">="+str(hardness_limit)])

        return hardnesses
    
    def get_specific_gravity_facts(self, specific_gravity):
        specific_gravity = clean_int_float(specific_gravity)
        
        specific_gravities = [["specific-fravity", str(specific_gravity)]]

        for point in self.specific_gravity_points:
            specific_gravity_limit = clean_int_float(point)
            if specific_gravity <= specific_gravity_limit:
                specific_gravities.append(["specific-gravity", "<="+str(specific_gravity_limit)])
            if specific_gravity >= specific_gravity_limit:
                specific_gravities.append(["specific-gravity", ">="+str(specific_gravity_limit)])

        return specific_gravities
    
    def make_facts_from_list(self, field, values):
        facts = [[field, val] for val in values]
        
        return facts
    
    def infer(self, initial_facts):
        learned_facts, self.KBS = self.inferenceEngine.forward_chaining(initial_facts, self.KBS)

        return list(set(learned_facts))


r, _, _ = load_mineral_classification_rules()
KBS = KnowledgeBase(r)
inferenceEngine = InferenceEngine()
initial_facts = [["color", "yellow"], ["color", "brown"], ["streak", "yellow"], ["streak", "brown"], ["luster", "earthy"], ["hardness", ">=1"], ["hardness", "<=5"], ["specific-gravity", ">=2.7"], ["specific-gravity", "<=4.3"], ["crystal-system", "cryptocrystalline"], ["diaphaneity", "opaque"], ["tenacity", "brittle"]]
initial_facts = [['rock-group', 'sedimentary'], ['color', 'yellow'], ['color', 'brown'], ['streak', 'yellow'], ['streak', 'brown'], ['hardness', '1.2'], ['hardness', '>=1'], ['hardness', '<=2.5'], ['hardness', '<=3.5'], ['hardness', '<=3'], ['hardness', '<=4'], ['hardness', '<=6'], ['hardness', '<=6.5'], ['hardness', '<=5'], ['hardness', '<=7'], ['hardness', '<=2'], ['hardness', '<=1.5'], ['hardness', '<=8'], ['hardness', '<=4.5'], ['hardness', '<=10'], ['hardness', '<=9'], ['specific-fravity', '2.8'], ['specific-gravity', '>=2.7'], ['specific-gravity', '>=2.5'], ['specific-gravity', '<=4.3'], ['specific-gravity', '<=2.8'], ['specific-gravity', '>=2.8'], ['specific-gravity', '<=5'], ['specific-gravity', '<=7.4'], ['specific-gravity', '<=7.6'], ['specific-gravity', '<=5.3'], ['specific-gravity', '<=5.2'], ['specific-gravity', '<=3'], ['specific-gravity', '<=3.4'], ['specific-gravity', '<=4.6'], ['specific-gravity', '<=6.7'], ['specific-gravity', '<=3.5'], ['specific-gravity', '<=4.4'], ['specific-gravity', '<=4'], ['specific-gravity', '<=4.9'], ['specific-gravity', '<=4.1'], ['specific-gravity', '<=5.5'], ['specific-gravity', '>=2.6'], ['specific-gravity', '>=2.1'], ['specific-gravity', '<=3.6'], ['specific-gravity', '<=3.1'], ['specific-gravity', '>=2.3'], ['specific-gravity', '<=3.3'], ['specific-gravity', '<=3.7'], ['specific-gravity', '<=4.8'], ['specific-gravity', '<=5.8'], ['specific-gravity', '>=2.4'], ['specific-gravity', '<=2.9'], ['specific-gravity', '<=3.9'], ['luster', 'earthy'], ['crystal-system', 'cryptocrystalline'], ['diaphaneity', 'opaque'], ['weathered', 'false'], ['magnetic', 'false']]

learned_facts, KBS = inferenceEngine.forward_chaining(initial_facts, KBS)

print(list(set(learned_facts)))