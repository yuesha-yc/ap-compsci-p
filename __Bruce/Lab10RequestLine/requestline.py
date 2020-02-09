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
    sp = []
    if line.startswith("GET"):
        sp = line.split(" ")
        if sp[1].startswith("/"):
            if sp[1].find("\"") == -1:
                if sp[2] == "HTTP/1.1":
                    return sp[1]
                else: return "505 HTTP Version Not Supported"
            else: return "400 Bad Request"
        else: return "501 Not Implemented"
    else: return "405 Method Not Allowed"

result = parse("GET /hello.html HTTP/1.1")
print(result)

