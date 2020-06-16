{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import time\n",
    "import requests\n",
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "def retrieve_html():\n",
    "    for year in range(2013,2019):\n",
    "        for month in range(1,13):\n",
    "            if(month<10): \n",
    "                url='https://en.tutiempo.net/climate/0{}-{}/ws-37720.html'.format(month,year)\n",
    "            else:\n",
    "                url='https://en.tutiempo.net/climate/{}-{}/ws-37720.html'.format(month,year)  \n",
    "        \n",
    "            texts=requests.get(url)\n",
    "            text_utf=texts.text.encode('utf=8')\n",
    "        \n",
    "            if not os.path.exists(\"./Data/Html_Data/{}\".format(year)):\n",
    "                os.makedirs(\"./Data/Html_Data/{}\".format(year))\n",
    "            with open(\"./Data/Html_Data/{}/{}.html\".format(year,month),\"wb\") as output:\n",
    "                output.write(text_utf)\n",
    "            \n",
    "        sys.stdout.flush()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__==\"__main__\":\n",
    "    start_time=time.time()\n",
    "    retrieve_html()\n",
    "    stop_time=time.time()\n",
    "    print(\"Time taken {}\".format(stop_time-start_time))"
   ]
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
