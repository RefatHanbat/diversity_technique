{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2f22c281",
   "metadata": {},
   "outputs": [],
   "source": [
    "def myf_channel(sys_param,param_channel):\n",
    "\n",
    "  Nant = sys_param[\"Nant\"]\n",
    "\n",
    "  seed_seq = param_channel[\"seed_seq\"]\n",
    "\n",
    "  rng = np.random.default_rng(seed=seed_seq)\n",
    "\n",
    "  channel = {}\n",
    "\n",
    "  PL = 1\n",
    "\n",
    "  H_mat = rng.normal(loc=0, scale=np.sqrt(1/2),size=(Nant,1)) +1j * rng.normal(loc=0, scale=np.sqrt(1/2), size=(Nant,1))\n",
    "\n",
    "  H_mat = np.sqrt(PL) + H_mat\n",
    "\n",
    "  channel[\"H_mat_SISO\"] = H_mat[0][0]\n",
    "\n",
    "  channel[\"H_mat_SIMO\"] = np.copy(H_mat)\n",
    "\n",
    "  channel[\"H_mat_MISO\"] = np.transpose(H_mat)\n",
    "\n",
    "  if(Nant==2):\n",
    "    channel[\"H_mat_Alamouti\"] = np.transpose(H_mat)\n",
    "  elif(Nant ==4):\n",
    "    channel[\"H_mat_Alamouti\"] = np.vstack(np.transpose(H_mat[0:2],np.transpose(H_mat[2:4])))\n",
    "\n",
    "  return channel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a94774a0",
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
