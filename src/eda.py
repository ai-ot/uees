import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(path):
    return pd.read_csv(path)

def plot_correlation_matrix(df, save_path=None):
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0, fmt='.2f')
    plt.title("Matriz de Correlación")
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()

def plot_boxplots(df, features, target, save_path=None):
    plt.figure(figsize=(12, 8))
    for i, feat in enumerate(features):
        plt.subplot(2, 2, i+1)
        sns.boxplot(x=target, y=feat, data=df)
        plt.title(f'{feat} por Fallo')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()
