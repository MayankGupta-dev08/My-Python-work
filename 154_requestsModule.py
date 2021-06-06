'''Requests Module For HTTP Requests
Requests library is one of the integral part of Python for making HTTP requests to a specified URL. Whether it be REST APIs or Web Scrapping, requests is must to be learned for proceeding further with these technologies. When one makes a request to a URI, it returns a response. Python requests provides inbuilt functionalities for managing both the request and response.

Why??
    To play with web, Python Requests is must. Whether it be hitting APIs, downloading entire facebook pages, and much more cool stuff, one will have to make a request to the URL.
    Requests play a major role is dealing with REST APIs, and Web Scrapping.

How??
    Python requests module has several built-in methods to make Http requests to specified URI using GET, POST, PUT, PATCH or HEAD requests. A Http request is meant to either retrieve data from a specified URI or to push data to a server. It works as a request-response protocol between a client and a server.

Http Request Methods –
Method	Description
GET	    GET method is used to retrieve information from the given server using a given URI.
POST	POST request method requests that a web server accepts the data enclosed in the body of the request message, most likely for storing it
PUT	    The PUT method requests that the enclosed entity be stored under the supplied URI. If the URI refers to an already existing resource, it is modified and if the URI does not point to an existing resource, then the server can create the resource with that URI.
DELETE	The DELETE method deletes the specified resource
HEAD	The HEAD method asks for a response identical to that of a GET request, but without the response body.
PATCH	It is used for modify capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource
'''


import requests # import requests module

# 1.    Making a get request
response = requests.get('https://api.github.com/')
print(response.url) # print request object
print(response.status_code, "\n") # print status code - 200 means success.


# 2.    Make a request to a web page, and print the response text:
x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)


# 3.    just an Example of post request
# url2 = "www.someurl.com"
# data = {"p1": 4, "p2":8}
# response2 = requests.post(url = url2, data = data)