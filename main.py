"""Charm the Commuter: Forecast a City That Isn't — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one line of weather, 140 characters at most, for a city that does not exist.
"""
import os

LINE = "In Borington today: light drizzle of confetti, a 90% chance of naps, and the 8 AM train is on time for once."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
