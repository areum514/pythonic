import threading

def worker(count):
    print("name : %s, argumnet : %s"%(threading.currentThread().getName(),count))
def main():
    for i in range(5):
        t = threading.Thread(target=worker, name = "thread %i"%i,args=(i,))
        t.start()
if __name__=="__main__":
    main()
        
