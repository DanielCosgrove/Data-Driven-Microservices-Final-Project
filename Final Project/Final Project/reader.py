from concurrent import futures
import logging

import grpc

import datadriven_pb2
import datadriven_pb2_grpc

import time



class TextReader(datadriven_pb2_grpc.TextReaderServicer):    

      def __init__(self):        

          self.greetings = open('ToTheLighthouse.txt', 'r')

      def ReadText(self, request, context):        
         
          for g in self.greetings:            
              
              for word in g.split():
                  time.sleep(2)            
                  yield datadriven_pb2.ReadReply(message=word)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    datadriven_pb2_grpc.add_TextReaderServicer_to_server(TextReader(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
