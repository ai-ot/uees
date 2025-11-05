import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
def plot_decision_boundary(model, X, y, title, save_path=None):
X1, X2 = np.meshgrid(
np.arange(start=X[:, 0].min()-1, stop=X[:, 0].max()+1, step=0.01),
np.arange(start=X[:, 1].min()-1, stop=X[:, 1].max()+1, step=0.01)
)
plt.contourf(X1, X2, model.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
alpha=0.75, cmap=ListedColormap(('red', 'green')))
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=ListedColormap(('red','green')))
plt.title(title)
plt.xlabel('Air temperature [K] (escalado)')
plt.ylabel('Process temperature [K] (escalado)')
if save_path:
plt.savefig(save_path, bbox_inches='tight')
plt.show()
EOFcat > notebooks/01_eda.ipynb << 'EOF'
{
"cells": [
{
"cell_type": "markdown",
"metadata": {},
"source": ["# 1. Análisis Exploratorio de Datos (EDA)"]
},
{
"cell_type": "code",
"metadata": {},
"outputs": [],
"source": [
"import sys\nsys.path.append('../src')\nfrom eda import *\nimport pandas as pd\n\ndf = load_data('../data/DataSet_Caso_Practico.csv')\ndf.head()"
]
},
{
"cell_type": "code",
"metadata": {},
"outputs": [],
"source": ["print("Información:")\ndf.info()"]
},
{
"cell_type": "code",
"metadata": {},
"outputs": [],
"source": ["print("\nDistribución de fallos:")\nprint(df['Machine failure'].value_counts(normalize=True))"]
},
{
"cell_type": "code",
"metadata": {},
"outputs": [],
"source": [
"features = ['Air temperature [K]', 'Process temperature [K]', \n            'Rotational speed [rpm]', 'Torque [Nm]']\nplot_correlation_matrix(df[features + ['Machine failure']], \n                        save_path='../results/correlation_matrix.png')"
]
},
{
"cell_type": "code",
"metadata": {},
"outputs": [],
"source": [
"plot_boxplots(df, features, 'Machine failure', \n              save_path='../results/boxplots.png')"
]
}
],
"metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
"nbformat": 4,
"nbformat_minor": 2
}
