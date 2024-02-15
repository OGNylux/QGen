class Quest:
    def __init__(self, questName: str, questDesc: str, questDialogue: list[str],
                 questUnfinishedDialogue: list[str], questFinishedDialogue: list[str], reward: list,
                 questCondition: list[dict]):
        self.questName = questName
        self.questDesc = questDesc
        self.questDialogue = questDialogue
        self.questUnfinishedDialogue = questUnfinishedDialogue
        self.questFinishedDialogue = questFinishedDialogue
        self.reward = reward
        self.questCondition = questCondition

    def getName(self) -> str:
        return self.questName

    def getDesc(self) -> str:
        return self.questDesc

    def getDialogue(self) -> list[str]:
        return self.questDialogue

    def getUnfinishedDialogue(self) -> list[str]:
        return self.questUnfinishedDialogue

    def getFinishedDialogue(self) -> list[str]:
        return self.questFinishedDialogue

    def getReward(self) -> list:
        return self.reward

    def getQuestCondition(self) -> list:
        return self.questCondition


