from uniswap import Uniswap
address = "0x0000000000000000000000000000000000000001"         
private_key = None  
PROVIDER = "https://mainnet.infura.io/v3/PRIVATE-KEY"

uniswap_wrapper = Uniswap(address, private_key, provider=PROVIDER, version=2)  
eth_c = "0x0000000000000000000000000000000000000000"
bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
dai = "0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359"
usdt = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
uni = "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984"

dai_rate = uniswap_wrapper.get_eth_token_input_price(dai, 5*10**18)
bat_rate = uniswap_wrapper.get_eth_token_input_price(bat, 1*10**18)

print(dai_rate)
print(bat_rate)

conversion = ((1/bat_rate) * (dai_rate / 10 ** 6)) * (10 ** 18)
print(conversion)
print('${:,.2f}'.format(conversion))