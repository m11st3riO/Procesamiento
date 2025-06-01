import numpy as np
import matplotlib.pyplot as plt
from src.utils.Graficas import Grap_s, Grap_c, Grap_e, Grap_t


def tarea_1():
    t_s= -1
    t_e = 5
    Ts = 0.01
    f = 2
    a = 2

    t_cont = np.linspace(t_s, t_e, 1000)

    n = np.arange(t_s/Ts, t_e/Ts + 1)
    t_disc = n * Ts


    fig, axs = plt.subplots(4, 1, figsize=(14, 14))
    fig.suptitle(f"Tarea 1 \n Señales continuas y discretas Frecuencia = {f}, Amplitud = {a}", fontsize=16)

    axs[0].plot(t_cont, Grap_s(t_cont,f,a), "b-", label="Continua", linewidth=1.5)
    axs[0].plot(t_disc, Grap_s(t_disc,f,a), "mo", markersize=3, label="Muestras")
    axs[0].set_title(f"Funcion Seno")
    axs[0].grid(True, linestyle="--", alpha=0.7)
    axs[0].legend()
    axs[0].set_xlim(t_s, t_e)

    axs[1].plot(t_cont, Grap_e(t_cont), "b-", linewidth=1.5)
    axs[1].plot(t_disc, Grap_e(t_disc), "mo", markersize=3)
    axs[1].set_title("Funcion Exponencial Decreciente")
    axs[1].grid(True, linestyle="--", alpha=0.7)
    axs[1].set_xlim(t_s, t_e)


    axs[2].plot(t_cont, Grap_t(t_cont,f), "b-", linewidth=1.5)
    axs[2].plot(t_disc, Grap_t(t_disc,f), "mo", markersize=3)
    axs[2].set_title("Funcion Triangular")
    axs[2].grid(True, linestyle="--", alpha=0.7)
    axs[2].set_xlim(t_s, t_e)


    axs[3].plot(t_cont, Grap_c(t_cont,f), "b-", linewidth=1.5)
    axs[3].plot(t_disc, Grap_c(t_disc,f), "mo", markersize=3)
    axs[3].set_title("Funcion cuadratica")
    axs[3].grid(True, linestyle="--", alpha=0.7)
    axs[3].set_xlim(t_s, t_e)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()