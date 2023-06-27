import argparse

parser = argparse.ArgumentParser(
    description="handy tool to greate developers"
)

parser.add_argument("developer", type=str)
args = parser.parse_args()

print(f"Hello {args.developer}")
