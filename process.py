log_file = open("um-server-01.txt")
"""stores to a variable the file containing sales data"""

def generate_sales_reports(log_file): """defining the function"""
    for line in log_file:             """goes through each line in the file"""
        line = line.rstrip()          """removes unecessary empty space"""
        day = line[0:3]               """for each line in log, slices the first three and assigns to day"""
        if day == "Mon":              """if those characters = mon"""
            print(line)               """prints corresponding line"""


generate_sales_reports(log_file)      """calls function passing in log_file as an argument"""
