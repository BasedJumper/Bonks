import robin_stocks as r
import pyotp

#account info from  robinhood
totp = pyotp.TOTP("your key").now()

login = r.login('username','password', mfa_code=totp)


ask_price=[]

bid_price=[]

#only trading doge at the moment 
crypto="DOGE"

#doges price when we started trading 
startingprice= float(r.get_crypto_quote(crypto,"ask_price"))

#our account balance 
startingamountmoney =float(r.load_account_profile("cash"))

#the amout of doge we own 
dogeamout=r.get_crypto_positions("quantity")

starrtamontofcrypto =float(dogeamout[0])

#trading scale 
buyamount=1
sellamount=1

run = True


# buy using the RH API
def buy(crypto,amountofcrypto,price):
	r.order_buy_crypto_limit(crypto,amountofcrypto,price)
#sell using the Rh API
def sell(crypto,orderamount,priceofcrypto):
	r.order_sell_crypto_limit(crypto, orderamount, priceofcrypto, timeInForce='gtc')

while run:
	currentprice = float(r.get_crypto_quote(crypto,"ask_price"))
	print("start_price:"+str(startingprice))
	print("current_price:"+str(currentprice))
	print("cash:"+str(startingamountmoney))
	print("amount:"+str(starrtamontofcrypto))



