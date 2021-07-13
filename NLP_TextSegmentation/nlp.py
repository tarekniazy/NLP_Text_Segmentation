from math import log
import time
# assume that all words in a string are independently distributed
# we need to calculate the relative frequency of all words


startPeriod = time.time()

dataset = open("dataset.txt").read().split()




unigram={}  # It is a dictionary which holds the word and a cost value 
              # Calculated from Zipf's law : P(word's_frequency) * word's_rank = constant
              # the data set (words-by-frequency.txt) contains a splitted text and holds anly a unique words
              # the words are sorted ascendingly by their ranks
              # the rank= itemCount+1 -- counting starts from 0
              
 

maximum_word_len=0

# bulding the unigram model ; each word holds its cost value.
for count,word in enumerate(dataset):
    unigram[word]=log((count+1)*(log(len(dataset))))


for x in dataset:
    if len(x)>maximum_word_len:
        maximum_word_len=len(x)
        # print(maxword)


def Split_with_no_Spaces(s):
       
    s=s.lower()
    s=s.strip()
    s=s.replace(" ","")
    s=s.replace("-","")
    s=s.replace("’","")
    s=s.replace("@","")
    s=s.replace("#","")
    s=s.replace("_","")
    s=s.replace("%","")
    s=s.replace("*","")
    s=s.replace(";","")
    s=s.replace("(","")
    s=s.replace(")","")
    s=s.replace("{","")
    s=s.replace("}","")
    s=s.replace("]","")
    s=s.replace("[","")
    s=s.replace("\n","")
    s=s.replace("/","")
    s=s.replace("?","")
    s=s.replace(">","")
    s=s.replace("<","")
    s=s.replace("!","")
    s=s.replace(",","")


    # Build the history table
    def WordMatch(i):

        
        possibleWords = historyTable[max(0, i-maximum_word_len):i]
        
        reversed_possibleWords=possibleWords[::-1]

        min=(reversed_possibleWords[0] + unigram.get(s[i-1:i], 9e999),1) 
        

        for k,c in enumerate(reversed_possibleWords):
            if min > (c + unigram.get(s[i-k-1:i], 9e999),k+1):
                min=(c + unigram.get(s[i-k-1:i], 9e999),k+1)       
        return min




    historyTable = [0]    
    for i in range(1,len(s)+1):
        cost,index = WordMatch(i)
        historyTable.append(cost)

    # perform backtracking to get the minimum cost.
    splitted_list = []
    i = len(s)
    while i>0:
        cost,index = WordMatch(i)
        if cost == historyTable[i]:
            splitted_list.append(s[i-index:i])
        i -= index

    return splitted_list[::-1]
#s = 'PriorresearchpointstoefficientidentificationofembeddedwordsasakeyfactorinfacilitatingthereadingoftextprintedwithoutspacingbetweenwordsHerewefurthertestedtheprimaryroleofbottomupwordidentificationbyalteringthisprocesswithalettertranspositionmanipulationIntwoexperimentsweexaminedsilentreadingandreadingaloudofnormalsentencesandsentencescontainingwordswithlettertranspositionsinbothnormallyspacedandunspacedconditionsWepredictedthatlettertranspositionsshouldbeparticularlyharmfulforreadingunspacedtextInlinewithourpredictionthemajorityofourmeasuresofreadingfluencyshowedthatunspacedtextwithlettertranspositionswasdisproportionatelydifficulttoreadThesefindingsprovidefurthersupportfortheclaimthatreadingtextwithoutbetweenwordspacingreliesprincipallyonefficientbottomupprocessingenablingaccuratewordidentificationintheabsenceofvisualcuestoidentifywordboundariesPriorresearchpointstoefficientidentificationofembeddedwordsasakeyfactorinfacilitatingthereadingoftextprintedwithoutspacingbetweenwordsHerewefurthertestedtheprimaryroleofbottomupwordidentificationbyalteringthisprocesswithalettertranspositionmanipulationIntwoexperimentsweexaminedsilentreadingandreadingaloudofnormalsentencesandsentencescontainingwordswithlettertranspositionsinbothnormallyspacedandunspacedconditionsWepredictedthatlettertranspositionsshouldbeparticularlyharmfulforreadingunspacedtextInlinewithourpredictionthemajorityofourmeasuresofreadingfluencyshowedthatunspacedtextwithlettertranspositionswasdisproportionatelydifficulttoreadThesefindingsprovidefurthersupportfortheclaimthatreadingtextwithoutbetweenwordspacingreliesprincipallyonefficientbottomupprocessingenablingaccuratewordidentificationintheabsenceofvisualcuestoidentifywordboundaries.'
s="Themainunifyingthemeistheideaofanintelligentagent.WedefineAIasthestudyofagentsthatreceiveperceptsfromtheenvironmentandperformactions.Eachsuchagentimplementsafunctionthatmapsperceptsequencestoactions,andwecoverdifferentwaystorepresentthesefunctions,suchasreactiveagents,real-timeplanners,anddecision-theoreticsystems.Weexplaintheroleoflearningasextendingthereachofthedesignerintounknownenvironments,andweshowhowthatroleconstrainsagentdesign,favoringexplicitknowledgerepresentationandreasoning.Wetreatroboticsandvisionnotasindependentlydefinedproblems,butasoccurringintheserviceofachievinggoals.Westresstheimportanceofthetaskenvironmentindeterminingtheappropriateagentdesign.OurprimaryaimistoconveytheideasthathaveemergedoverthepastfiftyyearsofAIresearchandthepasttwomillenniaofrelatedwork.Wehavetriedtoavoidexcessiveformalityinthepresentationoftheseideaswhileretainingprecision.Wehaveincludedpseudocodealgorithmstomakethekeyideasconcrete;ourpseudocodeisdescribedinAppendixB.Thisbookisprimarilyintendedforuseinanundergraduatecourseorcoursesequence.Thebookhas27chapters,eachrequiringaboutaweek’sworthoflectures,soworkingthroughthewholebookrequiresatwo-semestersequence.Aone-semestercoursecanuseselectedchapterstosuittheinterestsoftheinstructorandstudents.Thebookcanalsobeusedinagraduate-levelcourse(perhapswiththeadditionofsomeoftheprimarysourcessuggestedinthebibliographicalnotes).Samplesyllabiareavailableatthebook’sWebsite,aima.cs.berkeley.edu.Theonlyprerequisiteisfamiliaritywithbasicconceptsofcomputerscience(algorithms,datastructures,complexity)atasophomorelevel.Freshmancalculusandlinearalgebraareusefulforsomeofthetopics;therequiredmathematicalbackgroundissuppliedinAppendixA.Exercisesaregivenattheendofeachchapter.Exercisesrequiringsignificantprogrammingaremarkedwithakeyboardicon.Theseexercisescanbestbesolvedbytakingadvantageofthecoderepositoryataima.cs.berkeley.edu.Someofthemarelargeenoughtobeconsideredtermprojects.Anumberofexercisesrequiresomeinvestigationoftheliterature;thesearemarkedwithabookicon.Throughoutthebook,importantpointsaremarkedwithapointingicon.Wehaveincludedanextensiveindexofaround6,000itemstomakeiteasytofindthingsinthebook.Whereveranewtermisfirstdefined,NEWTERMitisalsomarkedinthemargin.AbouttheWebsiteaima.cs.berkeley.edu,theWebsiteforthebook,contains"
print(Split_with_no_Spaces(s))
print(time.time()-startPeriod)