#!/usr/bin/env python3
# Created by: Gustav I
# Created on: April 19, 2025
# This program executes a for loop for RGB selections.


def main():
    for r in range(0, 256, 85):  # Red values
        for g in range(0, 256, 85):  # Green values
            for b in range(0, 256, 85):  # Blue values
                color_text = f"RGB({r}, {g}, {b})"
                print(f"\033[38;2;{r};{g};{b}m{color_text}\033[0m")


if __name__ == "__main__":  # Call the function
    main()
