"""
Problem Description:
Given a string, split it into major separated parts by the special character '/'. 
For each major part split by '/', we can further split it into minor parts 
separated by a specific character (space implied by context).

Compression Steps:
1. Part 1 Compression:
   - For each major part, compress each minor part by keeping the first 
     and last characters intact and replacing the middle characters 
     with their count.

2. Part 2 Compression:
   - After Part 1 compression, merge consecutive minor parts of each 
     major part to form new minor parts.

Parameters:
- Input string `str`: The string to be processed.
- `minor_parts`: The number of minor parts each major part should be 
  divided into after Part 1 compression.

Output:
- After both compressions, return the processed string.

Examples:
Example 1:
Input:
  str = "stripe.com/payments/checkout/customer.john.doe"
  minor_parts = 2
Part 1 Compression:
  => s4e.c1m/p6s/c6t/c6r.j2n.d1e
Part 2 Compression:
  => s4e.c1m/p6s/c6t/c6r.j5e"

Example 2:
Input:
  str = "www.api.stripe.com/checkout"
  minor_parts = 3
Part 1 Compression:
  => w1w.a1i.s4e.c1m/c6t
Part 2 Compression:
  => w1w.a1i.s7m/c6t
"""

class URLShortener:

    def __init__(self) -> None:
        pass

    def shorten(self, url: str, minor_parts: int) -> str:
        major_parts = url.split('/')
        shortened_url = []
        for part in major_parts:
            shortened_url.append(self._shortened(major_part=part, max_parts=minor_parts))
        return "/".join(shortened_url)

    def _shortened(self, major_part: str, max_parts: int) -> str:
        minor_parts = major_part.split('.')
        res = []

        initial, last = [], ""

        if len(minor_parts) > max_parts:
            initial = minor_parts[:max_parts - 1]
            last = "".join(minor_parts[max_parts - 1:])
        else:
            initial = minor_parts

        for part in initial:
            if len(part) == 1:
                res.append(part)
            else:
                res.append(f"{part[0]}{len(part) - 2}{part[-1]}")

        if last:
            if len(last) == 1:
                res.append(part)
            else:
                res.append(f"{last[0]}{len(last) - 2}{last[-1]}")
        
        return ".".join(res)
        


if __name__ == "__main__":
    inputs = [("stripe.com/payments/checkout/customer.john.doe", 2), ("www.api.stripe.com/checkout", 3), ("abc.c.com/payment/a/b/c", 1)]
    shortener = URLShortener()
    for url, minor_parts in inputs:
        print(shortener.shorten(url=url, minor_parts=minor_parts))
