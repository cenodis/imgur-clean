#!/usr/bin/env python3

import re
import argparse
parser = argparse.ArgumentParser()                                               

parser.add_argument("--file", "-f", type=str, required=True)
parser.add_argument("--enable-id-groups", "-g", action="store_true", help='Enables matching of the imgur.com/id1,id2,id3,... format.')
args = parser.parse_args()

f = open(args.file, "r")
dump = f.read()
f.close()

regex = r"(?:(?:(?:[hH][tT][tT][pP][sS]?:\\?\/\\?\/)?(?:[wW][wW][wW]\.|[im]\.)?[iI][mM][gG][uU][rR](?:\.|(?:.?[dD][oO][tT].?)|.)?(?:[cC][oO][mM]|[iI][oO])(?:\\\/|\\|\/|.?[sS][lL][aA][sS][hH]|(?:.?[sS][lL][aA][sS][hH]|.?\/)(?:\w|[^\S\r\n]|%2F)))?�(?:(?!gallery|search)(?:r\/\w+\/)?(\w{7}|\w{5})[bghlmrst]?)|(?:(?:[hH][tT][tT][pP][sS]?:\\?\/\\?\/)?(?:www\.|[im]\.)?(?:i\.[sS][tT][aA][cC][kK]\.)[iI][mM][gG][uU][rR](?:\.|(?:.?[dD][oO][tT].?)|.)?(?:[cC][oO][mM]|[iI][oO])\\?\/?)(?:(?!gallery|search)(?:r\/\w+\/)?(\w{7}|\w{5})[bghlmrst]?)|(?:(?:[hH][tT][tT][pP][sS]?:\\?\/\\?\/)?(?:[wW][wW][wW]\.|[im]\.)?[iI][mM][gG][uU][rR](?:\.|(?:.?[dD][oO][tT].?)|.)?(?:[cC][oO][mM]|[iI][oO])(?:\\\/|\\|\/|.?[sS][lL][aA][sS][hH]|(?:.?[sS][lL][aA][sS][hH]|.?\/)(?:\w|[^\S\r\n])|%2F))(?:(?!gallery|search)(?:r\/\w+\/)?(?:(?:original|mp4)(?:\\\/|\\|\/|.?[sS][lL][aA][sS][hH]|(?:.?[sS][lL][aA][sS][hH]|.?\/)(?:\w|[^\S\r\n])|%2F).+?|download(?:\\\/|\\|\/|.?[sS][lL][aA][sS][hH]|(?:.?[sS][lL][aA][sS][hH]|.?\/)(?:\w|[^\S\r\n])|%2F)?)?(\w{7}|\w{5})[bghlmrst]?|(?:a\/?\\?(\w{7}|\w{5}))|(?:(?:gallery|t\/\w+)\/(\w{7}|\w{5}))|(?:(?:user\/([^\/?#]+)(?:\", )+?(?:\/posts|\/submitted)?\/?)|(?:user\/([^\/?#]+)(?:\/posts|\/submitted)\/?)|(?:user\/([^\/?#]+)(?:\/favorites)\/?))))"

if args.enable_id_groups:
	regex = r"(?:(?:(?:[hH][tT][tT][pP][sS]?:\\?\/\\?\/)?(?:[wW][wW][wW]\.|[im]\.)?[iI][mM][gG][uU][rR](?:\.|(?:.?[dD][oO][tT].?)|.)?(?:[cC][oO][mM]|[iI][oO])(?:\\\/|\\|\/|.?[sS][lL][aA][sS][hH]|(?:.?[sS][lL][aA][sS][hH]|.?\/)(?:\w|[^\S\r\n]|%2F)))?,(?:(?!gallery|search)(?:r\/\w+\/)?(\w{7}|\w{5})[bghlmrst]?)|(?:(?:[hH][tT][tT][pP][sS]?:\\?\/\\?\/)?(?:www\.|[im]\.)?(?:i\.[sS][tT][aA][cC][kK]\.)[iI][mM][gG][uU][rR](?:\.|(?:.?[dD][oO][tT].?)|.)?(?:[cC][oO][mM]|[iI][oO])\\?\/?)(?:(?!gallery|search)(?:r\/\w+\/)?(\w{7}|\w{5})[bghlmrst]?)|(?:(?:[hH][tT][tT][pP][sS]?:\\?\/\\?\/)?(?:[wW][wW][wW]\.|[im]\.)?[iI][mM][gG][uU][rR](?:\.|(?:.?[dD][oO][tT].?)|.)?(?:[cC][oO][mM]|[iI][oO])(?:\\\/|\\|\/|.?[sS][lL][aA][sS][hH]|(?:.?[sS][lL][aA][sS][hH]|.?\/)(?:\w|[^\S\r\n])|%2F))(?:(?!gallery|search)(?:r\/\w+\/)?(?:(?:original|mp4)(?:\\\/|\\|\/|.?[sS][lL][aA][sS][hH]|(?:.?[sS][lL][aA][sS][hH]|.?\/)(?:\w|[^\S\r\n])|%2F).+?|download(?:\\\/|\\|\/|.?[sS][lL][aA][sS][hH]|(?:.?[sS][lL][aA][sS][hH]|.?\/)(?:\w|[^\S\r\n])|%2F)?)?(\w{7}|\w{5})[bghlmrst]?|(?:a\/?\\?(\w{7}|\w{5}))|(?:(?:gallery|t\/\w+)\/(\w{7}|\w{5}))|(?:(?:user\/([^\/?#]+)(?:\", )+?(?:\/posts|\/submitted)?\/?)|(?:user\/([^\/?#]+)(?:\/posts|\/submitted)\/?)|(?:user\/([^\/?#]+)(?:\/favorites)\/?))))"

with open('links.txt', 'a') as f:
  for i in re.finditer(regex, dump):
    if i.group(1):
      print('https://imgur.com/' + i.group(1))
      f.write('https://imgur.com/' + i.group(1) + '\n')
    if i.group(2):
      print('https://i.stack.imgur.com/' + i.group(2) + '.png')
      f.write('https://i.stack.imgur.com/' + i.group(2) + '.png' + '\n')
    if i.group(3):
      print('https://imgur.com/' + i.group(3))
      f.write('https://imgur.com/' + i.group(3) + '\n')
    if i.group(4):
      print('https://imgur.com/a/' + i.group(4))
      f.write('https://imgur.com/a/' + i.group(4) + '\n')
    if i.group(5):
      print('https://imgur.com/gallery/' + i.group(5))
      f.write('https://imgur.com/gallery/' + i.group(5) + '\n')
    if i.group(6):
      print('https://imgur.com/user/' + i.group(6))
      f.write('https://imgur.com/user/' + i.group(6) + '\n')
    if i.group(7):
      print('https://imgur.com/user/' + i.group(7) + '/posts')
      f.write('https://imgur.com/user/' + i.group(7) + '/posts' + '\n')
    if i.group(8):
      print('https://imgur.com/user/' + i.group(8) + '/favorites')
      f.write('https://imgur.com/user/' + i.group(8) + '/favorites' + '\n')
print("Complete")
