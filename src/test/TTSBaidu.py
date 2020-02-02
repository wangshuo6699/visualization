import tempfile
from aip import AipSpeech

appid = '9670645'
api_key = 'qg4haN8b2bGvFtCbBGqhrmZy'
secret_key = '585d4eccb50d306c401d7df138bb02e7'
dev_pid = 1936
lan = 'zh'

client = AipSpeech(appid, api_key, secret_key)
result = client.synthesis(
    '你好',
    lan,
    1,
    {
        'vol': 5,  # 合成音频文件的准音量
        'spd': 4,  # 语速取值0-9,默认为5中语速
        'pit': 8,  # 语调音量,取值0-9,默认为5中语调
        'per': 0  # 发音人选择,0为女声,1为男生,3为情感合成-度逍遥,4为情感合成-度丫丫,默认为普通女
    }  # options:这是一个dict类型的参数,里面的键值对才是关键.
)


def write_temp_file(data, suffix, mode='w+b'):
    """
    写入临时文件

    :param data: 数据
    :param suffix: 后缀名
    :param mode: 写入模式，默认为 w+b
    :returns: 文件保存后的路径
    """
    with tempfile.NamedTemporaryFile(mode=mode, suffix=suffix,
                                     delete=False) as f:
        f.write(data)
        tmpfile = f.name
    return tmpfile


if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
