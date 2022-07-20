import time 
import random

class Internet:

    def check_alice(self):
        if len(Alice.packets) > 0:
            Bob.packets = Alice.packets
            

class Alice:
    ## Periodically creates "packets" to send to Bob
    packets = []
    def create_packets(self):
        for i in range(random.randint(1,10)):
            self.packets.append([random.randint(1,100)])

class Bob:
    packets = []
    def read_packets(self):
        if len(self.packets) > 0:
            print("Reading packets: ",self.packets) ##reading them
            for ele in self.packets:
                self.packets.remove(ele)
if __name__ == "__main__":
    alice = Alice()
    bob = Bob()
    internet = Internet()
    k = 0
    while k < 15:
        alice.create_packets()
        #time.sleep(random.randint(1,7))
        internet.check_alice()
        #time.sleep(random.randint(1,3))
        bob.read_packets()
        k+=1
