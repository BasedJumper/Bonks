import robin_stocks as r
import pyotp

#info from  robinhood
totp = pyotp.TOTP("your key").now()
login = r.login('username','password', mfa_code=totp)
ask_price=[]
bid_price=[]
crypto="DOGE"
startingprice= float(r.get_crypto_quote(crypto,"ask_price"))
startingamountmoney =float(r.load_account_profile("cash"))
dogeamout=r.get_crypto_positions("quantity")
starrtamontofcrypto =float(dogeamout[0])
buyamount=1
sellamount=1

def buy(crypto,amountofcrypto,price):
	r.order_buy_crypto_limit(crypto,amountofcrypto,price)

def sell(crypto,orderamount,priceofcrypto):
	r.order_sell_crypto_limit(crypto, orderamount, priceofcrypto, timeInForce='gtc')



