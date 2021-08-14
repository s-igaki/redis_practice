import redis

def publish(con, channel, data):
    con.publish('hoge', 'hello')

def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    publish(r, 'hoge', 'hello')

if __name__ == '__main__':
    main()
