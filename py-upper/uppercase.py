import sys

def to_upper(text: str) -> str:
    return text.upper()

def to_lower(text: str) -> str:
    return text.lower()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: uppercase.py [-U|-L] <string_to_convert>")
    else:
        mode = sys.argv[1] if sys.argv[1] in ["-U", "-L"] else "-U"
        text = sys.argv[2] if mode in ["-U", "-L"] else sys.argv[1]

        result = to_upper(text) if mode == "-U" else to_lower(text)
        print(result)
