from brownie import accounts, EasyToken
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

initial_supply = 1000000000000000000
gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)
gas_price(gas_strategy)


def main():
    account = accounts[0]
    erc20 = EasyToken.deploy(
        initial_supply,
        {"from": account, "gas_price": gas_strategy},
    )
    print(erc20)
