



#print(check_matchdetails_Feecurrencystr())

def sum_frozenamount_calculate(): # 计算账户冻结量 未做执行层
    #str="select  aa.userId,aa.currency,sum(aa.frozeen_amount) as amount  from (" \
    #    "select d.id , d.userid , 'withdraw' as bs , ifnull(d.amount,0)+ifnull(d.withdrawFee,0) as frozeen_amount, d.currency " \
    #    "from  withdraw_requests d where d.status not in ('CANCELLED','DONE','FAILED','DENIED') " \
    #    "union all " \
    #    "select a.id, a.userId ,LEFT(trim(a.type),LOCATE('_',trim(a.type))-1) as bs " \
    #    ",if (LEFT(trim(a.type),LOCATE('_',trim(a.type))-1)='SELL',if(trim(a.type)='BUY_MARKET',1,a.amount)-ifnull((select sum(ifnull(amount,0)) from match_details where orderid=a.id),0),0) as frozeen_amount " \
    #    ",LEFT(trim(a.symbol),LOCATE('_',trim(a.symbol))-1) as currency " \
    #    "from orders a where  a.status not in ('FULLY_CANCELLED','CANCELLED_OK','PARTIAL_CANCELLED','FULLY_FILLED') and a.refOrderId=0  " \
    #   "union all " \
    #   "select a.id, a.userId ,LEFT(trim(a.type),LOCATE('_',trim(a.type))-1) as bs " \
    #   ",if (LEFT(trim(a.type),LOCATE('_',trim(a.type))-1)='BUY',(if(trim(a.type)='BUY_MARKET',1,a.amount)-ifnull((select sum(ifnull(amount,0)) from match_details where orderid=a.id),0))*a.price,0)*(1+a.takerFeeRate) as frozeen_amount ," \
    #   "RIGHT(trim(a.symbol),LENGTH(trim(a.symbol))-LOCATE('_',trim(a.symbol))) as currency " \
    #   "from orders a where  a.status not in ('FULLY_CANCELLED','CANCELLED_OK','PARTIAL_CANCELLED','FULLY_FILLED') and a.refOrderId=0 ) aa   GROUP BY  aa.userId,aa.currency  order by aa.userId"
    #状态不明确，IEO冻结金额必须重新计算获取，不能使用表中已经计算好的冻结金额
    str="select  aa.userId,aa.currency,sum(aa.frozeen_amount) as amount  from (" \
        "select a.id ,a.user_id as userId,'IEO' as bs,a.frozen_funds as frozeen_amount, c.valuation_currency as currency   from ieo.user_purchase_info a ,ieo.currency_purchase_info  b  ,ieo.currency_exchange_rate c  " \
       " where   a.purchase_currency_id=b.id and b.start_time<=unix_timestamp(now())*1000  and a.state  in (0,1) and a.user_id >2000  and a.payment_currency=c.valuation_currency and c.currency_id=a.purchase_currency_id "\
       "union all " \
       "select id,user_id as userId,'withdraw' as bs  ,ifnull(amount,0)+ifnull(fee,0) as frozeen_amount , currency   from fiat_withdraw  where status  in ('WAITING_CONFIRM_FOR_OPERATION','WAITING_CONFIRM_FOR_FINANCE','SUBMITTED','AML_RISK','AML_RISK_REPORTED') " \
       "union all " \
       "select d.id , d.userid , 'withdraw' as bs , ifnull(d.amount,0)+ifnull(d.withdrawFee,0) as frozeen_amount, d.currency from  withdraw_requests d where d.status not in ('CANCELLED','DONE','FAILED','DENIED') " \
       "union all " \
       "select a.id, a.userId ,LEFT(trim(a.type),LOCATE('_',trim(a.type))-1) as bs ,if (LEFT(trim(a.type),LOCATE('_',trim(a.type))-1)='SELL',if(trim(a.type)='BUY_MARKET',1,a.amount)-ifnull((select sum(ifnull(amount,0)) from match_details " \
       "where orderid=a.id),0),0) as frozeen_amount ,LEFT(trim(a.symbol),LOCATE('_',trim(a.symbol))-1) as currency from orders a where  a.status not in ('FULLY_CANCELLED','CANCELLED_OK','PARTIAL_CANCELLED','FULLY_FILLED') and a.refOrderId=0   " \
       "union all " \
       "select a.id, a.userId ,LEFT(trim(a.type),LOCATE('_',trim(a.type))-1) as bs ,if (LEFT(trim(a.type),LOCATE('_',trim(a.type))-1)='BUY',(if(trim(a.type)='BUY_MARKET',1,a.amount)-ifnull((select sum(ifnull(amount,0)) from match_details where orderid=a.id),0))*a.price,0)*(1+a.takerFeeRate) as frozeen_amount ,RIGHT(trim(a.symbol),LENGTH(trim(a.symbol))-LOCATE('_',trim(a.symbol))) as currency from orders a " \
       "where  a.status not in ('FULLY_CANCELLED','CANCELLED_OK','PARTIAL_CANCELLED','FULLY_FILLED') and a.refOrderId=0 " \
       " ) aa   GROUP BY  aa.userId,aa.currency  order by aa.userId"
    return str

