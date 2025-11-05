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
