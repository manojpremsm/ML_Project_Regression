import logging 
import os
import sys 
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

print(LOG_FILE.split(".")[0])