class Protected:
    def __init__(self):
         self.protectedVar = 0
 
obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)

class Protected:
    def __init__(self):
            self._privateVar = 12

    def getPrivate(self):
            print(self._privateVar)

    def setPrivate(self, private):
            self._privateVar = private

    obj = Protected()
    obj.getPrivate()
    obj.setPrivate(23)
    obj.getPrivate()

