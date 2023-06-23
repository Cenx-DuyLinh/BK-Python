def RUN():

    class A :
        def __init__(self) -> None:
            pass
    class B (A):
        def __init__(self) -> None:
            super().__init__()
if __name__ == '__main__':
    RUN()
