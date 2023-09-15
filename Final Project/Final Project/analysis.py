from __future__ import print_function
import logging

import grpc

import datadriven_pb2
import datadriven_pb2_grpc

import redis

import random
import time
import datetime

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    while True:
        with grpc.insecure_channel('reader:50051') as channel:
            stub = datadriven_pb2_grpc.TextReaderStub(channel)
            total_length = 0        

            for response in stub.ReadText(datadriven_pb2.ReadRequest(request='')): 
               total_length += len(response.message) 
             # print('')          
             #  print("chars: " + str(total_length))
              # print("-- " + response.message)
               time.sleep(random.randint(1,6))

               wordlenth = len(response.message)
               vowel = 'False'
               sailor = 'False'
               window = 'False'

               if(response.message[0] == 'a' or response.message[0] == 'e' or response.message[0] == 'i' or response.message[0] == 'o' or response.message[0] == 'u'):
                    vowel = 'vowel'
 
               if(response.message == 'sailor'):
                    sailor = 'sailor'

               if(response.message == 'window'):
                    window = 'window'
 

               try:
                    conn = redis.StrictRedis(host='redis', port=6379) 
                    conn.set('log.greeter_server.' + str(datetime.datetime.now()) , vowel + ' ' + sailor + ' ' + window) 
               except Exception as ex: 
                    print('Error:', ex)
    

if __name__ == '__main__':
    logging.basicConfig()
    run()
