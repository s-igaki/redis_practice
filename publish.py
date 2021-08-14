import redis

def publish(con, channel, data):
    con.publish(channel, data)

def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    publish(r, 'hoge', '1hello')
    publish(r, 'hoge', '2hello')
    publish(r, 'hoge', '3hello')
    publish(r, 'hoge', '4hello')
    publish(r, 'hoge', '5hello')

if __name__ == '__main__':
    main()
