"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""

def make_readable(seconds):
	hours = seconds // 3600
	minutes = (seconds - hours * 3600) // 60
	seconds = seconds - (hours * 3600) - (minutes * 60)
	return f"{hours:0>2d}:{minutes:0>2d}:{seconds:0>2d}"

print(make_readable(359999))