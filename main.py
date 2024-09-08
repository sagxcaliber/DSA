class burger:
    onion = "onion"

    def __init__(self):
        self.bun = 'bun'
        self.tikii = 'tikki'

    def getBuger(self):
        return {
            "bun": self.bun
            , "tikki": self.tikii
        }


a = burger()
a.tikii = 'potato tikki'
burger.onion = 'banana'
print(a.onion)
print(a.getBuger())

b = burger()
print(b.onion)
print(b.getBuger())
type()