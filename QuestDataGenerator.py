from Quest import Quest

class QuestConditions:
    def __init__(self, name):
        self.name = name



def QuestDataGenerator(quests: list):
    arr = []
    for quest in quests:
        print(quest)
