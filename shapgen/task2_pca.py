

import open3d as o3d
import numpy as np
from sklearn.decomposition import PCA
from numpy import linalg as la

from configs import BASIS_SIZE

pca = PCA(n_components = BASIS_SIZE) #components





def pca():
    with open(filepath, 'rb') as f:
        b = np.load(f)
        print(b, b.shape)
        print(type(b))

        # scaling=StandardScaler()# Use fit and transform method 
        # scaling.fit(pointcloud)

        pca.fit(b) #pretty fast no need to time
        print(pca.explained_variance_ratio_)
        print(pca.singular_values_)


def pca_using_svd(m_3NxS):

    #do some preprocessing ( like centering of matrix ,
    #  check what exactly)
    #-------------------------------------------

    U, S, Vt = la.svd(m_3NxS, full_matrices=False)
    #expected shapes?  seems U V are switched? not sure

    V = Vt.T 
    print('U:', U.shape, 'S:', S.shape, 'V:', V.shape)
    return U,S,V


def pca_matrices():
    pass


if __name__ == '__main__':
    print(reconstruction_error_pca())
    print('done')