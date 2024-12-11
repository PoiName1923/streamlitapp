import os
import subprocess
import sys


subprocess.Popen([sys.executable, "-m", "streamlit", "run", "test/testapp.py"])