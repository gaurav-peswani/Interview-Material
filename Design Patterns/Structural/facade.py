"""
Facade Pattern:
 * Provides a simpliefied interface to a library, framework or a comlex set of classes.
"""

class Transform():

    def __init__(self, image):
        pass
    
    def transform(self):
        print("Transforming...")
        pass

class Transpose():

    def __init__(self, image):
        pass

    def transpose(self):
        print("Transposing...")
        pass

class Resize():

    def __init__(self, image):
        pass

    def resize(self):
        print("Resizing...")
        pass

## This class is a Facade.
class Photo():

    def __init__(self, image):
        self.image = image

    def process(self):
        Transform(self.image).transform()
        Transpose(self.image).transpose()
        Resize(self.image).resize()
        print("Final Image is here!")
        return self.image
    
if __name__ == "__main__":
    Photo("Image").process()

    ## If the Facade was not there, we would have to create the 
    ## classes ourselves and do the complete process manually.
