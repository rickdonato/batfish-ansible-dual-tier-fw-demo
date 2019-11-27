from pybatfish.client.commands import *
from pybatfish.question.question import load_questions
from pybatfish.datamodel.flow import (HeaderConstraints,
                                         PathConstraints)
from pybatfish.question import bfq
import random
import sys

NETWORK_NAME = "network1"
BASE_SNAPSHOT_NAME = "snapshot1"
SNAPSHOT_PATH = sys.argv[1]
BATFISH_SERVICE_IP = "172.29.236.139"

bf_session.host = BATFISH_SERVICE_IP
load_questions()

print("[*] Initializing BASE_SNAPSHOT")
bf_set_network(NETWORK_NAME)
bf_init_snapshot(SNAPSHOT_PATH, name=BASE_SNAPSHOT_NAME, overwrite=True)

print("[OK] Success - Batfish imports ready...")
