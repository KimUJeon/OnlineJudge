import sys

winners = ["ITMO", "SPbSU", "SPbSU", "ITMO", "ITMO",
                               "SPbSU", "ITMO", "ITMO", "ITMO", "ITMO",
                               "ITMO", "PetrSU, ITMO", "SPbSU", "SPbSU",
                               "ITMO", "ITMO", "ITMO", "ITMO", "SPbSU",
                               "ITMO", "ITMO", "ITMO", "ITMO", "SPbSU", "ITMO"
           ]

init_year = 1995
year = int(sys.stdin.readline().rstrip())
gap_year = year - init_year


print(winners[gap_year])