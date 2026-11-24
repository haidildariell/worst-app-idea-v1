"""Write the worst app idea pitch to /output/entry.txt."""

import os

WORST_APP_PITCH = (
    "GrandmaGram is a social network exclusively for grandmothers to rate "
    "each other's grandchildren, with a premium tier that lets you boost "
    "your grandson to the top of the family leaderboard."
)


def write_entry(output_dir, pitch):
    """Write one pitch sentence to entry.txt inside output_dir."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(pitch)
    return path


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(output_dir, WORST_APP_PITCH)


if __name__ == "__main__":
    main()
