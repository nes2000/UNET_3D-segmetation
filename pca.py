import pandas as pd
from sklearn.decomposition import PCA

data = pd.read_csv('/kaggle/input/data-csv/data.csv')

non_numeric_columns = ['img']
numeric_columns = [col for col in data.columns if col not in non_numeric_columns]
X = data[numeric_columns]

pca = PCA(n_components=200)  # Set n_components to 100 for 100 dimensions

X_pca = pca.fit_transform(X)

df_pca = pd.DataFrame(X_pca, columns=['PC{}'.format(i+1) for i in range(200)])  # Adjust column names to PC1, PC2, ..., PC100

df_pca.to_csv('path_to_save_pca_data.csv', index=False)
