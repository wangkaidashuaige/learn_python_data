from hashlib import sha256
import hmac, base64


def get_sha256(data, key):
    key = key.encode('utf-8')  # sha256加密的key
    message = data.encode('utf-8')  # 待sha256加密的内容
    sign = base64.b64encode(hmac.new(key, message, digestmod=sha256).digest()).decode()
    return sign


if __name__ == '__main__':
    key = 'HappyNewYear123456'
    data_str = '一段测试的字符串,祝你新年快乐哦!'
    sign = get_sha256(data_str, key)
    print(sign)
