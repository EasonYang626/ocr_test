from aip import AipOcr
import webbrowser
import mss
import mss.tools
import time
import os
import keyboard
import re
import db

APP_ID = '00000000'
API_KEY = 'fad46ee1e2654ef5b857adefd17ecfb8'
SECRET_KEY = '78986563c59342898ce3041deaa90a99'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# 初始化识别客户端


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def image2text(fileName):
    image = get_file_content(fileName)
    dic_result = client.basicGeneral(image)
    res = dic_result['words_result']
    result = ''
    for m in res:
        result = result + str(m['words'])
        # 去掉无用的符号 会影响搜索
        # 去掉非 汉字英文数字 的符号
    new_res = re.sub(r'[^\u4e00-\u9fa5^a-zA-Z0-9]','',result)
    new_res = new_res.strip('0123456789')#去掉开头结尾的数字
    return new_res

def autoquery():
    with mss.mss() as sct:
        # print(sct.shot())
        beg = time.time()
        monitor = {"top": 140, "left": 100, "width": 270, "height": 73}
        # 指定截图的范围
        # output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        output = "problem.png"
        # Grab the data
        sct_img = sct.grab(monitor)
        # Save to the picture file
        # 转成PNG格式保存
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    keyword = image2text('problem.png')
    print('題目：' + keyword)
    url = "http://www.baidu.com/s?wd=" + keyword
    webbrowser.open(url, new=0, autoraise=True)
    end = time.time()
    print('耗時：'+ str(end - beg))
    insert_sql = """
                insert history (question , time)
                values('%s' , %s);
                """
    insert_sql = insert_sql % (keyword , end - beg)
    db.insert_or_update_data(insert_sql)

if __name__ == '__main__': 
    keyboard.add_hotkey('alt+r', autoquery)
    # keyboard.add_hotkey('Space', print, args=['space was pressed'])
    while True:
        keyboard.wait() 
        # print (sys.argv[0])
        # print (os.getcwd()) 测试当前工作目录
