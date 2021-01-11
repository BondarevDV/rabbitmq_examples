#!/usr/bin/env python
import pika, sys


def main(msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=msg)
    print(" [x] Sent '{}'".format(msg))
    connection.close()



if __name__ == '__main__':
    try:
        print(len(sys.argv))
        for  _,arg in enumerate(sys.argv):
           main(arg)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

