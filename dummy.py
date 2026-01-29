from prefect import flow, get_run_logger
from tiled.client import from_uri
from prefect.blocks.system import Secret

@flow
def handle_uri(uri="https://tiled.nsls2.bnl.gov"):
    tiled_api_key = Secret.load("TILED_API_KEY")
    api_key_value = tiled_api_key.get()
    
    client = from_uri(uri, api_key=api_key_value)
    logger = get_run_logger()
    logger.info(list(client))
