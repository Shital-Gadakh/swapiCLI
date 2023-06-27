"""
parsing

text file parse:  we are reading/treating the file line by line
"""

import argparse

developers = {"java": ["prashant", "rahul", "hardik"],
              "python": ["sachin", "dhoni"]
              }

parser = argparse.ArgumentParser(
    description="handy tool to greet of developers")

print(parser)
print(type(parser))  # object of class `<class 'argparse.ArgumentParser'>`


parser.add_argument("developer1", type=str, choices=["python", "java"])
parser.add_argument("developer2", type=str, choices=["python", "java"])

args = parser.parse_args()


if args.developer1 == "java" or args.developer1 == "python":
    print(f"List of developers -\n {developers.get(args.developer1)}")
else:
    print("ERROR: please choose either python or java")


if args.developer2 == "java" or args.developer2 == "python":
    print(f"List of developers -\n {developers.get(args.developer2)}")
else:
    print("ERROR: please choose either python or java")


# Use this Command  =  python argparsetwo commands.py java python
