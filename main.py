import time
import sys
import random
from sign import *

sign()
score = 0
def delete_last_line():
    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

no1 = random.randint(1,20)
no2 = random.randint(1,20)
no3 = random.randint(1,20)
no4 = random.randint(1,20)
no5 = random.randint(1,20)
no6 = random.randint(1,20)

time.sleep(1)

print(no1)
time.sleep(0.1)
delete_last_line()
time.sleep(0.6)

print(no2)
time.sleep(0.1)
delete_last_line()
time.sleep(0.1)

print(no3)
time.sleep(0.1)
delete_last_line()
time.sleep(0.4)

print(no4)
time.sleep(0.1)
delete_last_line()
time.sleep(0.3)

print(no5)
time.sleep(0.1)
delete_last_line()
time.sleep(0.4)

print(no6)
time.sleep(0.1)
delete_last_line()
time.sleep(0.4)

question = int(input("What was the third number? "))
if question == no3:
    score += 1
    print("Correct, keep going.")
    time.sleep(0.5)
else:
    print("Incorrect, keep going.")
    time.sleep(0.5)
question = int(input("What was the last number? "))
if question == no5:
    score += 1
    print("Correct, keep going.")
    time.sleep(0.5)
else:
    print("Incorrect, keep going.")
    time.sleep(0.5)
question = int(input("What was the first number? "))
if question == no1:
    score += 1
    print("Correct, keep going.")
    time.sleep(0.5)
else:
    print("Incorrect, keep going.")
    time.sleep(0.5)
question = int(input("How many numbers were there? "))
if question == 6:
    score += 1
    score_percent = score / 4 * 100
    print(f"Correct, your score was {score}/4. ({score_percent}%)")
    time.sleep(0.5)
else:
    score_percent = score / 4 * 100
    print(f"Incorrect, your score was {score}/4. ({score_percent}%)")
    time.sleep(0.5)