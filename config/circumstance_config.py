from config.db_config import cir_var
# Filename: circumstance_config.py
# author: yujie.li


def circumstance_config_init(cir_var):
    cir_config = dict()
    if cir_var == "soda-dev1":
        cir_config = {"host": "api-dev1.bitsoda.top", "protocol": "https", "origin": "https://ui-new-dev1.bitsoda.top", "referer": "https://ui-new-dev1.bitsoda.top/"}
    if cir_var == "soda-regress":
        cir_config = {"host": "api-regress.bitsoda.top", "protocol": "https","origin": "https://ui-new-regress.bitsoda.top", "referer": "https://ui-new-regress.bitsoda.top/"}
    if cir_var == "soda-test":
        cir_config = {"host": "api-test.bitsoda.top", "protocol": "https","origin": "https://ui-new-test.bitsoda.top", "referer": "https://ui-new-test.bitsoda.top/"}
    if cir_var == "soda-stage":
        cir_config = {"host": "api-stage.bitsoda.top", "protocol": "https", "origin": "https://ui-new-stage.bitsoda.top",
                      "referer": "https://ui-new-stage.bitsoda.top/"}
    if cir_var == "manage-dev1":
        cir_config = {"host": "manage-new-dev1.bitsoda.top", "protocol": "https", "origin": "https://manage-new-dev1.bitsoda.top", "referer": "https://manage-new-dev1.bitsoda.top/"}
    if cir_var == "manage-test":
        cir_config = {"host": "manage-new-test.bitsoda.top", "protocol": "https", "origin": "https://manage-new-test.bitsoda.top", "referer": "https://manage-new-test.bitsoda.top/"}
    if cir_var == "manage-regress":
        cir_config = {"host": "manage-new-regress.bitsoda.top", "protocol": "https", "origin": "https://manage-new-regress.bitsoda.top", "referer": "https://manage-new-regress.bitsoda.top/"}
    return cir_config

def manage_config_init(cir_var):
    cir_config = dict()
    if cir_var == "soda-dev1":
        cir_config = {"host": "manage-new-dev1.bitsoda.top", "protocol": "https", "origin": "https://manage-new-dev1.bitsoda.top", "referer": "https://manage-new-dev1.bitsoda.top/"}
    if cir_var == "soda-regress":
        cir_config = {"host": "manage-new-regress.bitsoda.top", "protocol": "https", "origin": "https://manage-new-regress.bitsoda.top", "referer": "https://manage-new-regress.bitsoda.top/"}
    if cir_var == "soda-test":
        cir_config = {"host": "manage-new-test.bitsoda.top", "protocol": "https", "origin": "https://manage-new-test.bitsoda.top", "referer": "https://manage-new-test.bitsoda.top/"}
    if cir_var == "soda-stage":
        cir_config = {"host": "manage-new-stage.bitsoda.top", "protocol": "https", "origin": "https://manage-new-stage.bitsoda.top", "referer": "https://manage-new-stage.bitsoda.top/"}
    return cir_config


def get_config():
    config = circumstance_config_init(cir_var)
    return config

