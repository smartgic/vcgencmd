from .vcgencmd import subprocess

try:
    subprocess.check_output("vcgencmd")
except Exception:
    raise ImportError("\"vcgencmd\" command not found")
