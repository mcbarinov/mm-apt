import pytest
from mm_std import get_dotenv


@pytest.fixture
def mainnet_rpc_url() -> str:
    return get_dotenv("MAINNET_RPC_URL")
