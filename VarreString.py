pos = 0
request = "GET /docs/index.html HTTP/1.1"
pos = pos + request.find(" ")
method = request[0:pos]
print(method)
