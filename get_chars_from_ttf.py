"""
FFG-benchmarks
Copyright (c) 2021-present NAVER Corp.
MIT license
"""
import sys
from tqdm import tqdm
from pathlib import Path

from base.dataset import get_filtered_chars


def main():
    root_dir = sys.argv[1]
    print(root_dir)
    ttffiles = sorted(Path(root_dir).rglob("*.ttf"))

    # for ttffile in tqdm(ttffiles):
    for ttffile in tqdm(ttffiles, desc="Font files", position=0):
        txtfile = Path(str(ttffile).replace(".ttf", ".txt"))
        if txtfile.is_file():
            continue
        try:
            avail_chars = get_filtered_chars(ttffile)
            with open(txtfile, "w", encoding='utf-8') as f:
                f.write("".join(avail_chars))
        except Exception as e:
            tqdm.write(f"Error processing {ttffile}: {e}")


if __name__ == "__main__":
    main()
