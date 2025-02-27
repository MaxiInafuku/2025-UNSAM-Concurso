import numpy as np 

class Solution:
    #Constructor
    def __init__(self, Mr, solutionType, pK='none', K='none',V=0, Cmolar=0, n=0, m=0):
        self.Mr = Mr
        self.solutionType = solutionType
        self.V = V
        self.Cmolar = Cmolar 
        self.n = n
        self.m = m
        self.pK = pK
        self.K = K

    #Methods
    def n_from_VCmolar(self):
        if self.Cmolar or self.V == 0:
            print('C(molar) or V are not defined.')
        else:
            self.n = self.Cmolar*self.V
            print('n:{:.4g} mol.' .format(self.n))
    
    def V_from_nCmolar(self):
        if self.n or self.Cmolar==0:
            print('C(molar) or n are not defined.')
        else:
            self.V = self.n/self.Cmolar
            print('V:{:.4g} L' .format(self.V))

    def Cmolar_from_nV(self):
        if self.n or self.V == 0:
            print('n or V are not defined.')
        else: 
            self.Cmolar = self.n/self.V
            print('C:{:.4g} M' .format(self.Cmolar))
    
    def K_from_pK(self):
        if self.pK == 'none':
            print('pKa is not defined')
        else: 
            self.K = 10**(-self.pK)
            print('Ka:{:.4g} ' .format(self.K))
    
    def pK_from_K(self):
        if self.K == 'none':
            print('Ka is not defined')
        else:
            self.pK = -np.log10(self.K)
            print('pKa:{:.4g} ' .format(self.pK))
        
    



