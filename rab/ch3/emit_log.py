#!/usr/bin/env python
import pika
import sys

def emit_log(message=None):
    message = message or ' '.join(sys.argv[1:]) or "info: Hello World!"
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', type='fanout')

    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=message)
    print " [x] Sent %r" % (message,)
    connection.close()

if __name__ == '__main__':
    emit_log()