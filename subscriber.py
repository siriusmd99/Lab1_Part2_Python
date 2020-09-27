import grpc


import helloworld_pb2
import helloworld_pb2_grpc


def select_mem():
    while True:
        print("""select that mem you want:
        1.memes
        2.dankmemes
        3.me_irl""")
        user_inp = int(input())
        if user_inp == 1:
            return "i'd like memes"
        elif user_inp == 2:
            return "i'd like dankmemes"
        elif user_inp == 3:
            return "i'd like me_irl"
        else:
            print("eror plz select 1 of this!")
        
sub_mess = select_mem()

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(message = sub_mess))
    print(response.message)