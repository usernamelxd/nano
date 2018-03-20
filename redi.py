import redis
import time
from datetime import datetime, timedelta
import random
import faker

r = redis.Redis(password='sunck')
faker = faker.Faker('zh_CN')
DEADLINE = datetime.now() + timedelta(hours=1)


def exam(course, students=50):
    print("%s exam start.....   %s  studends " % (course, students))
    for i in range(students):
        name = faker.name()
        time_remaining = (DEADLINE - datetime.now()).total_seconds()
        score = '%s.%s' % (random.randint(60, 100),
        str(time_remaining).replace('.', ''))
        r.zadd(course, name, score)
        print('%s: %s' % (name, score))
        time.sleep(0.2)
    print('%s axem end' % course)

def top(course, rank_range=10):
    stus = r.zrevrange(course, 0, rank_range-1, withscores=True)
    for i, (stu, score) in enumerate(stus):
        print(i + 1, stu.decode('utf-8'), score)


if __name__ == "__main__":
    courses = ['English','Math']
    for course in courses:
        exam(course)
        top(course)
