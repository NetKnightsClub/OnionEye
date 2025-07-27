import json
import os
import logging
from datetime import datetime
from tor_skimmer.scanner import scan_sites

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    log_filename = f"logs/run_{datetime.now().strftime('%Y%m%d')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(asctime)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("OnionEye")

def load_seeds(filename='seeds.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        logger.error(f"Failed to load seeds: {e}")
        return []

def log_dead_sites(dead_sites):
    if not dead_sites:
        return
    with open("dead_onions.txt", "a") as f:
        date = datetime.utcnow().strftime("%Y/%m/%d")
        for site in dead_sites:
            f.write(f"{site} | DEAD | {date}\n")

def main():
    seeds = load_seeds()
    if not seeds:
        logger.warning("No seeds to scan. Exiting.")
        return

    logger.info("Starting scan from seeds:")
    for seed in seeds:
        logger.info(f" - {seed}")

    results = scan_sites(seeds)

    dead = [url for url, is_alive in results.items() if not is_alive]
    if dead:
        logger.warning(f"{len(dead)} dead sites found.")
        log_dead_sites(dead)
    else:
        logger.info("No dead sites found!")

if __name__ == "__main__":
    logger = setup_logger()
    try:
        main()
    except Exception as e:
        logger.exception("Unhandled error during scan.")

# man i sure wish the burger tank was open right now... i could go for a barbecue bacon burger, a large side of fries, an orange soda with no ice, and a hot apple pie.
