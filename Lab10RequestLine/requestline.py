"""
|-------------------------------------------------------------------------------
| requestline.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Nov 19, 2019
|
| This program determines the validity of an HTTP request line.
|
"""

def parse(line):
    # YOUR CODE HERE
    if line.startswith("GET"):
        if line[line.find(" ")+1:line.find(" ", 4)].startswith("/"):
            if '"' not in line[line.find(" ")+1:line.find(" ", 4)]:
                if line.endswith("HTTP/1.1"):
                    t = line[line.find(" ")+1:line.find(" ", 4)]
                else:
                    t = "505 HTTP Version Not Supported"
            else:
                t = "400 Bad Request"
        else:
            t = "501 Not Implemented"
    else:
        t = "405 Method Not Allowed"
    return t

result = parse("GET /hello.html HTTP/1.1")
print(result)

