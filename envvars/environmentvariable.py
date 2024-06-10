import os

envkeys = list(os.environ.keys())

loglevel = "DEBUG"

if "LOGLEVEL" in envkeys:
    loglevel = os.getenv("LOGLEVEL", "INFO")

print(f"{loglevel=}")