#print(sum_frozenamount_calculate())



def get_frozenamount_sys():# 获取账户 未做执行层
    str="select d.id,d.userId,d.balance ,d.currency from spot_accounts d where d.type='SPOT_FROZEN'"
    return str
#print(get_frozenamount_sys())


def check_orderfilledamount():
    str="select a.id,a.filledAmount ,ifnull((select sum(amount)  from  match_details where orderid=a.id),0) as tradeamount from  orders a"
    return str
#print(check_orderfilledamount())


def get_accountspotavailable():

    #init_deposit=123600000.00 #USDT
    #init_deposit_1=21100.00 #BTC
    #init_deposit_2=98500.00#ETH

    # str="select aaa.userid,aaa.currency," \
    #     "case aaa.currency " \
    #     "when 'ETH' then 98500 " \
    #     "WHEN 'USD' then 123600000 " \
    #     "WHEN 'BTC' then 21100 " \
    #     "WHEN  'LTC' then 0 " \
    #     "END " \
    #     "+sum(aaa.amount) -ifnull((select balance from spot_accounts where userid=aaa.userid and type='SPOT_FROZEN' and currency=aaa.currency),0) as amount /*,aaa.type*/ from  " \
    #    "(select a.userid,a.currency,a.amount,'deposit' as type  from deposit_results a where status ='DEPOSITED' " \
    #    "union all " \
    #    "select f.userid,f.currency, -1*(f.amount+f.withdrawFee) as amount ,'withdraw' as type from withdraw_requests f where f.status ='DONE' " \
    #    "union all " \
    #     "select aa.userid,aa.currency_base as Currency,aa.amount_base as amount ,'trade' as type from  (select  a.userid, b.symbol " \
    #     ",if(LEFT(trim(b.type),LOCATE('_',trim(b.type))-1)='BUY',  a.amount,-1*a.amount) as amount_base " \
    #     ",LEFT(trim(b.symbol),LOCATE('_',trim(b.symbol))-1) as currency_base from  match_details a,orders b where b.id=a.orderId ) aa " \
    #     "union all " \
    #     " select aa.userid,aa.currency_quote as Currency,aa.amount_quote as amount,'trade' as type  from (select  a.userid, b.symbol " \
    #     ",if(LEFT(trim(b.type),LOCATE('_',trim(b.type))-1)='SELL', a.amount*a.price-a.fee,-1*a.amount*a.price-a.fee)  as amount_quote " \
    #     ",RIGHT(trim(b.symbol),LENGTH(trim(b.symbol))-LOCATE('_',trim(b.symbol))) as currency_quote from  match_details a,orders b " \
    #     "where b.id=a.orderId ) aa ) aaa group by aaa.userid,aaa.currency"

