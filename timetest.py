import threading
import time


def music():
    print("我在听音乐")
    time.sleep(5)


def movie():
    print("我在看电影")


threads = []
t1 = threading.Thread(target=music)
threads.append(t1)
t2 = threading.Thread(target=movie)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        """
        setDaemon()方法中的属性值的含义为：当属性值为False的时候表示当主线程运行完了
        后需要判断子线程是否运行完毕，如果子线程没有运行完，则主线程需要等到子线程运行
        完后才能退出。
        当属性值为True的时候，当主线程运行完后不需要对其下子线程进行检查就可以之间
        退出，同时其下的所有属性值为True的子线程将全部结束退出
        """
        t.setDaemon(False)
        t.start()
    print("结束")
