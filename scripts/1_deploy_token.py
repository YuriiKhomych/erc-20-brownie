from brownie import accounts, config, TokenERC20
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

initial_supply = 1000000000000000000
token_name = "TOKEN"
token_symbol = "TKN"

gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)
gas_price(gas_strategy)


def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = TokenERC20.deploy(
        initial_supply,
        token_name,
        token_symbol,
        {"from": account, "gas_price": gas_strategy},
        publish_source=True,
    )
    print(erc20)
