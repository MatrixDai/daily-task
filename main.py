import argparse
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument('--url')
parser.add_argument('--method')
parser.add_argument('--host')
parser.add_argument('--cookie')
parser.add_argument('--ua')
parser.add_argument('--al')
parser.add_argument('--referer')
parser.add_argument('--result')
args = parser.parse_args()


def read_json_by_key(data, key):
    for i in key.split("."):
        if i in data:
            data = data[i]
        else:
            return None
    return data


if __name__ == '__main__':
    headers = {
        'Host': args.host,
        'Cookie': args.cookie,
        'User-Agent': args.ua,
        'Accept-Language': args.al,
        'Referer': args.referer
    }
    response = requests.request(args.method, args.url, headers=headers, data={})
    if response.status_code == requests.codes.ok:
        data_json = response.text
        if response.text.endswith(');'):
            data_json = response.text.split("(", 1)[1].strip(");")
        # print(data_json)
        jj = json.loads(data_json)
        # print(jj['data'])
        print(read_json_by_key(jj, args.result))
