import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe('hoge')
for message in p.listen():
    print(message)
