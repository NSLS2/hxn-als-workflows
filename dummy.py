from prefect import flow, get_run_logger
from prefect.blocks.system import Secret
from tiled.client import from_profile


@flow
def handle_uri(uri="https://tiled.nsls2.bnl.gov"):
    logger = get_run_logger()
    logger.info(f"URI: {uri}")
