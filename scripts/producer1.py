import pika

username = 'hitrader'
password = 'hitrader123'

user_pwd = pika.PlainCredentials(username, password)
s_conn = pika.BlockingConnection(pika.ConnectionParameters('10.203.106.234',credentials=user_pwd))
chan = s_conn.channel()
chan.queue_declare(queue='hello')
chan.queue_bind('hello','250test','250')
chan.basic_publish(exchange='250test',routing_key='250',body='hello 250 250!')
print('[生产者] hello adfkajfl.')
s_conn.close()
