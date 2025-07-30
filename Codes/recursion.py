'''
In Recursion, a function calls itself repeatedly.
Each recursive call works on a smaller or simpler subproblem,
 and the process continues until it reaches a base case,
 which stops the recursion


Recursive Case

The part of the function where it calls itself on a smaller/simpler input.

Base Case

A condition that stops the recursion to prevent infinite loops.
'''

#factorial using recursion


# def factorial(n):
#     #Base Case
#
#     if n==0:
#         return 1
#
#     #Recursive case
#
#     else:
#         return  n * factorial(n-1)
#
#
# print(factorial(10))



#fibonacci series

# def fibonacci(n):
#     if n==0:
#         return 0
#
#     elif n==1:
#         return 1
#
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# print(fibonacci(6))


import requests
from bs4 import BeautifulSoup

def crawl(url, depth):
    if depth == 0:
        return

    try:
        response=requests.get(url)
        soup = BeautifulSoup(response.text ,"html.parser")

        print("Visited:", url)

        for link in soup.find_all("a", href=True):
            new_url = link['href']

            if new_url.startswith("http"):
                crawl(new_url, depth-1)



    except:
        pass



crawl("https://www.perplexity.ai/search/what-is-the-contribution-for-f-8Sn_JfqXRTuBnTXlShr3KA", 2)
