import  data_conn

def get_userid_keySecret(user_id):
    str="select userId,apiKey,apiSecret from api_key_auths where userid=" +repr(user_id)
    return str

#print(get_userid_keySecret(99000))


def get_username(user_id):
    str="select userId,email from user_profiles where userid=" +repr(user_id)
    return str

def get_usersigin(email):
    str="select email,code from registration_requests where email=" +repr(email)
    return str


def get_orders_trades():
    str="select orderid, symbol, message from match_message_store"
    return str
def K_line(amount,price,createAt,symbol,orderid):
      str="INSERT INTO K_line (amount,price,createAt,symbol,orderid) VALUES ( "+repr(amount)+", "+ repr(price) +","+repr(createAt)+",'" + symbol+ "'," + repr(orderid)+");"
      return(str)
#print(K_line(1,2,34,'fdf',232))