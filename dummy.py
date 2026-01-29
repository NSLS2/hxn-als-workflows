from prefect import flow, get_run_logger
from tiled.client import from_uri
from prefect.blocks.system import Secret

@flow
def handle_uri(uri_in="https://tiled.nsls2.bnl.gov", uri_out="https://tiled.nsls2.bnl.gov"):
    tiled_api_key = Secret.load("tiled-synaps-api-key")
    api_key_value = tiled_api_key.get()
    
    reader = from_uri(uri_in, api_key=api_key_value)
    writer = from_uri(uri_out, api_key=api_key_value)
    
    writer.write_array(reader.read(), access_tags=['tst_sandbox'])

    logger = get_run_logger()
    logger.info(list(writer))
