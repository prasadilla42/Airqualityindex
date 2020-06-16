{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "from plot_AQI import avg_data_2013,avg_data_2014,avg_data_2015,avg_data_2016,avg_data_2017,avg_data_2018\n",
    "import requests\n",
    "import sys\n",
    "import pandas as pd \n",
    "from bs4 import BeautifulSoup\n",
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "def met_data(month, year):\n",
    "    \n",
    "    file_html = open('./Data/Html_Data/{}/{}.html'.format(year,month), 'rb')\n",
    "    plain_text = file_html.read()\n",
    "\n",
    "    tempD = []\n",
    "    finalD = []\n",
    "\n",
    "    soup = BeautifulSoup(plain_text, \"lxml\")\n",
    "    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):\n",
    "        for tbody in table:\n",
    "            for tr in tbody:\n",
    "                a = tr.get_text()\n",
    "                tempD.append(a)\n",
    "\n",
    "    rows = len(tempD) / 15\n",
    "\n",
    "    for times in range(round(rows)):\n",
    "        newtempD = []\n",
    "        for i in range(15):\n",
    "            newtempD.append(tempD[0])\n",
    "            tempD.pop(0)\n",
    "        finalD.append(newtempD)\n",
    "\n",
    "    length = len(finalD)\n",
    "\n",
    "    finalD.pop(length - 1)\n",
    "    finalD.pop(0)\n",
    "\n",
    "    for a in range(len(finalD)):\n",
    "        finalD[a].pop(6)\n",
    "        finalD[a].pop(13)\n",
    "        finalD[a].pop(12)\n",
    "        finalD[a].pop(11)\n",
    "        finalD[a].pop(10)\n",
    "        finalD[a].pop(9)\n",
    "        finalD[a].pop(0)\n",
    "\n",
    "    return finalD"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "def data_combine(year, cs):\n",
    "    for a in pd.read_csv('./Data/Real-Data/real_' + str(year) + '.csv', chunksize=cs):\n",
    "        df = pd.DataFrame(data=a)\n",
    "        mylist = df.values.tolist()\n",
    "    return mylist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    if not os.path.exists(\"./Data/Real-Data\"):\n",
    "        os.makedirs(\"./Data/Real-Data\")\n",
    "    for year in range(2013, 2019):\n",
    "        final_data = []\n",
    "        with open('./Data/Real-Data/real_' + str(year) + '.csv', 'w') as csvfile:\n",
    "            wr = csv.writer(csvfile, dialect='excel')\n",
    "            wr.writerow(\n",
    "                ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])\n",
    "        for month in range(1, 13):\n",
    "            temp = met_data(month, year)\n",
    "            final_data = final_data + temp\n",
    "            \n",
    "        pm = getattr(sys.modules[__name__], 'avg_data_{}'.format(year))()\n",
    "\n",
    "        if len(pm) == 364:\n",
    "            pm.insert(364, '-')\n",
    "\n",
    "        for i in range(len(final_data)-1):\n",
    "            # final[i].insert(0, i + 1)\n",
    "            final_data[i].insert(8, pm[i])\n",
    "\n",
    "        with open('./Data/Real-Data/real_' + str(year) + '.csv', 'a') as csvfile:\n",
    "            wr = csv.writer(csvfile, dialect='excel')\n",
    "            for row in final_data:\n",
    "                flag = 0\n",
    "                for elem in row:\n",
    "                    if elem == \"\" or elem == \"-\":\n",
    "                        flag = 1\n",
    "                if flag != 1:\n",
    "                    wr.writerow(row)\n",
    "                    \n",
    "    data_2013 = data_combine(2013, 600)\n",
    "    data_2014 = data_combine(2014, 600)\n",
    "    data_2015 = data_combine(2015, 600)\n",
    "    data_2016 = data_combine(2016, 600)\n",
    "    data_2017 = data_combine(2017, 600)\n",
    "    data_2018 = data_combine(2016, 600)\n",
    "     \n",
    "    total=data_2013+data_2014+data_2015+data_2016+data_2017+data_2018\n",
    "    \n",
    "    with open('./Data/Real-Data/Real_Combine.csv', 'w') as csvfile:\n",
    "        wr = csv.writer(csvfile, dialect='excel')\n",
    "        wr.writerow(\n",
    "            ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])\n",
    "        wr.writerows(total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
