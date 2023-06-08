ef full_chain():

    data = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    response = app.response_cla