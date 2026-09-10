#Excersise 1
#Take in a list of sentences(strings)
#return all possible training input/output pairs for each sentence
#return the total number of training/output pairs and the number of words
def LLMDataCounter(sentenceList):
    #Tracking variables
    wordCount = 0
    trainingData = []
    #Go through each sentence
    for i in range(0, len(sentenceList)):
        #count the number of words and split by word
        words = sentenceList[i].split()
        #update the word count
        wordCount += len(words)
        #generale all possible pieces of training data for each sentence
        for i in range(1, len(words)):
            trainingData.append(' '.join(words[:i]))
#Finally compute the amount of training data
    numTrainingSamples = len(trainingData)
    return wordCount, numTrainingSamples, trainingData

sentenceList = ["Hello how are you", "What is up"]
wordCount, numTrainingSamples, trainingData = LLMDataCounter(sentenceList)
print("wordCount =", wordCount)
print("numTrainingSamples =", numTrainingSamples)
print("trainingData =", trainingData)

class Doc():
   def __init__(self, docName, numSentences, wordsPerSentence):
        self.docName = docName
        self.numSentences = numSentences
        self.wordsPerSentence = wordsPerSentence

# Excercise 2
import itertools
docNames = ["doc1","doc2","doc3","doc4","doc5","doc6","docs7"] #all possible elements
sentencePerDocList = [72,52,75,40,61,55,68]
wordPerSentenceList = [13,20,22,28,25,19,17]
allDocsObjectList = []
#fill in the document class
for i in range(0, len(docNames)):
    allDocsObjectList.append(Doc(docNames[i], sentencePerDocList[i], wordPerSentenceList[i]))

def ComputeTrainingCombinations(allDocsObjectList):
    r = 3 #Tod: set the correct value of r
    allRCombinationsList = [] #list that contains the solution
    for subset in itertools.combinations(allDocsObjectList, r):
        #Get the subset which is one of the r combinations
        #convert that r combination into a list and add it to our solution
        #Todo: get the r combination list using itertool function
        allRCombinationsList.append(list(subset))   
    return allRCombinationsList

#Print the solution
allRCombinationsList = ComputeTrainingCombinations(allDocsObjectList)
for i in range(0, len(allRCombinationsList)):
    for x in allRCombinationsList[i]: print(x.docName)
    print("=====")


# Extra credit
#Compute the number of training samples each 3-combination generates. 
#Then return the best 3-combination that the company should translate 
#and how many training samples will be obtained from the best 3-combination.  
def ComputeBestCombination(allDocsObjectList):
    allRCombinationsList = ComputeTrainingCombinations(allDocsObjectList)
    bestCombination = allRCombinationsList[0]
    mostTrainingSamples = 0
    for combination in allRCombinationsList:
        totalTrainingSamples = 0
        for doc in combination:
            sentenceList = []
            sentenceList = ["word " * doc.wordsPerSentence] * doc.numSentences
            wordCount, currentTrainingSamples, trainingData = LLMDataCounter(sentenceList)
            totalTrainingSamples += currentTrainingSamples
        if totalTrainingSamples > mostTrainingSamples:
            mostTrainingSamples = totalTrainingSamples
            bestCombination = combination
    return bestCombination, mostTrainingSamples

bestCombination, mostTrainingSamples = ComputeBestCombination(allDocsObjectList)
print("Best Combination: ")
for doc in bestCombination: 
    print(doc.docName)
print("Most Training Samples: ", mostTrainingSamples)