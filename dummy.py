from prefect import flow, get_run_logger
from tiled.client import from_uri


@flow
def handle_uri(uri="https://tiled.nsls2.bnl.gov"):
    client = from_uri(uri)
    logger = get_run_logger()
    logger.info(list(client))
