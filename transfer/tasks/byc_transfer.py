from web3 import Web3
import json
import logging
from requests.exceptions import RequestException
from web3.exceptions import Web3Exception
from transfer.models import TransferEvent

logger = logging.getLogger('django')

INFURA_URL = 'https://mainnet.infura.io/v3/553b3db346a24efb8d042f726c730cd6'
WSS_INFURA_URL = 'wss://mainnet.infura.io/ws/v3/553b3db346a24efb8d042f726c730cd6'
BAYC_ADDRESS = '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'
END_BLOCK_RANGE = 200000
BYC_ABI = """ 
    [
        {
        "anonymous": false,
        "inputs": [
            { "indexed": true, "name": "from", "type": "address" },
            { "indexed": true, "name": "to", "type": "address" },
            { "indexed": true, "name": "tokenId", "type": "uint256" }
        ],
        "name": "Transfer",
        "type": "event"
        }
    ]
"""


def fetch_and_save_transfer_byc_events():
    try:
        web3 = Web3(Web3.HTTPProvider(INFURA_URL))
        bayc_abi = json.loads(BYC_ABI)

        bayc_contract = web3.eth.contract(address=BAYC_ADDRESS, abi=bayc_abi)

        END_BLOCK = web3.eth.block_number
        START_BLOCK = END_BLOCK - END_BLOCK_RANGE

        logger.info('Fetching past transfer events...')

        try:
            event_filter = bayc_contract.events.Transfer.create_filter(
                from_block=START_BLOCK,
                to_block=END_BLOCK
            )

            events = event_filter.get_all_entries()

            for event in events:
                from_address = event['args']['from']
                to_address = event['args']['to']
                token_id = event['args']['tokenId']
                transaction_hash = event['transactionHash'].hex()
                block_number = event['blockNumber']

                transfer_event, created = TransferEvent.objects.update_or_create(
                    transaction_hash=transaction_hash,
                    defaults={
                        'token_id': token_id,
                        'from_address': from_address,
                        'to_address': to_address,
                        'block_number': block_number,
                        'contract_address': BAYC_ADDRESS
                    }
                )

                if created:
                    logger.info(f'Saved TransferEvent: {transaction_hash}')
                else:
                    logger.info(
                        f'TransferEvent already exists: {transaction_hash}')

        except Web3Exception as w3e:
            logger.error('Web3 error occurred: %s', w3e)
        except RequestException as reqe:
            logger.error('Network error occurred: %s', reqe)
        except Exception as e:
            logger.error('Error fetching events: %s', e)

    except Exception as e:
        logger.error('Error initializing Web3: %s', e)


def listen_for_live_transfer_events():
    try:
        web3 = Web3(Web3.LegacyWebSocketProvider(WSS_INFURA_URL))
        ayc_abi = json.loads(BYC_ABI)

        bayc_contract = web3.eth.contract(address=BAYC_ADDRESS, abi=ayc_abi)

        event_filter = bayc_contract.events.Transfer.create_filter(
            from_block='latest')

        logger.info('Listening for live Transfer events...')

        while True:
            try:
                for event in event_filter.get_new_entries():
                    from_address = event['args']['from']
                    to_address = event['args']['to']
                    token_id = event['args']['tokenId']
                    transaction_hash = event['transactionHash'].hex()
                    block_number = event['blockNumber']

                    transfer_event, created = TransferEvent.objects.update_or_create(
                        transaction_hash=transaction_hash,
                        defaults={
                            'token_id': token_id,
                            'from_address': from_address,
                            'to_address': to_address,
                            'block_number': block_number,
                            'contract_address': BAYC_ADDRESS
                        }
                    )

                    if created:
                        logger.info(f'Saved TransferEvent: {transaction_hash}')
                    else:
                        logger.info(
                            f'TransferEvent already exists: {transaction_hash}')

            except Web3Exception as w3e:
                logger.error('Web3 error while fetching new entries: %s', w3e)
            except Exception as e:
                logger.error('Error retrieving new entries: %s', e)

    except Exception as e:
        logger.error('Error setting up event listening: %s', e)
