
'''
Plotting and drawing functions

'''
import matplotlib.pyplot as plt
import open3d as o3d

from configs import BASIS_SIZE, WIDTH, NUMs_SHAPE , ITERS_I, SWAP_K, PLOTPATH_PCA
from configs import TRAINING_ID

def draw_point_cloud(ptcloud_matrix_3Nx1_old):
    print('point cloud old matrix shape:', ptcloud_matrix_3Nx1_old.shape)
    ptcloud_matrix_3Nx1 = ptcloud_matrix_3Nx1_old.reshape(-1,3) # check if it keeps xyz adjacent
    print('point cloud matrix shape:', ptcloud_matrix_3Nx1.shape)

    assert ptcloud_matrix_3Nx1_old[0] == ptcloud_matrix_3Nx1[0,0] , print(ptcloud_matrix_3Nx1[0,0] , ptcloud_matrix_3Nx1[0,0])
    assert ptcloud_matrix_3Nx1_old[1] == ptcloud_matrix_3Nx1[0,1]
    assert ptcloud_matrix_3Nx1_old[2] == ptcloud_matrix_3Nx1[0,2]
    assert ptcloud_matrix_3Nx1_old[3] == ptcloud_matrix_3Nx1[1,0]
    assert ptcloud_matrix_3Nx1_old[4] == ptcloud_matrix_3Nx1[1,1]
    


    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(ptcloud_matrix_3Nx1[:]) #reshape(-1,3) col matrix
    o3d.visualization.draw_geometries([pcd])
    #draw the point cloud
    return 

def plot_error_vs_iters(pca_error_periters_list,iters_idx):
    #plot the error vs iterations
    
    plt.plot(pca_error_periters_list)
    plt.xlabel('Iterations')
    plt.ylabel('Error')
    plt.title('Error vs Iterations')
    
    savepath = f'{PLOTPATH_PCA}/pca_error_vs_iters_{iters_idx}_{SWAP_K}_{BASIS_SIZE}_{WIDTH}_{NUMs_SHAPE}.png'
    plt.savefig(savepath)
    # plt.show()
    plt.close()

    return 

def plot_losses(Gene_losses, Disc_losses):
    #plot the losses of the generator and discriminator
    print(type(Gene_losses[0]))
    plt.plot(Gene_losses, label='Generator Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Losses vs Epochs')
    plt.legend()
    plt.savefig(f'plots/losses_vs_epochs_G{TRAINING_ID}.png')
    plt.show()

    #separately as scales are different
    plt.plot(Disc_losses, label='Discriminator Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Losses vs Epochs')
    plt.legend()
    plt.savefig(f'plots/losses_vs_epochs_D{TRAINING_ID}.png')
    return

def save_column_matrix_as_pcd(save_path, column_matrix):
    #save the column matrix as a point cloud data file
    column_matrix = column_matrix.reshape(-1,3) # check if it keeps xyz adjacent
    print(type(column_matrix), column_matrix.shape)
    
    
    # From numpy to Open3D
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(column_matrix) #column_matrix is a 3xN matrix
    path = save_path + '_' +'.pcd'

    
    o3d.io.write_point_cloud(path, pcd)
  

    return 