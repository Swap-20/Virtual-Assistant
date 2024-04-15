import multiprocessing


def startAlexa():
    # code for process 1 = to run alexa
    print('Process 1 is running...')
    from main import start
    start()

def listenHotword():
    # code for process 2 = to run hotword
    print('Process 2 is running...')
    from engine.features import hotword
    hotword()

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=startAlexa)
    p2 = multiprocessing.Process(target=listenHotword)
    p1.start()
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print('system stop')
