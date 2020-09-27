from __future__ import print_function
import logging
import requests
import grpc
import time
import helloworld_pb2
import helloworld_pb2_grpc


def js():
    response = requests.get("https://meme-api.herokuapp.com/gimme")
    return response.text

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(message = js()))
    print(response.message)

while True:
    run()
    time.sleep(5)
