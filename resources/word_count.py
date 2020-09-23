import os
from collections import Counter
from pathlib import Path

INPUTS_PATH = os.environ.get("NEVERMINED_INPUTS_PATH")
OUTPUTS_PATH = os.environ.get("NEVERMINED_OUTPUTS_PATH")

def word_count():
    """Count words in all files under INPUTS_PATH"""
    word_counter = Counter()

    # read files and count words
    for file_path in Path(INPUTS_PATH).rglob("*"):
        if file_path.is_file():
            print(f"Processing input file: {file_path.as_posix()}")
            word_counter += Counter(file_path.read_text().split())

    # write the result to OUTPUTS_PATH
    output_file = Path(OUTPUTS_PATH) / "output.txt"
    with output_file.open("w") as f:
        for word, count in word_counter.most_common():
            f.write(f"{word}: {count}\n")
    print(f"Generated output file: {output_file.as_posix()}")


if __name__ == "__main__":
    word_count()
