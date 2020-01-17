import time
from win32timezone import now
import test



if __name__ == '__main__':
    # { "apiKey": "AAAADAVYcB2SNK5wFIAMHA2E", "apiSecret": "brE72wUEpAt0Cz7i" },
    #"AAAADAVYcB2SNK5wFIAMHA2E", "brE72wUEpAt0Cz7i"
    #print("test");
    #交易部分
    #client =  test.ApiClient( "AAAADAVYcB2SNK5wFIAMHA2E", "brE72wUEpAt0Cz7i","",True, 10,False);
    #ui
    #client =  test.ApiClient( "75fdcedbc25e1f91a353fe183fe775a365a5e802", "80dd128ba3d1ff944616588fb32bec54f6e6160a","",True, 10,False);
    #wallet
    client =  test.ApiClient( "f390a3fbdacb3e1c9ee7408c838e2a806060c540", "72098785c599f797eb8905b95f920d2ef05ed1ca","",True, 10,False);
    print(client.get("/v1/user/withdraw/records"))
    #后端管理
    #client =  test.ApiClient( "751b5905607b127c80040a8fcfe72c194390d7b1", "2ce8b02733c93901ce0a709877339c86fcbb5b73","",True, 10,False);
    #print(client.post("/ui/users/99005/withdraw/requests/100002/cancel",""))
    #{'result': True}
    #str='{"status": "success","data":'+client.get( "/v1/trade/fee/ETH_BTC")+'}'
    #print(str)
    #print(client.post("/ui/users/{userId}/withdraw/addresses",{"address":"AES:00000000000182bdf74eab9e4a067a8d649dd05106d0fa285dc096dcd5b2ea7c24a8791e7947918332efbedebaf57ee121b28ba4eb881148a1f491638f70e1d64ee00af183357a38","currency":"ETH","description":"test"}))
    #print(client.get("/ui/users/99005/withdraw/requests"))
    #{'requests': [{'id': 100001, 'createdAt': 1553772413790, 'updatedAt': 1553778277007, 'status': 'PROCESSING', 'errorCode': '', 'errorMessage': '', 'currency': 'ETH', 'userId': 99005, 'encryptedToAddress': 'AES:00000000000182bdf74eab9e4a067a8d649dd05106d0fa285dc096dcd5b2ea7c24a8791e7947918332efbedebaf57ee121b28ba4eb881148a1f491638f70e1d64ee00af183357a38', 'amount': 0.1, 'withdrawFee': 0.0001, 'tx': '', 'toAddress': '0xE429143ac1bbE667473DFd060C7eee4c1e5CA96e', 'cancellable': False}]}
    #withdrawAddAddressByUser
    #print(client.post("/ui/users/99005/withdraw/addresses",{"address":"0xb7d1d095349fb1d13e127e2c11c6c73f158724d0","currency":"ETH","description":""}))
    #{'id': 100002, 'createdAt': 1553838017286, 'userId': 99005, 'currency': 'ETH', 'addressHash': 'd91bde1b0e51e3b73af17e47b5706855539982ba66aaab865cb6c6c222805253', 'description': '', 'address': '0xb7d1d095349fb1d13e127e2c11c6c73f158724d0'}
    #withdrawCreateRequest
    #print(client.post("/ui/users/99005/withdraw/requests",{"amount":0.2,"currency":"ETH","withdrawAddressId":100001}))
    #{'id': 100002, 'createdAt': 1553845495952, 'updatedAt': 1553845495952, 'status': 'SUBMITTED', 'errorCode': '', 'errorMessage': '', 'currency': 'ETH', 'userId': 99005, 'encryptedToAddress': 'AES:00000000000182bdf74eab9e4a067a8d649dd05106d0fa285dc096dcd5b2ea7c24a8791e7947918332efbedebaf57ee121b28ba4eb881148a1f491638f70e1d64ee00af183357a38', 'amount': 0.2, 'withdrawFee': 0.0002, 'tx': '', 'toAddress': '0xE429143ac1bbE667473DFd060C7eee4c1e5CA96e', 'cancellable': True}
    #print(client.post("/ui/users/99000/unlock",{"amount":2.01,"currency":"ETH"}))
    #print(client.get("/json/register/activate"))
    #print(client.post("/json/register",{"email":"zangyirong@dae.org","lang":"","name":"zangyirong","password":"123456zang"}))
    #print(client.post("/signin",{"email":"bot0@example.com","ga":"","next":"","password":"17ca2c39e340048b1d9afa8b2bdb77407cc698343e30b58b09e19a4995fc44af"}));
    #创建订单
    #print(client.post( "/v1/trade/orders",{"type":"BUY_LIMIT","symbol":"BTC_USDT","price":"1","amount":"100","fillOrKill":False,"immediateOrCancel":False,"hidden":False,"postOnly":False}));

    #print(client.post("/ui/users/1001/withdraw/requests",{"amount": 0.01,"createdAt": 1553325364858,"currency": "USDT","encryptedToAddress": "0xb7d1d095349fb1d13e127e2c11c6c73f158724d0",	"id": 1,"withdrawFee": 0.01}))
    #print(client.post("/ui/users/99000/withdraw/requests",{"limit":100,"currency": "USDT"}))
    #print(client.post("/ui/users/99000/withdraw/addresses/100000/delete",{}))

    ################
    #钱包相关数据
    #depositGetMaxBipIndex
    #print(client.get("/wallet/deposits/ETH/addresses/maxIndex"))
    #{'max': 1}
    #getTradesForRemoteSymbolLoader
    #print(client.get("/wallet/trades"))
    #{'symbols': [{'id': 100000, 'createdAt': 1553189225736, 'updatedAt': 1553189225736, 'baseName': 'BTC', 'quoteName': 'USDT', 'baseScale': 8, 'quoteScale': 4, 'baseMinimum': 0.01, 'quoteMinimum': 0.01, 'startTime': 0, 'endTime': 5000000000000, 'sequenceIndex': 1, 'displayOrder': 0, 'meta': '', 'name': 'BTC_USDT'}, {'id': 100004, 'createdAt': 1553189225737, 'updatedAt': 1553189225737, 'baseName': 'CFC', 'quoteName': 'BTC', 'baseScale': 4, 'quoteScale': 4, 'baseMinimum': 0.01, 'quoteMinimum': 0.01, 'startTime': 0, 'endTime': 5000000000000, 'sequenceIndex': 0, 'displayOrder': 0, 'meta': '', 'name': 'CFC_BTC'}, {'id': 100003, 'createdAt': 1553189225737, 'updatedAt': 1553189225737, 'baseName': 'CFC', 'quoteName': 'ETH', 'baseScale': 4, 'quoteScale': 4, 'baseMinimum': 0.01, 'quoteMinimum': 0.01, 'startTime': 0, 'endTime': 5000000000000, 'sequenceIndex': 0, 'displayOrder': 0, 'meta': '', 'name': 'CFC_ETH'}, {'id': 100005, 'createdAt': 1553189225737, 'updatedAt': 1553189225737, 'baseName': 'CFC', 'quoteName': 'USDT', 'baseScale': 4, 'quoteScale': 4, 'baseMinimum': 0.01, 'quoteMinimum': 0.01, 'startTime': 0, 'endTime': 5000000000000, 'sequenceIndex': 0, 'displayOrder': 0, 'meta': '', 'name': 'CFC_USDT'}, {'id': 100002, 'createdAt': 1553189225737, 'updatedAt': 1553189225737, 'baseName': 'ETH', 'quoteName': 'BTC', 'baseScale': 4, 'quoteScale': 4, 'baseMinimum': 0.01, 'quoteMinimum': 0.01, 'startTime': 0, 'endTime': 5000000000000, 'sequenceIndex': 3, 'displayOrder': 0, 'meta': '', 'name': 'ETH_BTC'}, {'id': 100001, 'createdAt': 1553189225737, 'updatedAt': 1553189225737, 'baseName': 'ETH', 'quoteName': 'USDT', 'baseScale': 4, 'quoteScale': 4, 'baseMinimum': 0.01, 'quoteMinimum': 0.01, 'startTime': 0, 'endTime': 5000000000000, 'sequenceIndex': 2, 'displayOrder': 0, 'meta': '', 'name': 'ETH_USDT'}], 'currencies': [{'id': 100000, 'createdAt': 1553189225736, 'name': 'BTC', 'legal': False, 'addressAliasTo': '', 'encryptedXpubKey': 'AES:ee92a633f0f5fa5430fb82d2fbe06ec6db6bb64743b970b664de1525833b959fbf7222f6416191dfb469ebec1260c607b89c7a5797594dcae905f62a2838d0d970ee35fc1201e3ceaec8598b3edaa07ec4a1aaac71f25acd32315dba5c532dd58c9548e0341af549e274e0ed3286f793c00c5adc70195ac81550a9ca32c75849fc11a09200127b29', 'token': False, 'tokenContractAddress': '', 'tokenDecimals': 0, 'tokenIssuesOn': '', 'depositEnabled': True, 'withdrawEnabled': True, 'meta': '', 'xpubKey': 'xpub6FNwEcVr6n9GHEwbyrStEFi3S894TAB3k28CrFvPhoCaDbgXvYcv1KyqruTVSnQjtEUkxKeMYvcncaEmdD94oQvLXc4JKQCdpeJGv3hPTi1'}, {'id': 100001, 'createdAt': 1553189225736, 'name': 'LTC', 'legal': False, 'addressAliasTo': '', 'encryptedXpubKey': 'AES:6386f400c15406a2676e720758b4160a616ce5fc8b7fe98bab707e4eeea857d98b4b60e9c2d2ffbd2c71314bebafd0f3467a851592437a75d0fd609b6e9cab02c7eb62a654dae2691a4c9d6d76a95f8ba382e45c2424ca20589df55c0c19240a965376c16dbb57336a811f979b0adbad595f1604400a41ae8032678f42212446c52ba6d383fdfc22', 'token': False, 'tokenContractAddress': '', 'tokenDecimals': 0, 'tokenIssuesOn': '', 'depositEnabled': True, 'withdrawEnabled': True, 'meta': '', 'xpubKey': 'xpub6EfWzViWEYD8JfDstygWnDGTsT8Jb4Rdi1kPsbefnaLQxvc95kttHtRGdHp9HNtvHhLEj186Ai2328KLJb784R3QVubQB5nni85MdRdyf2f'}, {'id': 100002, 'createdAt': 1553189225737, 'name': 'ETH', 'legal': False, 'addressAliasTo': '', 'encryptedXpubKey': 'AES:a1a6e98fd96ae0f9d72c4587228786a417911d515ce70661b1866a930e5ecebf0231c705beb3424cf23fa65b57a0ed2abfc01cc56e9cd6560fb7a2bd51e28a01f98e63039ad9acaf9177411d5d209bf188947448fa00acea4d233cdcc8d80456fec8879575268121cf6a2196268114b77dfb2fa09c934f39d7aa66e45c9683c88854edb4024792ca', 'token': False, 'tokenContractAddress': '', 'tokenDecimals': 0, 'tokenIssuesOn': '', 'depositEnabled': True, 'withdrawEnabled': True, 'meta': '', 'xpubKey': 'xpub6FA7JevWzZM37Cqp9VWDnUwkwYGZSYoN6yxJKY16mD7cNvqaNWf9Mj4X4RYZDVVRfJrHP3QTSxw4m6ViiG1nUevfe4pbWtGM5oTv4tsgf7z'}, {'id': 100003, 'createdAt': 1553189225737, 'name': 'USDT', 'legal': False, 'addressAliasTo': 'BTC', 'encryptedXpubKey': '', 'token': True, 'tokenContractAddress': 'omni:31', 'tokenDecimals': 8, 'tokenIssuesOn': 'BTC', 'depositEnabled': True, 'withdrawEnabled': True, 'meta': '', 'xpubKey': ''}, {'id': 100004, 'createdAt': 1553189225737, 'name': 'CFC', 'legal': False, 'addressAliasTo': 'ETH', 'encryptedXpubKey': '', 'token': True, 'tokenContractAddress': '0x97dd6c78263aed33a28927243cc749952703b92f', 'tokenDecimals': 18, 'tokenIssuesOn': 'ETH', 'depositEnabled': True, 'withdrawEnabled': True, 'meta': '', 'xpubKey': ''}]}
    #depositGetLogsByOffsetId --未调成功
    #print(client.get("/v1/trade/orders",limit="100",symbol='ETH_USDT',offsetId=0))
    #{'deposits': [{'id': 100001, 'createdAt': 1553758584863, 'updatedAt': 1553758584887, 'status': 'PENDING', 'userId': 99005, 'currency': 'ETH', 'uniqueId': '0x908731f06f32f3b45f012add4f8791ff16133a6b811a1a9a4b54955189999c28#0x54051947fcda210ce8991119a8699664786582e5b9b1838e158e2778b3978fe2', 'amount': 0.11, 'shouldAudit': False, 'confirms': 6464, 'minimumConfirms': 50, 'toAddress': '0x605e8c8fb630afc5c4d2d11b8fc1121131facd21'}]}
    #withdrawGetRequestsForWallet
    #print(client.get("/wallet/withdraws",currency="ETH"))
    #{'requests': [{'id': 100001, 'currency': 'ETH', 'encryptedToAddress': 'AES:00000000000182bdf74eab9e4a067a8d649dd05106d0fa285dc096dcd5b2ea7c24a8791e7947918332efbedebaf57ee121b28ba4eb881148a1f491638f70e1d64ee00af183357a38', 'amount': 0.1, 'withdrawFee': 0.0001, 'createdAt': 1553772413790}]}

    #depositVirtualCurrency?????
    #print(client.post("/wallet/deposits",{"action":"DEPOSIT","amount":0.1,"bipIndex":1,"confirms":6464,"currency":"ETH","encryptedToAddress":"AES:00000000000000015b57f723786bf40772ae60b317cf3a9f100dd4ad221af27889a06162e3ab1e071feae4505754a04cf0c07175837107912ff90f68a1349c46cc76728f95204743","shouldAudit":True,"uniqueId":""}))
    #print(client.post("/wallet/deposits",{"action":"DEPOSIT","amount":0.1,"bipIndex":1,"confirms":6464,"currency":"ETH","encryptedToAddress":"AES:00000000000182b8aaadb6a4ae35803e6332e8172cfa469efa80799c40269f5dfb256b571a9b6b5409de1ead3bb700171dfb3f1b1076c17bd518f66f928f08588d30d85554c0c1a0","shouldAudit":True,"uniqueId":""}))
    #withdrawUpdateRequestByWalletStartProcess
    #print(client.post("/wallet/withdraws/100001/process",{}))
    #{'result': True}
    #withdrawUpdateResultByWalletProcessed
    #print(client.post("/wallet/withdraws/100001/result",{"errorCode":"0","errorMessage":"test","success":True,"tx":"","encryptedToAddress":"AES:00000000000182bdf74eab9e4a067a8d649dd05106d0fa285dc096dcd5b2ea7c24a8791e7947918332efbedebaf57ee121b28ba4eb881148a1f491638f70e1d64ee00af183357a38"}))
    #{'result': True}

    #withdrawOnTransactionFee
    #print(client.post("/wallet/withdraws/fee",{"blockHash":"00000000000000aaebd9238c5d15fb6ad155559d490ae926135592ea699e6279","blockHeight":23000,"currency":"BTC","feeAmount":0.002,"feeCurrency":"BTC","tx":"01a4ce7b60e87d83e10b81a8288072fb930c1128aae0520e72a4971380245ce1","uniqueId":0}))
    #{'result': True}


    #accountFreezeUserAccount
    #print(client.post("/manage/account/freeze",{"amount":0.02,"currency":"ETH","flowType":"TRADE_FREEZE","userId":99000}))
    #{'result': 0.02}
    #accountGetByUserAndCurrencyAndType
    #print(client.get("/manage/account/99000/ETH/SPOT_AVAILABLE"))
    #{'id': 100005, 'createdAt': 1553189225436, 'updatedAt': 1554119843855, 'userId': 99000, 'currency': 'ETH', 'type': 'SPOT_AVAILABLE', 'balance': 98499.98}
    #accountGetUserAccounts
    #print(client.get("/manage/account/99000/ETH"))
    #{'accounts': [{'id': 100005, 'createdAt': 1553189225436, 'updatedAt': 1554119843855, 'userId': 99000, 'currency': 'ETH', 'type': 'SPOT_AVAILABLE', 'balance': 98499.98}, {'id': 108016, 'createdAt': 1554119843855, 'updatedAt': 1554119843855, 'userId': 99000, 'currency': 'ETH', 'type': 'SPOT_FROZEN', 'balance': 0.02}, {'id': 108009, 'createdAt': 1553829622804, 'updatedAt': 1553829622804, 'userId': 99000, 'currency': 'ETH', 'type': 'SPOT_LOCKED', 'balance': 0.0}]}

    #accountTransfer
    #print(client.post("/manage/account/transfer",{"amount":0.02,"currency":"ETH","description":"test","flowType":"TRADE_FREEZE","fromAccountId":100005,"fromUserId":99000,"refId":0,"refType":"","toAccountId":100008,"toUserId":99001,"transferType":"AVAILABLE_TO_AVAILABLE"}))
    #{'from': {'id': 100005, 'createdAt': 1553189225436, 'updatedAt': 1554121095552, 'userId': 99000, 'currency': 'ETH', 'type': 'SPOT_AVAILABLE', 'balance': 98499.96}, 'to': {'id': 100008, 'createdAt': 1553189225574, 'updatedAt': 1554121095552, 'userId': 99001, 'currency': 'ETH', 'type': 'SPOT_AVAILABLE', 'balance': 98500.02}}
    #accountUnfreezeUserAccount
    #print(client.post("/manage/account/unfreeze",{"amount":0.02,"currency":"ETH","flowType":"TRADE_FREEZE","userId":99000}))
    #{'result': 0.02}
    #currencyCreate????
    #print(client.post("/manage/currency/create"))

    #currencyDepositGetRules
    #print(client.get("/manage/currency/USDT/deposit/rules"))
    #{'rules': [{'amount': 0.0, 'confirms': 3}]}
    #currencyWithdrawGetRule
    #print(client.get("/manage/currency/USDT/withdraw/rule"))
    #{'minimumAmount': 0.01, 'feeRate': 1.0, 'minimumFee': 0.01, 'maximumFee': 0.01}
    #currencyWithdrawSetRule
    #print(client.post("/manage/currency/ETH/withdraw/rule",{"feeRate":0.01,"maximumFee":0.02,"minimumAmount":0.001,"minimumFee":0.001}))
    #{'result': True}
    #feeGetCurrent
    #print(client.get("/manage/fee/current"))
    #{'fees': [{'currency': 'BTC', 'amount': 0.0}, {'currency': 'CFC', 'amount': 0.0}, {'currency': 'ETH', 'amount': 0.0}, {'currency': 'LTC', 'amount': 0.0}, {'currency': 'USDT', 'amount': 0.0}]}
    #feeRateGetDefaultFeeRate
    #print(client.get("/manage/fee/default"))
    #{'takerFeeRate': 0.002, 'makerFeeRate': 0.001}
    #getTradesForRemoteSymbolLoader
    #print(client.get("/manage/trades"))
    #{'symbols': [{'id': 100000, 'createdAt': 1553189225736, 'updatedAt': 1553189225736, 'baseName': 'BTC', 'quoteName': 'USDT', 'baseScale': 8, 'quoteScale': 4, 'baseMinimum': 0.01, 'quoteMinimum': 0.01, 'startTime': 0, 'endTime': 5000000000000, 'sequenceIndex': 1, 'displayOrder': 0, 'meta': '', 'name': 'BTC_USDT'}, {'id': 100004, 'createdAt': 1553189225737, 'updatedAt': 1553189225737, 'baseName': 'CFC', 'quoteName': 'BTC', 'baseScale': 4, 'quoteScale': 4, 'baseMinimum': 0.01, 'quoteMinimum': 0.01, 'startTime': 0, 'endTime': 5000000000000, 'sequenceIndex': 0, 'displayOrder': 0, 'meta': '', 'name': 'CFC_BTC'}, {'id': 100003, 'createdAt': 1553189225737, 'updatedAt': 1553189225737, 'baseName': 'CFC', 'quoteName': 'ETH', 'baseScale': 4, 'quoteScale': 4, 'baseMinimum': 0.01, 'quoteMinimum': 0.01, 'startTime': 0, 'endTime': 5000000000000, 'sequenceIndex': 0, 'displayOrder': 0, 'meta': '', 'name': 'CFC_ETH'}, {'id': 100005, 'createdAt': 1553189225737, 'updatedAt': 1553189225737, 'baseName': 'CFC', 'quoteName': 'USDT', 'baseScale': 4, 'quoteScale': 4, 'baseMinimum': 0.01, 'quoteMinimum': 0.01, 'startTime': 0, 'endTime': 5000000000000, 'sequenceIndex': 0, 'displayOrder': 0, 'meta': '', 'name': 'CFC_USDT'}, {'id': 100002, 'createdAt': 1553189225737, 'updatedAt': 1553189225737, 'baseName': 'ETH', 'quoteName': 'BTC', 'baseScale': 4, 'quoteScale': 4, 'baseMinimum': 0.01, 'quoteMinimum': 0.01, 'startTime': 0, 'endTime': 5000000000000, 'sequenceIndex': 3, 'displayOrder': 0, 'meta': '', 'name': 'ETH_BTC'}, {'id': 100001, 'createdAt': 1553189225737, 'updatedAt': 1553189225737, 'baseName': 'ETH', 'quoteName': 'USDT', 'baseScale': 4, 'quoteScale': 4, 'baseMinimum': 0.01, 'quoteMinimum': 0.01, 'startTime': 0, 'endTime': 5000000000000, 'sequenceIndex': 2, 'displayOrder': 0, 'meta': '', 'name': 'ETH_USDT'}], 'currencies': [{'id': 100000, 'createdAt': 1553189225736, 'name': 'BTC', 'legal': False, 'addressAliasTo': '', 'encryptedXpubKey': 'AES:ee92a633f0f5fa5430fb82d2fbe06ec6db6bb64743b970b664de1525833b959fbf7222f6416191dfb469ebec1260c607b89c7a5797594dcae905f62a2838d0d970ee35fc1201e3ceaec8598b3edaa07ec4a1aaac71f25acd32315dba5c532dd58c9548e0341af549e274e0ed3286f793c00c5adc70195ac81550a9ca32c75849fc11a09200127b29', 'token': False, 'tokenContractAddress': '', 'tokenDecimals': 0, 'tokenIssuesOn': '', 'depositEnabled': True, 'withdrawEnabled': True, 'meta': '', 'xpubKey': 'xpub6FNwEcVr6n9GHEwbyrStEFi3S894TAB3k28CrFvPhoCaDbgXvYcv1KyqruTVSnQjtEUkxKeMYvcncaEmdD94oQvLXc4JKQCdpeJGv3hPTi1'}, {'id': 100001, 'createdAt': 1553189225736, 'name': 'LTC', 'legal': False, 'addressAliasTo': '', 'encryptedXpubKey': 'AES:6386f400c15406a2676e720758b4160a616ce5fc8b7fe98bab707e4eeea857d98b4b60e9c2d2ffbd2c71314bebafd0f3467a851592437a75d0fd609b6e9cab02c7eb62a654dae2691a4c9d6d76a95f8ba382e45c2424ca20589df55c0c19240a965376c16dbb57336a811f979b0adbad595f1604400a41ae8032678f42212446c52ba6d383fdfc22', 'token': False, 'tokenContractAddress': '', 'tokenDecimals': 0, 'tokenIssuesOn': '', 'depositEnabled': True, 'withdrawEnabled': True, 'meta': '', 'xpubKey': 'xpub6EfWzViWEYD8JfDstygWnDGTsT8Jb4Rdi1kPsbefnaLQxvc95kttHtRGdHp9HNtvHhLEj186Ai2328KLJb784R3QVubQB5nni85MdRdyf2f'}, {'id': 100002, 'createdAt': 1553189225737, 'name': 'ETH', 'legal': False, 'addressAliasTo': '', 'encryptedXpubKey': 'AES:a1a6e98fd96ae0f9d72c4587228786a417911d515ce70661b1866a930e5ecebf0231c705beb3424cf23fa65b57a0ed2abfc01cc56e9cd6560fb7a2bd51e28a01f98e63039ad9acaf9177411d5d209bf188947448fa00acea4d233cdcc8d80456fec8879575268121cf6a2196268114b77dfb2fa09c934f39d7aa66e45c9683c88854edb4024792ca', 'token': False, 'tokenContractAddress': '', 'tokenDecimals': 0, 'tokenIssuesOn': '', 'depositEnabled': True, 'withdrawEnabled': True, 'meta': '', 'xpubKey': 'xpub6FA7JevWzZM37Cqp9VWDnUwkwYGZSYoN6yxJKY16mD7cNvqaNWf9Mj4X4RYZDVVRfJrHP3QTSxw4m6ViiG1nUevfe4pbWtGM5oTv4tsgf7z'}, {'id': 100003, 'createdAt': 1553189225737, 'name': 'USDT', 'legal': False, 'addressAliasTo': 'BTC', 'encryptedXpubKey': '', 'token': True, 'tokenContractAddress': 'omni:31', 'tokenDecimals': 8, 'tokenIssuesOn': 'BTC', 'depositEnabled': True, 'withdrawEnabled': True, 'meta': '', 'xpubKey': ''}, {'id': 100004, 'createdAt': 1553189225737, 'name': 'CFC', 'legal': False, 'addressAliasTo': 'ETH', 'encryptedXpubKey': '', 'token': True, 'tokenContractAddress': '0x97dd6c78263aed33a28927243cc749952703b92f', 'tokenDecimals': 18, 'tokenIssuesOn': 'ETH', 'depositEnabled': True, 'withdrawEnabled': True, 'meta': '', 'xpubKey': ''}]}
    #snapshotGetAll
    #print(client.get("/manage/snapshot/list"))
    #{'snapshots': ['snapshot_spot_accounts_at_2019_04_01_09_06_all']}
    #unreplayExist
    #print(client.get("/manage/exists",uniqueId=100))
    #userGetById
    #print(client.get("/manage/user/99000"))
    #withdrawAutoAudit
    #print(client.post("/manage/withdraw/100001/autoAudit",{"errorCode":0,"errorMessage":"test","status":"WAITING_FOR_APPROVAL"}))
    #{'result': true}
    #withdrawAudit
    #print(client.post("/manage/withdraw/100001/audit/true",{}))
    #{'result': True}
    #userUpdateLevel
    #print(client.post("/manage/users/99000/levels/1",{}))
    #{'id': 99000, 'createdAt': 1553189225436, 'updatedAt': 1554171394339, 'referrerId': 0, 'organizationId': 0, 'type': 'TRADER', 'level': 1, 'internal': True, 'canSignin': False, 'canTrade': False, 'canWithdraw': False}
    #userEnableUser
    #print(client.post("/manage/user/99000/enable",{"canSignin":"true","canTrade":"true","canWithdraw":"true"}))
    #{'id': 99000, 'createdAt': 1553189225436, 'updatedAt': 1554173146294, 'referrerId': 0, 'organizationId': 0, 'type': 'TRADER', 'level': 1, 'internal': True, 'canSignin': True, 'canTrade': True, 'canWithdraw': True}
    #symbolUpdate
    #print(client.post("/manage/symbol/BTC_USDT/update",{"baseMinimum":5000000000000,"displayOrder":"","endTime":5000000000000,"meta":"","quoteMinimum":5000000000000,"startTime":""}))
    #{'result': True}
    #ts = int(time.mktime(time.strptime(now(), "%Y-%m-%d %H:%M:%S")))
    #print(int(time.time()*1000))
    #symbolCreate
    #print(client.post("/manage/symbol/create",{"baseMinimum":5000000000000,"baseName":"LTC","baseScale":1,"displayOrder":1,"endTime":"","meta":"","quoteMinimum":5000000000000,"quoteName":"BTC","quoteScale":0.01,"sequenceIndex":0,"startTime":5000000000000,"type":""}))
    #'result': True}
    #snapshotDelete
    #print(client.post("/manage/snapshot/delete",{"table": ""}))
    #{'result': True}
    #snapshotCreate
    #print(client.post("/manage/snapshot/now",{}))
    #{'result': True}
    #orderForceCancel
    #print(client.post("/manage/order/100002/cancel",{}))
    #{'createdAt': 1554187194283, 'updatedAt': 1554187194283, 'seqId': 0, 'previousSeqId': 0, 'refOrderId': 100002, 'refSeqId': 3, 'userId': 99000, 'source': 'MGT', 'symbol': 'BTC_USDT', 'sequenceIndex': 1, 'type': 'CANCEL_BUY', 'price': 101.0, 'amount': 0, 'filledAmount': 0, 'fee': 0, 'triggerOn': 0.0, 'makerFeeRate': 0, 'takerFeeRate': 0, 'chargeQuote': True, 'features': 0, 'status': 'SUBMITTED', 'id': 100022, 'feeCurrency': 'USDT'}
    #feeUserFeeRatesDelete
    #print(client.post("/manage/fee/user/100002/delete",{}))
    #{'result': True}
    #feeUserFeeRatesCreate
    #print(client.post("/manage/fee/user/create",{"makerFeeRate":0.01,"startTime":1853189225436,"takerFeeRate":0.02,"userId":99001}))
    #static void checkStartTime(long startTime) {
		#if ((startTime - System.currentTimeMillis()) < 2 * REFRESH_INTERVAL) {
			#throw new ApiException(ApiError.PARAMETER_INVALID, "startTime", "startTime is too short from now on.");
     # public static final long REFRESH_INTERVAL = 10 * 60_000;
		#}
	#}
   #print(int(time.time()*1000)-1553189225436,10*60000)
    #{'result': True}

    #feeSymbolFeeRatesCreate
    #print(client.post("/manage/fee/symbol/create",{"makerFeeRate":0.001,"startTime":1853189225436,"symbol":"CFC_USDT","takerFeeRate":0.002}))
    #{'result': True}
    #feeSymbolFeeRatesDelete
    #print(client.post("/manage/fee/symbol/2/delete",{}))
    #{'result': True}

    #feeLevelFeeRatesCreate
    #print(client.post("/manage/fee/level/create",{"level":1,"makerFeeRate":0.001,"startTime":1853189225436,"takerFeeRate":0.002}))
    #{'result': True}

    #feeLevelFeeRatesDelete
    #print(client.post("/manage/fee/level/1/delete",{}))
    #{'result': True}




    #depositAudit ????????????????
    #print(client.post("/manage/deposit/100003/audit/False",{}))
    #{'result': True}
    #{'error': 'INTERNAL_SERVER_ERROR', 'data': None, 'message': "Request processing failed; nested exception is org.springframework.jdbc.BadSqlGrammarException: PreparedStatementCallback; bad SQL grammar [UPDATE deposit_logs SET status = ?, updatedAt = ?, version = version + 1 WHERE id = ?]; nested exception is com.mysql.jdbc.exceptions.jdbc4.MySQLSyntaxErrorException: Table 'ex.deposit_logs' doesn't exist"}




    #currencyUpdate
    #print(client.post("/manage/currency/USDT/update",{"depositEnabled":True,"meta":"","withdrawEnabled":True}))
    #{'result': True}

    #currencyDepositSetRules
    #print(client.post("/manage/currency/ETH/deposit/rules",{"rules":[{"amount":0,"confirms":1}]}))
    #{'rules': 1}
    #currencyCreate
    #print(client.post("/manage/currency/create",{"addressAliasTo":"ETH","legal":False,"meta":"","name":"XRP","token":False,"tokenContractAddress":"ETH","tokenDecimals":2,"tokenIssuesOn":"","xpubKey":""}))
    #{'result': True}
    #accountUnfreezeUserAccount
    #print(client.post("/manage/account/unfreeze",{"amount":"0.002","currency":"ETH","flowType":"TRADE_UNFREEZE","userId":99000}))
    #{'result': 0.002}

    #accountFreezeUserAccount
    #print(client.post("/manage/account/freeze",{"amount":"20.22","currency":"ETH","flowType":"TRADE_FREEZE","userId":99000}))
    #{'result': 20.22}

    #/v1/manage/kyc/request/list
    #print(client.get("/v1/manage/kyc/request/list"))



    #tempSignIn
    #print(client.post("/ui/json/signin",{'email':'email','passwd':'password','ga':'0000' }))