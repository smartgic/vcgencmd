from .vcgencmd2 import *

try:
    subprocess.check_output("vcgencmd")
except Exception:
    raise ImportError("\"vcgencmd\" command not found")
