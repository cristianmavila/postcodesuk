#!/usr/bin/env python

from sys import argv
from formattingcodes.codes import get_detail_code, validate_code

def input():
  code = raw_input("Enter code:")
  get_detail_code(code)

input()
