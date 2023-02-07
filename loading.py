from tqdm import tqdm
import time

members=["one", "two", "three", "four"]
for member in tqdm(members):
    print(member)
    time.sleep(1)
