class Beagle:

#a class for Beagle

    def print(self):
        print("This is my favorite animal")
        print(f"Length of forelegs = {self.len_forelegs}")
        print(f"Length of hindlegs = {self.len_hindlegs}")
        print(f"Number of eyes = {self.num_eyes}")
        print(f"Does it have a tail = {self.TAIL_boolean}")
        print(f"Does it have fur = {self.FUR_boolean}")

    def __init__(self,lForelegs =6.5,lHindlegs =6.5,nEyes =2,TAIL =True,FUR =True):
        self.len_forelegs = lForelegs
        self.len_hindlegs = lHindlegs
        self.num_eyes = nEyes
        self.TAIL_boolean = TAIL
        self.FUR_boolean = FUR
        
Piaca = Beagle(6.5, 6.5, 2, True, True)    
Piaca2= Beagle()

Piaca.print()
Piaca2.print()
