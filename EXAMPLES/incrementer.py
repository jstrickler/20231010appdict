class Incrementer:
    def __init__(self, initial_value=0):
        self._value = initial_value

    def __call__(self):
        self._value += 1

    @property
    def value(self):
        return self._value
    
if __name__ == "__main__":
    inc = Incrementer()
    # inc.increment()
    inc()
    inc()
    inc()
    print(f"inc.value: {inc.value}")
    
