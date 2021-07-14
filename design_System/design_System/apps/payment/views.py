import os
import traceback

from django.shortcuts import render
# from alipay import AliPay
# Create your views here.
from alipay import AliPay
from rest_framework.response import Response
from rest_framework.views import APIView
import base64
# app_private_key_string = open(r"C:\毕设\Design_System\design_System\design_System\apps\payment\key\alipay_public_key.pem").read()
# alipay_public_key_string = open(r"C:\毕设\Design_System\design_System\design_System\apps\payment\key\app_private_key.pem").read()

# app_private_key_string = base64.b64encode(app_private_key_string)
# alipay_public_key_string = base64.b64encode(alipay_public_key_string)
# app_private_key_string = "-----BEGIN RSA PRIVATE KEY-----"  + app_private_key_string + "    -----END RSA PRIVATE KEY-----"
#
# alipay_public_key_string = "-----BEGIN PUBLIC KEY-----" + alipay_public_key_string + "-----END PUBLIC KEY-----"
import logging

# from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
# from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
#
# from alipay.aop.api.domain.AlipayTradeCreateModel import AlipayTradeCreateModel
# from alipay.aop.api.request.AlipayTradeCreateRequest import AlipayTradeCreateRequest
# from alipay.aop.api.response.AlipayTradeCreateResponse import AlipayTradeCreateResponse

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s %(levelname)s %(message)s',
#     filemode='a',)
# logger = logging.getLogger('')
#
# if __name__ == '__main__':
#     # pass
#     # 实例化客户端
#     alipay_client_config = AlipayClientConfig()
#     alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
#     alipay_client_config.app_id = '2021000117689346'
#     alipay_client_config.app_private_key = 'MIIEpQIBAAKCAQEA3fG4pxoPQ/OHMyU++tTrJ/YhLVAA39FFHCtZJygCBUvfZiMNu2+e2LqSFMOE1tNlYnebDJxe0keCH70LFMx8JmxLbo/BNmwWfyWoaWO/TWytKS+X3unN+Hxk7265JfGGxPb0ZTl2CwJ6GDBQOnsWc4GisJbu0R340lxhaXhUUTVTtTjOXCbAME7xWDFzcHp6i3KcORnTdjT8hXc4NAnnw6C+A/okjCP/PIhQ7iXbg1Y+ss+iTjNgsOHn3FklDH4awqLBJWq08n0I+Zlxt0bnjVvldlbliN+9AvzPf4447W6r+qFZKyNF7rAoAw4N0VYYDJ8zCD75MfMRiezetPBlOwIDAQABAoIBAQDO1VyjBYsiZUoi5NwLf+9iP2Ltynf2HR1NwiwEbKltbCbWFWbPvZcIHN7UUN10Im+CUzqAhx1q0881asRv7pzoZdXqRDfoUtSoS1zmUlnOeq/pCPx8deFIaAzcgZA0ByD0X7yktOcIHZfRAP1TcrAalr4Z2Z7X7RmcWRFC7CuPvOizLGZVTvfCyKaAf1IVuxkhzFkzI0B7Spd/4qx06cvtIG0bU9Uk/tT0fvqlzO2xhWjSTUFt/GbsU3Ot1FXXSsyPaAXecKbSgDHZ59NGHbNRTZjhjbhbm3sU6ly2/5/bU6DkFVIZ2WlfewAeEPDFfOKG4oDjpZgxrrERCkWqdAsBAoGBAPxlslCsoEJvmxq5c0qK30y4m6a+Db9e5oLjFDu5wC2g4UcHV2WujaqTUSb6xSXGSD39q5EAXnNIldgLXG/SmnQ3VW9ROQRK77rySAmOEOGtd6wOo5OZvvur3JlVQmuJ02/HBceZE+zv1cF+jAkNHmzc1GbyVBUjZWI8fpGDmZ27AoGBAOEcvnz5a+MVvlU1gYBKdoDb5lvWMfNtleEeMTj2t8K3WIxaMRfqiPsT0vfQ937MOCfqrfEkIFi84rTqtfJ+7yx+Q4kOFw0x/sThTDItkxYlbyUEQ/z6X+X4Akf5QwAoVejv82GWxfgYZi/OBxoA27oCUEQcS4pqMbXTXvllZB6BAoGBAOmjUg8v3SHiohd49+pW5yHj+eG+KIev133tqnsnFWindiID/7kWffkaaZLFq92t0I3h1gFh8AyTcnINAkJZF7Tgy+tBqp/4pjXNtTVzFtlxdEgHPRCSz6G0k3402Eknylu8RfNgFnvL/3kgJYzzYeiv+sZZJ9BxdZYcHaWhxn+lAoGBAM/qz5n4eYhVheWHtOO8YvWjpYF/NcWjmsJBM69sWM+0rkl76EoxqnFUnw+a520qzFc574yBFItBcpctDf469UeAG3qUFABxA+HuQYU7CNZ0ntJuvSkES9zJE7pMZHDZ0HeEYKPrMVBzoLZYscB3uHp2NpKiG7dtXBqXbuoklrOBAoGADr8neDxTrO9eJE8zDgevU/gIzo9cFZKnYhXlQug6idaQDkWqfD97VtfWODeaOwCb6N6O2wvBpg8KjseyxLopzVFD/Mf8pC/fbldoXa7NUj6wpTz2R8qk5KljTXQG6cycBxTrpCypHrtdUmjvMBYxcYPeTa12bJzqHl3cCFOm4SE='
#     alipay_client_config.alipay_public_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDIgHnOn7LLILlKETd6BFRJ0GqgS2Y3mn1wMQmyh9zEyWlz5p1zrahRahbXAfCfSqshSNfqOmAQzSHRVjCqjsAw1jyqrXaPdKBmr90DIpIxmIyKXv4GGAkPyJ/6FTFY99uhpiq0qadD/uSzQsefWo0aTvP/65zi3eof7TcZ32oWpwIDAQAB'
#     client = DefaultAlipayClient(alipay_client_config, logger)
#
#     # 构造请求参数对象
#     model = AlipayTradeCreateModel()
#     model.out_trade_no = "20150320010101001"
#     model.total_amount = "88.88"
#     model.subject = "Iphone6 16G"
#     model.buyer_id = "2088102177846880"
#     request = AlipayTradeCreateRequest(biz_model=model)
#
#     # 执行API调用
#     try:
#         response_content = client.execute(request)
#     except Exception as e:
#         print(traceback.format_exc())
#
#     if not response_content:
#         print("failed execute")
#     else:
#         # 解析响应结果
#         response = AlipayTradeCreateResponse()
#         response.parse_response_content(response_content)
#         # 响应成功的业务处理
#         if response.is_success():
#             # 如果业务成功，可以通过response属性获取需要的值
#             print("get response trade_no:" + response.trade_no)
#         # 响应失败的业务处理
#         else:
#             # 如果业务失败，可以从错误码中可以得知错误情况，具体错误码信息可以查看接口文档
#             print(response.code + "," + response.msg + "," + response.sub_code + "," + response.sub_msg)
class PaymentStatusView(APIView):
    def post(self,request):
        DataPrice = request.data
        print(DataPrice)
        price = DataPrice.get("price").strip().split(",")
        print(price)
        carname = DataPrice.get("name")
        result = ""
        for i in price:
            result += i
        Total = result
        alipay_public_key_string = '''-----BEGIN PUBLIC KEY-----
            MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr4iqlQVteXpZ2TXI31TWYuoiUuIGJr40lb+7woY5xWMpO9bnPbRvIv7T4AyuOHgHir2Dgc+1HiqHI02BY6IdGcAeTitMoE/GzhgL3GD17XZSVUMHQjWIGgmaD0XRt0BuaDTW0gZBmHKdstC9MhKvbMMqMjqyXfT4igAloxdPc2/cmx29kH6gQOpG/ZITzXp3Rhkdv51iToN7Y94EwqUtguk/F6YeSblsahIARn/Co5tjuYIPY2C0ujO3nwiBfR9xGoVcesLurNmQQaPEdguhzO7wx2k3ktEKmEnytuY2GCLTkNRBUdyYBt0t5ZsSkC8eo3IFWO31IYutwn1v+FjJ4wIDAQAB
        -----END PUBLIC KEY-----'''

        app_private_key_string = '''-----BEGIN RSA PRIVATE KEY-----
            MIIEpQIBAAKCAQEA3fG4pxoPQ/OHMyU++tTrJ/YhLVAA39FFHCtZJygCBUvfZiMNu2+e2LqSFMOE1tNlYnebDJxe0keCH70LFMx8JmxLbo/BNmwWfyWoaWO/TWytKS+X3unN+Hxk7265JfGGxPb0ZTl2CwJ6GDBQOnsWc4GisJbu0R340lxhaXhUUTVTtTjOXCbAME7xWDFzcHp6i3KcORnTdjT8hXc4NAnnw6C+A/okjCP/PIhQ7iXbg1Y+ss+iTjNgsOHn3FklDH4awqLBJWq08n0I+Zlxt0bnjVvldlbliN+9AvzPf4447W6r+qFZKyNF7rAoAw4N0VYYDJ8zCD75MfMRiezetPBlOwIDAQABAoIBAQDO1VyjBYsiZUoi5NwLf+9iP2Ltynf2HR1NwiwEbKltbCbWFWbPvZcIHN7UUN10Im+CUzqAhx1q0881asRv7pzoZdXqRDfoUtSoS1zmUlnOeq/pCPx8deFIaAzcgZA0ByD0X7yktOcIHZfRAP1TcrAalr4Z2Z7X7RmcWRFC7CuPvOizLGZVTvfCyKaAf1IVuxkhzFkzI0B7Spd/4qx06cvtIG0bU9Uk/tT0fvqlzO2xhWjSTUFt/GbsU3Ot1FXXSsyPaAXecKbSgDHZ59NGHbNRTZjhjbhbm3sU6ly2/5/bU6DkFVIZ2WlfewAeEPDFfOKG4oDjpZgxrrERCkWqdAsBAoGBAPxlslCsoEJvmxq5c0qK30y4m6a+Db9e5oLjFDu5wC2g4UcHV2WujaqTUSb6xSXGSD39q5EAXnNIldgLXG/SmnQ3VW9ROQRK77rySAmOEOGtd6wOo5OZvvur3JlVQmuJ02/HBceZE+zv1cF+jAkNHmzc1GbyVBUjZWI8fpGDmZ27AoGBAOEcvnz5a+MVvlU1gYBKdoDb5lvWMfNtleEeMTj2t8K3WIxaMRfqiPsT0vfQ937MOCfqrfEkIFi84rTqtfJ+7yx+Q4kOFw0x/sThTDItkxYlbyUEQ/z6X+X4Akf5QwAoVejv82GWxfgYZi/OBxoA27oCUEQcS4pqMbXTXvllZB6BAoGBAOmjUg8v3SHiohd49+pW5yHj+eG+KIev133tqnsnFWindiID/7kWffkaaZLFq92t0I3h1gFh8AyTcnINAkJZF7Tgy+tBqp/4pjXNtTVzFtlxdEgHPRCSz6G0k3402Eknylu8RfNgFnvL/3kgJYzzYeiv+sZZJ9BxdZYcHaWhxn+lAoGBAM/qz5n4eYhVheWHtOO8YvWjpYF/NcWjmsJBM69sWM+0rkl76EoxqnFUnw+a520qzFc574yBFItBcpctDf469UeAG3qUFABxA+HuQYU7CNZ0ntJuvSkES9zJE7pMZHDZ0HeEYKPrMVBzoLZYscB3uHp2NpKiG7dtXBqXbuoklrOBAoGADr8neDxTrO9eJE8zDgevU/gIzo9cFZKnYhXlQug6idaQDkWqfD97VtfWODeaOwCb6N6O2wvBpg8KjseyxLopzVFD/Mf8pC/fbldoXa7NUj6wpTz2R8qk5KljTXQG6cycBxTrpCypHrtdUmjvMBYxcYPeTa12bJzqHl3cCFOm4SE=
        -----END RSA PRIVATE KEY-----'''

        alipay = AliPay(
            appid="2021000117689346",  # 支付宝app的id
            app_notify_url="http://127.0.0.1:8080/index/",  # 回调视图
            app_private_key_string=app_private_key_string,  # 私钥字符
            alipay_public_key_string=alipay_public_key_string,  # 公钥字符
            debug=True,
            sign_type="RSA2",  # 加密方法
        )
        import time
        order_string = alipay.api_alipay_trade_page_pay(

            out_trade_no=str(time.time() * 1000),
            total_amount=str(Total),  # 将Decimal类型转换为字符串交给支付宝
            subject=carname,
            return_url="http://127.0.0.1:8080/index/",
            notify_url="http://127.0.0.1:8080/index/"  # 可选, 不填则使用默认notify url
        )
        # print(order_string)
        loctime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        alipay_url = f"https://openapi.alipaydev.com/gateway.do?timestamp={loctime}&" + order_string
        return Response({"alipay_url":alipay_url})




