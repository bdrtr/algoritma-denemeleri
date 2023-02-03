#bedir karaabalı
#i have tried to solve philosoph problem with python (random oriented)
#about problem -> https://bilgisayarkavramlari.com/2012/01/22/filozoflarin-aksam-yemegi-dining-philosophers/
#about threading -> https://python-istihza.yazbel.com/standart_moduller/threading.html

import threading as th
import random, time




list_of_philosophers = ["bedir","ali","mehmet","ahmet","veli"]
eat_time = random.randint(2,5)
eat_count = 3
think_time = random.randint(2,5)

my_semaphore = th.BoundedSemaphore(value=len(list_of_philosophers))

class Problem(th.Thread):
    def __init__(self,philosopher):
        th.Thread.__init__(self)
        self.philosopher = philosopher

    def run(self):
        for i in range(eat_count):
            print(self.philosopher,"is hungry") 
            print(self.philosopher,"is seated")
            my_semaphore.acquire()
            print(self.philosopher,"is eating")
            time.sleep(eat_time)
            my_semaphore.release()
            print(self.philosopher,"is thinking")
            time.sleep(think_time)
        
        print(self.philosopher,"is full")


if __name__ == "__main__":
    for philosopher in list_of_philosophers:
        Problem(philosopher).start()


        




