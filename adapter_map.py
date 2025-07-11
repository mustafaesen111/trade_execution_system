python
from adapters.fidelity_adapter import FidelityAdapter
from adapters.robinhood_adapter import RobinhoodAdapter
from adapters.questrade_adapter import QuestradeAdapter
from adapters.td_adapter import TDAdapter
from adapters.midas_adapter import MidasAdapter
from adapters.ibkr_adapter import IBKRAdapter

adapter_map = {
    'Fidelity': FidelityAdapter,
    'Robinhood': RobinhoodAdapter,
    'Questrade': QuestradeAdapter,
    'TD': TDAdapter,
    'Midas': MidasAdapter,
    'IBKR': IBKRAdapter
}
