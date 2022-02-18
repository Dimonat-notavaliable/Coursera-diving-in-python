import os
import tempfile
import argparse
import json
from json.decoder import JSONDecodeError


parser = argparse.ArgumentParser()

parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if not os.path.exists(storage_path):
    with open(storage_path, 'w') as outfile:
        pass

if args.value and args.key:
    with open(storage_path, 'r') as json_file:
        try:
            data = json.load(json_file)
            data.setdefault(args.key, [])
            data[args.key].append(args.value)
        except JSONDecodeError:
            data = {args.key: []}
            data[args.key].append(args.value)

    with open(storage_path, 'w') as json_file:
        json.dump(data, json_file)

elif args.key:
    with open(storage_path, 'r') as json_file:
        try:
            data = json.load(json_file)
            result = data.get(args.key, None)
            print(*result, sep=", ") if result else print(result)
        except JSONDecodeError:
            pass
