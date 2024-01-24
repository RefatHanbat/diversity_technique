{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "373641fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2c0c5257",
   "metadata": {},
   "outputs": [],
   "source": [
    "def myf_plot_BER(sys_param, x_axis_cand, Num_errors_bit,Num_errors_bit_th,x_axis_name):\n",
    "    \n",
    "    ###Parameters###\n",
    "    ###Functions###\n",
    "    \n",
    "    fig, axes = plt.subplots(1,1)\n",
    "    \n",
    "    axes.semilogy(x_axis_cand,Num_errors_bit[0],'b+-', markersize=12, markerfacecolor=\"None\", label=r'SISO')\n",
    "    \n",
    "    if(sys_param[\"constellation_type\"]==\"BPSK\"):\n",
    "        \n",
    "        axes.semilogy(x_axis_cand,Num_errors_bit_th[0],'b+--',markersize=12,markerfacecolor=\"None\", label=r'SISO(theory)')\n",
    "        \n",
    "        \n",
    "    axes.semilogy(x_axis_cand,Num_errors_bit[1],'r1--',markersize=12,markerfacecolor=\"None\", label=r'SIMO_SC')\n",
    "    \n",
    "    if(sys_param[\"constellation_type\"]==\"BPSK\"):\n",
    "        \n",
    "        axes.semilogy(x_axis_cand,Num_errors_bit_th[1],'r1--',markersize=12,markerfacecolor=\"None\", label=r'SISO(theory)')\n",
    "        \n",
    "        \n",
    "    axes.semilogy(x_axis_cand,Num_errors_bit[2],'r2-',markersize=12,markerfacecolor=\"None\", label=r'SIMO_EGC')\n",
    "    \n",
    "    if(sys_param[\"constellation_type\"]==\"BPSK\"):\n",
    "        \n",
    "        if(sys_param[\"Nant\"==2]):\n",
    "            \n",
    "            axes.semilogy(x_axis_cand,Num_errors_bit_th[2],'r2--',markersize=12,markerfacecolor=\"None\",\n",
    "                         label=r'SIMO-EGC(theory)')\n",
    "        axes.semilogy(x_axis_cand,Num_errors_bit[3],'r3-',markersize=12,markerfacecolor=\"None\",label=r'SIMO-MRC')\n",
    "        \n",
    "        if(sys_param[\"constellation_type\"]==\"BPSK\"):\n",
    "            axes.semilogy(x_axis_cand,Num_errors_bit_th[3],'r3--',markersize=12,markerfacecolor=\"None\",label=r\"SIMO-MRC(theory)\")\n",
    "        axes.semilogy(x_axis_cand,Num_errors_bit[4],'m^-',markersize=12,markerfacecolor=\"None\",label=r'MISO-EPA')\n",
    "        \n",
    "        axes.semilogy(x_axis_cand,Num_errors_bit[5],'mv-',markersize=12,markerfacecolor=\"None\",label=r'Alamoutii')\n",
    "        \n",
    "        axes.semilogy(x_axis_cand,Num_errors_bit[6],'ko-',markersize=12,markerfacecolor=\"None\",label=r'MISO-MRT')\n",
    "        \n",
    "        axes.grid()\n",
    "        \n",
    "        if(x_axis_name==\"EsoverN0_dB_cand\"):\n",
    "            \n",
    "            axes.legend(loc=\"best\")\n",
    "            #axes.legend(loc=\"lower right\"),fontsize=6)\n",
    "            axes.set_xlabel(r'SNR,s\\frac{E_b}{N_0}s [dB]')\n",
    "        elif(x_axis_name==\"EboverN0_dB_cand\"):\n",
    "            axeslegend(loc=\"best\")\n",
    "            #axes.legend(loc=\"Lower right\",fontsize=6)\n",
    "            \n",
    "            axes.set_xlabel(r'SNR,s\\frac{E_b}{N_0}s [dB]')\n",
    "        axes.set_ylabel(r'BER')\n",
    "        \n",
    "        axes.set_xlim(min(x_axis_cand),max(x_axis_cand))\n",
    "        \n",
    "        axes.set_ylim(10**(-5),1)\n",
    "        \n",
    "        plot.savefig(\"fig_BER.png\",dpi=300)\n",
    "        \n",
    "        plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "84463b00",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
