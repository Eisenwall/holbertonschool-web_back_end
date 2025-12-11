#!/usr/bin/env python3
"""
Cleaned-up main file for testing get_hyper_index
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()
server.indexed_dataset()

# --- Test 1: Out of range ---
try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print("AssertionError raised when out of range")

# Initial parameters
index = 3
page_size = 2

print("Nb items:", len(server._Server__indexed_dataset))

# --- Test 2: First request ---
res = server.get_hyper_index(index, page_size)
print(res)

# --- Test 3: Request using next_index ---
res_next = server.get_hyper_index(res["next_index"], page_size)
print(res_next)

# --- Test 4: Delete the first returned index ---
del server._Server__indexed_dataset[res["index"]]
print("Nb items:", len(server._Server__indexed_dataset))

# --- Test 5: Request again initial index (should return different items) ---
print(server.get_hyper_index(index, page_size))

# --- Test 6: Request again initial next_index (same as request 3) ---
print(server.get_hyper_index(res["next_index"], page_size))