#123600000

    str="select aaa.userid,aaa.currency," \
        "case aaa.currency " \
        "when 'USDT' then 0 " \
        "when 'ETH' then 0 " \
        "WHEN 'BTC' then 0 " \
        "WHEN  'LTC' then 0 " \
        "WHEN  'BCH' then 0 " \
        "WHEN  'CKB' then 0  " \
        "WHEN  'ETC' then 0  END +sum(aaa.amount) -ifnull((select balance from spot_accounts where userid=aaa.userid and type='SPOT_FROZEN' and currency=aaa.currency),0) as amount " \
        "from  ( " \
        "select  user_id as userid,currency,amount ,'deposit' as type from fiat_deposit_results  where status in ('DEPOSITED') " \
        "union all " \
        "select a.user_id as userid ,b.name as currency ,a.effective_purchase as amount ,'IEO_in' as type    from ieo.user_purchase_info a, ieo.currency_purchase_info  b ,ieo.currency_exchange_rate c  "\
       " where a.purchase_currency_id=b.id and  b.end_time< unix_timestamp(now())*1000 and a.state=2 and a.user_id>2000 and a.payment_currency=c.valuation_currency  and c.currency_id=a.purchase_currency_id "\
       "union all "\
       "select a.user_id as userid ,a.payment_currency as currency ,-1*a.actual_deduction as amount ,'IEO_out' as type     from ieo.user_purchase_info a, ieo.currency_purchase_info  b ,ieo.currency_exchange_rate c  "\
       " where a.purchase_currency_id=b.id and  b.end_time< unix_timestamp(now())*1000 and a.state=2 and a.user_id>2000 and a.payment_currency=c.valuation_currency and c.currency_id=a.purchase_currency_id "\
       "union all "\
       "select inviter_id as userid,trade_currency as currency, refund_fee as amount ,'TRANSFER_REFUND' as type  from invite_fee_refund where success=1"\
       " union all "\
       "select toUserId as userid,currency,amount,'deposit' as type  from spot_account_flows  where flowType in ('ADJUST','IEO_INVITE_REBATE') "\
       "union all " \
       "select a.userid,a.currency,a.amount,'deposit' as type  from deposit_results a where status ='DEPOSITED' " \
       "union all "\
       "select fromUserId as userid ,currency,-1*amount as amount,'withdraw' as type   from spot_account_flows  where flowType  in ('ADJUST','IEO_INVITE_REBATE') "\
       "union all " \
       "select user_id as userid,currency,-1*ifnull(amount+fee,0) as amount , 'withdraw' as type  from fiat_withdraw  where status in ('DONE') " \
       "union all " \
       "select f.userid,f.currency, -1*(f.amount+f.withdrawFee) as amount ,'withdraw' as type from withdraw_requests f where f.status ='DONE' " \
       "union all " \
       "select aa.userid,aa.currency_base as Currency,aa.amount_base as amount ,'trade' as type " \
       "from  ( " \
       "select  a.userid, b.symbol ,if(LEFT(trim(b.type),LOCATE('_',trim(b.type))-1)='BUY',  a.amount,-1*a.amount) as amount_base ,LEFT(trim(b.symbol),LOCATE('_',trim(b.symbol))-1) as currency_base  " \
       "from  match_details a,orders b where b.id=a.orderId ) aa  " \
       "union all  " \
       "select aa.userid,aa.currency_quote as Currency,aa.amount_quote as amount,'trade' as type " \
       " from ( " \
       "select  a.userid, b.symbol ,if(LEFT(trim(b.type),LOCATE('_',trim(b.type))-1)='SELL', a.amount*a.price-a.fee,-1*a.amount*a.price-a.fee)  as amount_quote ,RIGHT(trim(b.symbol),LENGTH(trim(b.symbol))-LOCATE('_',trim(b.symbol))) as currency_quote " \
       "from  match_details a,orders b where b.id=a.orderId " \
       ") aa ) aaa where aaa.userid>=2000 group by aaa.userid,aaa.currency;"


    return str

#print(get_accountspotavailable())








