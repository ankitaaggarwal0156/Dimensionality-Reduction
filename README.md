# Dimensionality-Reduction
PCA and FastMap


PCA
Use PCA to reduce the dimensionality of the data points in pca-data.txt from 3D to 2D. Each line of
the data file represents the 3D coordinates of a single point. Please output the directions of the first two
principal components.

FastMap
Use FastMap to embed the objects in fastmap-data.txt into a 2D space. The first two columns in each
line of the data file represent the IDs of the two objects; and the third column indicates the symmetric
distance between them. If the furthest pair of objects is ambiguous, please use the one that includes the
smallest object ID.

The objects listed in fastmap-data.txt are actually the words in fastmap-wordlist.txt (nth
word in this list has an ID value of n) and the distances between each pair of objects are the Damerau–
Levenshtein distances between them. You can try to plot the words onto a 2D plane using your previous
FastMap solution and see what it looks like.
