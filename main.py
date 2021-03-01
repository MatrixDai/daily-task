import argparse
import requests
import json
import urllib

parser = argparse.ArgumentParser()
parser.add_argument('--title')
parser.add_argument('--url')
parser.add_argument('--method')
parser.add_argument('--host')
parser.add_argument('--cookie')
parser.add_argument('--ua')
parser.add_argument('--al')
parser.add_argument('--referer')
parser.add_argument('--payload')
parser.add_argument('--result')
parser.add_argument('--wc')
args = parser.parse_args()


def read_json_by_key(data, key):
    for i in key.split("."):
        if i in data:
            data = data[i]
        else:
            return None
    return data


def notify(title, desp):
    form = {"title": title, "desp": desp}
    requests.request('GET', f'{args.wc}?{urllib.parse.urlencode(form)}')


if __name__ == '__main__':
    headers = {
        'Host': args.host,
        'Cookie': args.cookie,
        'User-Agent': args.ua,
        'Accept-Language': args.al
    }
    if args.referer:
        headers['Referer'] = args.referer

    data = {}
    if args.payload:
        data = args.payload

    response = requests.request(args.method, args.url, headers=headers, data=data)
    result = 'Error'
    if response.status_code == requests.codes.ok:
        data_json = response.text
        if response.text.endswith(');'):
            data_json = response.text.split("(", 1)[1].strip(");")
        jj = json.loads(data_json)
        result = read_json_by_key(jj, args.result)
    else:
        result = response.text

    notify(args.title, result)
