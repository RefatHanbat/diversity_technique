{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fea51ded",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cdc7076a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import copy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d2fa9f03",
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.special import comb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "eb04d771",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [4]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mfParam\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;241m*\u001b[39m\n",
      "File \u001b[1;32m~\\diversity technique\\diversity_technique\\assignment_05\\fParam.py:43\u001b[0m, in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m {\n\u001b[0;32m      2\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcells\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m      3\u001b[0m   {\n\u001b[0;32m      4\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      5\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m1\u001b[39m,\n\u001b[0;32m      6\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m74682a7a\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      7\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m      8\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m      9\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     10\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mimport numpy as np\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     11\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m####fParam.py###\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     12\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef myf_sys_param():\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     13\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     14\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    ###Function###\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     15\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     16\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    sys_param = \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     17\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     18\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    sys_param[\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mNant\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m] = 4 #Multiple Tx or Rx antenna : 2,4\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     19\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     20\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    sys_param[\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mEs\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m] = 1 # Average transmit energy [Joule]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     21\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     22\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    sys_param[\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mEsoverNO_dB\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m] = 5 # Es/NO[dB]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     23\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     24\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    sys_param[\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mEsoverNO\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m] = 10**(sys_param[\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mEsoverNO_dB\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m]/ 10) #[no unit]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     25\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     26\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    sys_param[\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mNO\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m] = sys_param[\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mEs\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m]/sys_param[\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mEsoverNO\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m]#Noise energy [Joule]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     27\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     28\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    sys_param[\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mconstellation_type\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m] == \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mQPSK\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m #constellation type: \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mBpsk\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m / \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mQPSK\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     29\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     30\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    if (sys_param[\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mconstellation_type\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m] == \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mBPSK\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m): #constellation size\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     31\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     32\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        sys_param[\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mconstellation_size\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m] =2\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     33\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     34\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    elif(sys_param[\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mconstellation_type\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m] == \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mQPSK\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     35\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     36\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        sys_param[\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mconstellation_size\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m] = 4\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     37\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     38\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    return(sys_param)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     39\u001b[0m    ]\n\u001b[0;32m     40\u001b[0m   },\n\u001b[0;32m     41\u001b[0m   {\n\u001b[0;32m     42\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m---> 43\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[43mnull\u001b[49m,\n\u001b[0;32m     44\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m78e6ada7\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     45\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m     46\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m     47\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: []\n\u001b[0;32m     48\u001b[0m   }\n\u001b[0;32m     49\u001b[0m  ],\n\u001b[0;32m     50\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     51\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mkernelspec\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     52\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_name\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPython 3 (ipykernel)\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     53\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     54\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     55\u001b[0m   },\n\u001b[0;32m     56\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage_info\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     57\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcodemirror_mode\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     58\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     59\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m3\u001b[39m\n\u001b[0;32m     60\u001b[0m    },\n\u001b[0;32m     61\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfile_extension\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m.py\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     62\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmimetype\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/x-python\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     63\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     64\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbconvert_exporter\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     65\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpygments_lexer\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython3\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     66\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3.9.12\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     67\u001b[0m   }\n\u001b[0;32m     68\u001b[0m  },\n\u001b[0;32m     69\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m4\u001b[39m,\n\u001b[0;32m     70\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat_minor\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m5\u001b[39m\n\u001b[0;32m     71\u001b[0m }\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "from fParam import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd162b10",
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
