{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ffb2f9cf",
   "metadata": {},
   "source": [
    "# multiplication tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1086ce19",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(2,21):\n",
    "    with open(f\"Multitable for {i}.txt\", \"w\") as f:\n",
    "        for j in range(1,11):\n",
    "            f.write(f\"{i}x{j}={i*j}\\n\")"
   ]
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
