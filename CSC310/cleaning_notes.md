{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f28700b2-a222-4e1b-b23f-588df7e00a40",
   "metadata": {},
   "source": [
    "What are 3 common problems to look for in a dataset? Describe them with examples.\n",
    "\n",
    "1. Incorrect handling of blank values such as using a '-' rather than leaving it. This is a problem because it can make it so the column is read in as an object rather than a float. When changed to NaN the column can be read as a float.\n",
    "2. Another problem is duplicated data. When I was peer reviewing for the last assignment, my partners data had two games that were actually the exact same game and title, but they were listed seperately since they had been released on different platforms.\n",
    "3. inconsistencies in the data being listed for example USA vs United States would be listed different but are the same place. Another example I can think of is some data having a period at the end but others not.\n",
    "\n",
    "\n",
    "Using one of the examples you found of cleaned data, give an example of a question or context that would require making different choices for cleaning than were made. Include a bit about the data, what was done, the question, what would need to be done instead and justification.\n",
    "\n",
    "I looked at clean_artist.csv and messy_artist.csv. I noticed that in the artists file, when it was cleaned they had completely removed columns that did not have any artists that fit the description. For example in the messy file, there were no artists that were from Arkansas, were Hispanic, and an architect. The artists_n variable was left blank. In the cleaned version, the whole row was removed from the file. If we were trying to research which states had a lack of artists in certain fields or a certain race, we would actually want to look at the rows that had no artists that fell under that category, so when cleaning the file we would want to list the artists_n as 0.\n",
    "\n",
    "\n",
    "Explain in your own words, with a concrete example, how domain expertise can help you when cleaning data. Use either a made up example or one that you read about.\n",
    "An example that I can think of is a data file of all the classes listed at URI. As a student you would want to look through the files to see which are required for your major, how many credits they have, and more attributes about the classes. When cleaning the data, you could notice that some credits are listed as 3 and some as 3.0. When cleaning the data, using domain expertise you could cast all of the credits as integers that way there are no inconsistencies in the data that would cause issues when trying to search for classes with 3 credits."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a6fadec-13bc-432c-9912-a2db066ab967",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
