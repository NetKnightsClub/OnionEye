import json

def save_results_to_json(results, filename='results.json'):
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)

# why are stubs called stubs... why am i asking these questions in comments
