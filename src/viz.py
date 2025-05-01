import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar(data, x_col, y_col, title, xlabel, ylabel, save_path=None):
    """
    Función para crear un gráfico de barras.
    """
    plt.figure(figsize=(15, 6))
    sns.barplot(x=data[x_col], y=data[y_col], palette='Blues')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True)
    if save_path:
        plt.savefig(save_path)
    plt.show()
