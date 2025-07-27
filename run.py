import json
from tor_skimmer.scanner import scan_sites

def load_seeds(filename='seeds.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data.get('seeds', [])

def main():
    seeds = load_seeds()
    print("Starting scan from seeds:")
    for seed in seeds:
        print(f" - {seed}")
    scan_sites(seeds)

if __name__ == "__main__":
    main()

# man i sure wish the burger tank was open
