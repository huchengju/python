import requests
from config import circumstance_config, global_variable

from config import circumstance_config
from config import global_variable

def get_user_profile_api(token):
    url = "https://" + circumstance_config.circumstance_config_init(global_variable.cir_var).get("host") + "/v1/json/user/profile"
    # print(url)
    header = {"Authorization":token}
    response = requests.request("GET",url=url,headers = header)
    print(response.json())
    return response.json()

get_user_profile("AAAADB4L030000016d7736254fWEB7db1fae1fb816fbb20227f9f85685f500145b2341cc60807102a2623812b4b24")