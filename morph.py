import argparse

parser = argparse.ArgumentParser(description='Morph CLI')

args = parser.parse_args()
print(args.accumulate(args.integers))