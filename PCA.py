'''
@author: ankita
'''
import numpy  as np

x_coordinate_list = []
y_coordinate_list = []
z_coordinate_list = []


def ReadFile():
    list_of_coordinates = []
    global x_coordinate_list
    global y_coordinate_list
    global z_coordinate_list
    with open("./pca-data.txt", "r") as fo:
        for line in fo:
            list_of_coordinates.append(line)
    fo.close()
    for line in list_of_coordinates:
        list_of_items_in_line = line.split()
        x_coordinate_list.append(float(list_of_items_in_line[0]))
        y_coordinate_list.append(float(list_of_items_in_line[1]))
        z_coordinate_list.append(float(list_of_items_in_line[2]))


def PCA():
    Mean=[]
    m=0.0
    mean_x = np.mean(x_coordinate_list)
    mean_y = np.mean(y_coordinate_list)
    mean_z = np.mean(z_coordinate_list)
    cov_mat = np.cov([x_coordinate_list, y_coordinate_list, z_coordinate_list])

    Mean = [[mean_x],[mean_y], [mean_z]]
    
    print "Mean Vector: \n", Mean
    print "Covariance Matrix: \n", cov_mat
    eig_val_cov, eig_vec_cov = np.linalg.eig(cov_mat)
    print "eigen value from covariance Matrix :\n ",eig_val_cov
    print "eigen Vector from covariance Matrix:\n", eig_vec_cov

    for i in range(len(eig_val_cov)):
        eigvec_cov = eig_vec_cov[:, i].reshape(1, 3).T
        print('Eigenvector {}: \n{}'.format(i + 1, eig_vec_cov[i]))
        print('Eigenvalue {} from covariance matrix: {}'.format(i + 1, eig_val_cov[i]))
    eig_pairs = [(np.abs(eig_val_cov[i]), eig_vec_cov[:, i]) for i in range(len(eig_val_cov))]
    eig_pairs.sort(key=lambda x: x[0], reverse=True)
    #for i in eig_pairs:
    #   print(i[0])

    matrix_w = np.hstack((eig_pairs[0][1].reshape(3, 1), eig_pairs[1][1].reshape(3, 1)))
    print "**************************************************"
    print "2 dimensional eigen vector: \n ", matrix_w



ReadFile()
PCA()