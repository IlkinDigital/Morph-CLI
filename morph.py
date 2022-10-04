# Copyright 2022 Ilkin Mammadli

import argparse 

import action_handles as handles

parser = argparse.ArgumentParser(prog='Morph CLI', description='Morph CLI')
parser.add_argument('--create', help='create Morph application at provided directory')
parser.add_argument('--title', help='title for the project')

args = parser.parse_args()

# Handle args
if (args.create != None and args.title != None):
    print(f'Creating Morph application at "{args.create}"')
    handles.create_morphapp(args.create, args.title)
    parser.exit()


# Shouldn't get there (for debug only)
print("End")