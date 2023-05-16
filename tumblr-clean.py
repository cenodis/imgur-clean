#!/usr/bin/env python3

# Attempts to extract imgur links from tumblr URLs such as
# https://xxxx.tumblr.com/post/xxxx/xxxxx-httpimgurcom28htojx

# Can potentially result in garbage links, use with caution

import sys
import re

from enum import Enum

tumblr_regex = re.compile(r"tumblr.*?(?P<raw>i)?imgur(?:com|io)(?P<id>\w{5,8})")
thumb_list = ["s", "b", "t", "m", "l", "h"]

RAW = 0
ALBUM = 1
GALLERY = 2

class ImgurIdException(Exception):
	pass

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs, flush=True)

def clean(is_raw, imgur_id):
	length = len(imgur_id)
	
	if imgur_id.startswith("gallery"):
		return (GALLERY, None)
	
	if is_raw:
		if length in [5, 7]:
			return (RAW, imgur_id)
		elif length == 8:
			return (RAW, imgur_id[:-1])
		elif length == 6 and imgur_id[5] in thumb_list:
			return (RAW, imgur_id[:-1])
		else:
			raise ImgurIdException(f"Invalid length and suffix for raw ID {imgur_id}")

	if length in [5, 7]:
		return (RAW, imgur_id)
	
	if length in [6, 8]:
		maybe_album = imgur_id.startswith("a")
		maybe_thumb = imgur_id[-1:] in thumb_list
		
		if maybe_album and maybe_thumb:
			raise ImgurIdException(f"Ambiguous imgur id {imgur_id}")
		if maybe_album:
			return (ALBUM, imgur_id[1:])
		if maybe_thumb:
			return (RAW, imgur_id[:-1])
		
	raise ImgurIdException(f"Unable to process imgur id {imgur_id}")


for line in sys.stdin:
	if match := tumblr_regex.search(line):
		is_raw = match.group("raw") is not None
		imgur_id = match.group("id")
		try:
			imgur_type, imgur_id = clean(is_raw, imgur_id)
			if imgur_type == GALLERY:
				pass
			elif imgur_type == RAW:
				print(f"https://imgur.com/{imgur_id}")
			else:
				print(f"https://imgur.com/a/{imgur_id}")
		except ImgurIdException as err:
			eprint(f"{str(err)}\n{line}")
