import redis

def setData(con, data):
    for key, value in data.items():
        if con.set(key, value):
            continue
        else:
            raise Exception('error!');

def getData(con, key):
    data = con.get(key)
    if data is None:
        return ''
    return data.decode()

def main():
    data = {'name_1':'tanaka'}
    con = redis.Redis(host='localhost', port=6379, db=0)
    setData(con, data)
    print(getData(con, 'name_1'))
    print(getData(con, 'name_2'))

if __name__ == '__main__':
    main()
