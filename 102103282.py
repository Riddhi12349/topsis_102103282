import numpy as np
import pandas as pd
import sys

def topsis(decision,weights,impacts):
    decision = np.array(decision).astype(float)
    weights = np.array(weights).astype(float)
    impacts = [char for char in impacts]
    
    nrow = decision.shape[0]
    ncol = decision.shape[1]
    
  
    assert len(decision.shape) == 2, "Decision matrix must be two dimensional"
    assert len(weights.shape) == 1, "Weights array must be one dimensional"
    assert len(weights) == ncol, "Wrong length of Weights array, should be {}".format(ncol)
    assert len(impacts) == ncol,"Wrong length of Impacts array, should be {}".format(ncol)
    

    weights = weights/sum(weights)
    

    N = np.zeros((nrow,ncol))
    
    nf = [None]*ncol
    for j in range(ncol):
        nf[j] = np.sqrt(sum((decision[:,j])**2))
    
   
    for i in range(nrow):
        for j in range(ncol):
            N[i][j] = decision[i][j]/nf[j]
    
   
    W = np.diag(weights)
    V = np.matmul(N,W)
    
    
    u = [max(V[:,j]) if impacts[j] == '+' else min(V[:,j]) for j in range(ncol)]
    l = [max(V[:,j]) if impacts[j] == '-' else min(V[:,j]) for j in range(ncol) ]
    
     
    du = [None]*nrow
    dl = [None]*nrow
    
    
    for i in range(nrow):
        du[i] = np.sqrt(sum([(v1-u1)**2 for v1,u1 in zip(V[i],u) ]))
    for i in range(nrow):
        dl[i] = np.sqrt(sum([(v1-u1)**2 for v1,u1 in zip(V[i],l) ]))
    
    du = np.array(du).astype(float)
    dl = np.array(dl).astype(float)
    
    
    score = dl/(dl+du)
    
   
    index = pd.Series([i for i in range(nrow)])
    score = pd.Series(score)
    ranks = score.rank(ascending = False,method = 'min').astype(int)
    result = pd.concat([index,score, ranks], axis=1)
    result.columns = ['Alternative','Score','Rank']
    result = result.set_index('Alternative')
    return result
