# import requests
# from config import circumstance_config,global_variable
#
#
# def upload_pic():
#     pass
#
#
# def kyc_basic_info_api(IDType,country,firstName,lastName,IDNumber,token):
#     url = "https://"+ circumstance_config.circumstance_config_init(global_variable.cir_var) + "/v1/soda/kyc/basic_info"
#     header = {"Content-Type":"application/json","Authorization":token}
#     data = {"IDType":"PASSPROT_CARD",
#             "country":"CHN",
#             "firstName":"111",
#             "lastName":"2222",
#             "IDNumber":"33333",
#             "IDFrontPhoto":"https://bitsoda-static.oss-cn-shanghai.aliyuncs.com/kyc/1569749562330_19.640505292300748",
#             "IDHandPhoto":"https://bitsoda-static.oss-cn-shanghai.aliyuncs.com/kyc/1569749573442_95.69916011572141"}
#
#     data = {"IDType":"IDENTITY_CARD",
#             "country":"CHN",
#             "firstName":"111",
#             "lastName":"222",
#             "IDNumber":"333",
#             "IDFrontPhoto":"https://bitsoda-static.oss-cn-shanghai.aliyuncs.com/kyc/1569750177769_61.956901037702664",
#             "IDBackPhoto":"https://bitsoda-static.oss-cn-shanghai.aliyuncs.com/kyc/1569750180504_76.61908880522022",
#             "IDHandPhoto":"https://bitsoda-static.oss-cn-shanghai.aliyuncs.com/kyc/1569750183734_83.9102167870409"}
#
#     data = {"IDType":"DRIVING_CARD",
#             "country":"CHN",
#             "firstName":"111",
#             "lastName":"222",
#             "IDNumber":"333",
#             "IDFrontPhoto":"https://bitsoda-static.oss-cn-shanghai.aliyuncs.com/kyc/1569750257761_27.793646966336926",
#             "IDHandPhoto":"https://bitsoda-static.oss-cn-shanghai.aliyuncs.com/kyc/1569750260905_41.20139762742496"}