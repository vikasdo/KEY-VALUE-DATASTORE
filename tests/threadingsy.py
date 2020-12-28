import concurrent.futures
import time,threading
# from code.abc import dbstore
# from main import dbstore
from package import code
# from code import dbstore
start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds[2]} second(s)...',seconds)
    time.sleep(seconds[2])
    return f'Done Sleeping...{seconds[2]}'


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [('name','vikas',3),('street','canal lane',3),('city','hyderabad',2),('phone',9392322121,3),('state','Telangana',1)]
#     results = executor.map(obj.add, secs[0],secs[1],secs[2])

#     for result in results:
#         print(result)

path_file="/home/codespace/workspace/KEY-VALUE-DATASTORE/file"

threads = []
obj=dbstore(path_file)

for i in range(4):
    
    secs = [('name','vikas',113),('street','canal lane',3),('city','hyderabad',2),('phone2',9392322121,322),('states','Telangana',1)]
    obj.delete(secs[i][0],secs[i][1],secs[i][2])
    t = threading.Thread(target=obj.add , args=[secs[i][0],secs[i][1],secs[i][2]])
    t.start()
    
    threads.append(t)

for thread in threads:
    thread.join()
# for i in range(1):
    
#     secs = [('state','Telangana',1)]

#     t = threading.Thread(target=obj.delete , args=[secs[i][0],secs[i][1],secs[i][2]])

#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')