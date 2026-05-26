import dubbo
from dubbo.configs import ReferenceConfig

class UnaryServiceStub:
    def __init__(self, client: dubbo.Client):
        self.unary = client.unary(method_name="unary")

    def say_hello(self, message: bytes) -> bytes:
        return self.unary(message)

if __name__ == "__main__":
    # Create a client
    reference_config = ReferenceConfig.from_url(
        "tri://127.0.0.1:50051/org.apache.dubbo.samples.HelloWorld"
    )
    dubbo_client = dubbo.Client(reference_config)
    unary_service_stub = UnaryServiceStub(dubbo_client)

    # Call the remote method
    result = unary_service_stub.say_hello(b"Hello from client")
    print(result)