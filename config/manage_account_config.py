from config import global_variable

def manage_init(cir_var):
    if cir_var == "soda-dev1":
        account = {"manage_email": "root@example.com","manage_password": "password"}
    if cir_var == "soda-regress":
        account = {"manage_email": "root@example.com","manage_password": "password"}
    if cir_var == "soda-test":
        account = {"manage_email": "root@example.com","manage_password": "password"}
    if cir_var == "soda-stage":
        account = {"manage_email": global_variable.manage_email_stage,"manage_password": global_variable.manage_password_stage}
    return account