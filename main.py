# This is a sample Python script.
from Quest import Quest
from QuestDataGenerator import QuestDataGenerator

test = Quest(questName="Brot Disaster", questDesc="Hol Brot", questDialogue=["Hab ein Problem", "haaa"],
             questUnfinishedDialogue=["Bitte hilf mir", "Kein Brot mehr", "Bitte"], questFinishedDialogue=["Danke", "Jetzt hab ich Brot"],
             questCondition=[{"minecraft:apple": 64}, {"minecraft:carrot": 64}], reward=[{"minecraft:diamond": 32}])
test2 = Quest(questName="Brot Disaster1", questDesc="Hol Brot", questDialogue=["Hab ein Problem", "Kein Brot mehr", "Hilfe"],
             questUnfinishedDialogue=["Bitte hilf mir", "Kein Brot mehr", "Bitte"], questFinishedDialogue=["Danke"],
             questCondition=[{"minecraft:apple": 64}, {"minecraft:carrot": 64}], reward=[{"minecraft:diamond": 32}])
test3 = Quest(questName="Brot Disaster2", questDesc="Hol Brot", questDialogue=["Hab ein Problem", "Hilfe"],
             questUnfinishedDialogue=["Bitte hilf mir", "Kein Brot mehr", "Bitte"], questFinishedDialogue=["Danke", "Danke", "Jetzt hab ich Brot"],
             questCondition=[{"minecraft:apple": 64}, {"minecraft:carrot": 64}], reward=[{"minecraft:diamond": 32}])

testDict = []

testDict.append(test)
testDict.append(test2)
testDict.append(test3)

QuestDataGenerator(testDict)


