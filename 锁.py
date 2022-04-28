import threading
import time
locke = threading.Lock()
class Acc:
    def __init__(self,blanace):
        self.blance = blanace
def lock(acc,amout):
    with locke:
        if acc.blance > amout:
            time.sleep(0.1)
            print(threading.current_thread().name, '取钱成功')
            acc.blance -= amout
            print(threading.current_thread().name, '余额：', acc.blance)
        else:
            print(threading.current_thread().name, '取钱失败')
if __name__ == '__main__':
    acc = Acc(1500)
    ta = threading.Thread(name='1',target=lock,args=(acc,800,))
    tb = threading.Thread(name='2', target=lock, args=(acc, 800,))
    ta.start()
    tb.start()