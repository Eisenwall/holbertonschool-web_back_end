#!/usr/bin/env python3
"""
Cleaned-up main file for testing get_hyper_index
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()
server.indexed_dataset()
try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print("AssertionError raised when out of range")
index = 3
page_size = 2

print("Nb items:", len(server._Server__indexed_dataset))
res = server.get_hyper_index(index, page_size)
print(res)
res_next = server.get_hyper_index(res["next_index"], page_size)
print(res_next)
del server._Server__indexed_dataset[res["index"]]
print("Nb items:", len(server._Server__indexed_dataset))
print(server.get_hyper_index(index, page_size))
print(server.get_hyper_index(res["next_index"], page_size))
