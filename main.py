import random
import string
import time
while True:
    lower = string.ascii_lowercase;
    upper = string.ascii_uppercase;
    num = string.digits;
    symbols = string.punctuation;
    length = random.randint(1, 90);
    all = lower + upper + num + symbols;
    temp = random.sample(all,length);
    text = "".join(temp);
    print(text);
    time.sleep(0.009);
