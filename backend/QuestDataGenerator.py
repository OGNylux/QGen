import json


class QuestConditions:
    def __init__(self, name: str, conditions: list, reward: list, notFinishedTexts: int):
        self.name = name
        self.conditions = conditions
        self.reward = reward
        self.notFinishedTexts = notFinishedTexts


def QuestDataGenerator(quests: list):
    arr = []
    for quest in quests:
        conditionItems = quest['itemConditions']
        conditionTags = quest['tagConditions']
        rewardItems = quest['itemRewards']
        rewardTags = quest['tagRewards']
        newConditions = [{'items': conditionItems}, {'tags': conditionTags}]
        newRewards = [{'items': rewardItems}, {'tags': rewardTags}]
        notFinishedTexts = len(quest['progressDialogue'])

        qConditions = QuestConditions(quest['name'], newConditions, newRewards, notFinishedTexts)
        arr.append(json.dumps(qConditions.__dict__, indent=4))
    test = ''.join(arr)
    jsFile = f'export const QGenQuestConditions = {test}'
    return jsFile
