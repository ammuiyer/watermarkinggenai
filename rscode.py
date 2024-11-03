import unireedsolomon as rs

class rscode:
    def __init__(n, k):
        self.coder = rs.RSCoder(n,k)
    def encode(self, message: bytes):
        return self.coder.encode(message.decode("utf-8"))
    def decode(self, code: str):
        return self.coder.decode()



    