from generator import *


def add_loglines_to_file(file_name, n):
    f = open(file_name, "a")
    for i in range(n):
        logline = generate_logline()
        while len(logline) > 280:
            logline = generate_logline()
        f.write(logline + '\n')
    f.close()

add_loglines_to_file('results.txt', 5)
    

