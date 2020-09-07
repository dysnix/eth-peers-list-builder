# coding=utf-8
import os
from ethernodes import Ethernodes

PEERS_FILE_PATH = os.environ.get('PEERS_FILE_PATH', '/tmp/geth-nodes-list-builder/peers.txt')

if __name__ == '__main__':
    en = Ethernodes()
    en.make_peers_file(PEERS_FILE_PATH)
