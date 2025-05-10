from flag_loader import store

def evaluate_flags(user: str, region: str):
    results = {}
    flags = store.get_flags()

    for flag_name, rules in flags.items():
        result = rules.get("default", False)
        if region in rules.get("regions", {}):
            result = rules["regions"][region]
        if user in rules.get("users", {}):
            result = rules["users"][user]
        results[flag_name] = result

    return results
