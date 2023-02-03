import random,threading,time

#semaphore = threading.Semaphore()


class job(threading.Thread):
    def __init__(self,worker):
        threading.Thread.__init__(self)
        self.worker = worker

    def run(self):
        #semaphore.acquire()
        print(f"{self.worker} çalismaya basladi")
        time.sleep(random.randint(2,5))
        print(f"{self.worker} çalismayi bitirdi")
        #semaphore.release()

if __name__ == "__main__":
    
    workers = ["bedir","ahmet","mehmet","ali"]
    for worker in workers:
        job(worker).start()