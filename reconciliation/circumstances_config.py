import pymysql


def config_init_(name):
    cir_config=dict()
    #if name=="matrix":
        #cir_config={"host":"api-test.matrix.co","protocol":"https","origin":"https://ui-new-test.matrix.co","referer":"https://ui-new-test.matrix.co/"}
    if  name=="dev1":
         cir_config={"host":"api-dev1.bitsoda.top","protocol":"https","origin":"https://ui-new-dev1.bitsoda.top","referer":"https://ui-new-dev1.bitsoda.top/"}
    if  name=="test":
         cir_config={"host":"api-test.bitsoda.top","protocol":"https","origin":"https://ui-new-test.bitsoda.top","referer":"https://ui-new-test.bitsoda.top/"}
    if  name=="stage":
         cir_config={"host":"api-stage.bitsoda.top","protocol":"https","origin":"https://ui-new-stage.bitsoda.top","referer":"https://ui-new-stage.bitsoda.top/"}
    #if  name=="pressure":
         #cir_config={"host":"api-benchmark.matrix.co","protocol":"https","origin":"https://ui-new-benchmark.matrix.co","referer":"https://ui-new-benchmark.matrix.co/trade"}
    #if  name=="test":
         #cir_config={"host":"api-test.matrix.co","protocol":"https","origin":"https://ui-new-test.matrix.co","referer":"https://ui-new-test.matrix.co/trade"}
    #if  name=="ui-new":
         #cir_config={"host":"api.matrix.co","protocol":"https","origin":"https://ui-new.matrix.co","referer":"https://ui-new.matrix.co/trade"}

    return cir_config


