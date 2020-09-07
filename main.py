# coding=utf-8
import os
import logging
from ethernodes import Ethernodes

PEERS_FILE_PATH = os.environ.get('PEERS_FILE_PATH', '/tmp/geth-nodes-list-builder/peers.txt')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    en = Ethernodes()
    en.make_peers_file(PEERS_FILE_PATH)
    logging.info('File {} created'.format(PEERS_FILE_PATH))
