#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
# def eating_cookies(n, cache=None):
  
#   if n < 0 :
#     return 0

#   if n == 0:
#     return 1
  
#   while n >= 1:
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

def eating_cookies(n, cache=None):
  
  if cache and n in cache:
    return cache[n]
  
  if n < 0:
    cache[n] = 0
    return cache[n]

  if n == 0:
    cache[n] = 1
    return cache[n]

  # if n >= 1:
  #   cache[n] = n
  #   return n
  
  n_1 = eating_cookies(n-1, cache)
  n_2 = eating_cookies(n-2, cache)
  n_3 = eating_cookies(n-3, cache)
  cache[n] = n_1 + n_2 + n_3
  return n_1 + n_2 + n_3

print(eating_cookies(4))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

# WHAT WE KNOW:
# we are trying to find out how many ways the total amount of cookies can be eaten.
# we know that the total is n
# we know that he can only eat either 0, 1, 2, or 3 cookies at a time.

# BASE CODE:
# we know that if there is 0 cookies, cookie monster has the option to eat 0 cookies, so he would actually have 1 way of eating 0 cookies.
# if there is no cookies then cokie monster cant eat anything, thus have 0 ways of eating 0 cookies


# How the recursion works: eating_cookies(4) would return 7
#                                                                                                   f(4)
#                                                                                       /             |                 \
#                                                                                     f(3)           f(2)             f(1)
#                                                                                  /   |   \       /   |   \        /   |   \
#                                                                               f(2)  f(1)  1    f(1)  1    0      1    0    0         
#                                                                     /   |   \    /   |   \   /   |   \
#                                                                  f(1)   1   0   1    0    0  1   0    0               
#                                                               /   |   \
#                                                              1    0    0