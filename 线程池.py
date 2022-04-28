from concurrent.futures import ThreadPoolExecutor,as_completed
import time
import random
def name(i):
    print('name is',i)
    time.sleep(random.randint(1,3))
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = [pool.submit(name,url) for url in range(15)]
        # for future in futures:
        #     print(future.result())
        for future in as_completed(futures):
            print(future.done())