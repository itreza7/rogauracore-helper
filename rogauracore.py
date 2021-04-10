#!/usr/bin/python3.8
import json
import os
import sys


def convert_arg():
    data = []
    for farg in sys.argv:
        if farg.startswith('--'):
            data.append(farg.replace('--', ''))
    return data


args = convert_arg()

full_path = os.path.realpath(__file__)

path = os.path.split(full_path)[0]+'/rogauracore.json'

with open(path) as json_file:
    data = json.load(json_file)

brightness = data['brightness']
colors = data['colors']
current_color = data['current_color']
colors_len = len(colors)

if 'inc' in args:
    if brightness < 3:
        brightness += 1
    os.system('rogauracore brightness %d' % brightness)

if 'dec' in args:
    if brightness > 0:
        brightness -= 1
    os.system('rogauracore brightness %d' % brightness)

if 'next' in args:
    if colors_len > current_color:
        current_color += 1
    else:
        current_color = 1
    os.system('rogauracore %s' % colors[str(current_color)])

if 'prev' in args:
    if current_color > 1:
        current_color -= 1
    else:
        current_color = colors_len
    os.system('rogauracore %s' % colors[str(current_color)])

data['current_color'] = current_color
data['brightness'] = brightness
with open(path, 'w') as outfile:
    json.dump(data, outfile, sort_keys=True, indent=4)
