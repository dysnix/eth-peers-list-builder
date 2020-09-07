# eth-peers-list-builder

This resource uses www.ethernodes.org to prepare a list of working,
synchronized ethereum peers, which is needed to speed up the synchronization of 
an Ethereum node immediately after starting.

## Env config variables

* `PEERS_FILE_PATH` - indicates where the resulting file will be located

## Geth command start

Please add this command to geth start script:

    cat /tmp/geth-nodes-list-builder/peers.txt | while read peer; do geth attach --exec "admin.addPeer('$peer')"; done