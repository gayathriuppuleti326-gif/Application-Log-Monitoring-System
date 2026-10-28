import logging
import random
import time
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "application.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def simulate_request(request_id: int) -> None:
    """Simulate one application request and record its outcome."""
    outcome = random.choices(
        ["INFO", "WARNING", "ERROR"],
        weights=[75, 15, 10],
        k=1,
    )[0]

    if outcome == "INFO":
        logging.info("request_id=%s status=success response_ms=%s",
                     request_id, random.randint(40, 250))
    elif outcome == "WARNING":
        logging.warning("request_id=%s status=slow_response response_ms=%s",
                        request_id, random.randint(700, 1500))
    else:
        logging.error("request_id=%s status=failed error=simulated_application_error",
                      request_id)

def main() -> None:
    print("Application Log Monitoring System")
    print(f"Log file: {LOG_FILE.resolve()}")
    print("Generating 20 sample application events...")
    for request_id in range(1, 21):
        simulate_request(request_id)
        time.sleep(0.05)
    logging.info("monitoring_run_completed timestamp=%s",
                 datetime.now().isoformat(timespec="seconds"))
    print("Done. Open logs/application.log to view the events.")

if __name__ == "__main__":
    main()
