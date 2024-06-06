"""
All the functions defined in this module should be written using the re module.
They are tested by ``test_regex.py``.
"""
import re


def is_hex(string):
    """is_hex should return True if the given string only consists of digits and the
    letters A through to F."""


def has_vowel(string):
    """has_vowel should return True if the given string has a vowel (any of the
    letters aeiou) and False if it doesn't"""


def split_words(string):
    """Using re.split split the given string into a list of words."""


def grouped_date(string):
    """Using groups return the year, month and day from a date formatted as
    yyyy-mm-dd"""


def sub_digits(string):
    """Replace all digits with X using re.sub"""


def date_rewrite(string):
    """Rewrite dates in "American" style format to ISO 86001 format.
    i.e. m/dd/yyyy or mm/d/yyyy should become yyyy-mm-dd"""


def findall_airportcodes(string):
    """Find all the airport codes in the supplied string. An airport code is
    a three letter uppercase word."""


def valid_times(string):
    """Write a single regular expression that will match valid 24 hour times only
    in the format 00:00 to 23:59, but not invalid times like 00:60 or 24:00."""
