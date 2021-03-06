from module import Module 

class ReLU(Module):

    def __init__(self):

        super(ReLU, self).__init__()
        self.x = None

        
    def forward(self,x):

        self.x = x
        y = x * (x > 0).float()
        return y

    def backward(self, dl_ds):
        
        ds_dx =  0.5 * (self.x.sign() + 1 )
        dl_dx = ds_dx * dl_ds
        return dl_dx