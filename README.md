# redis遊んでみたリポジトリ
## 概要
使ったことあるけど、0から立てて、色々機能を利用したことがなかったので遊んでみた。

## 前提条件
以下がインストール済み

python3
pip3
docker

## 起動準備

```
pip3 install redis
docker-compose up -d
```

## キャッシュ機能の利用
redisにデータをセットして、取得しているだけ。

```
python3 ./cache.py
```


## pub/sub機能の利用
redisにpublishがデータをセットして、subscribeが取得する。

```
python3 ./subscribe.py
```
別ターミナルで以下のコマンドを実行するとsubscribeの方でデータが読まれる。
