import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("ECI_URL", "https://officials.eci.gov.in/aero")
PROFILE_PATH = os.path.abspath(os.getenv("PROFILE_PATH", "chrome_profile_eci"))
WAIT_TIME = int(os.getenv("WAIT_TIME", "20"))

USER_ID = os.getenv("ECI_USER_ID")
USER_PASSWORD = os.getenv("ECI_PASSWORD")