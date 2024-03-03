import json


def QuestDialogueGenerator(npc: dict, quests: list):
    arr = []
    for index, quest in enumerate(quests):
        scenes = (createIntroDialogue(npc, quest) + createProgressDialogue(npc, quest) +
                  createFinishedDialogue(npc, quest, quests, index))
        test = json.dumps({
            "format_version": "1.17.100",
            "minecraft:npc_dialogue": {
                "scenes": scenes
            }
        }, indent=4)
        arr.append(test)
    return arr


def createIntroDialogue(npc: dict, quest: dict):
    arr = []
    questName = quest['name'].replace(" ", "_").lower()
    for index, dialogue in enumerate(quest['dialogue']):
        arr.append({
            "scene_tag": f'QGen.{questName}.intro{index}',
            "npc_name": {"rawtext": [{"translate": f'entity.{npc["namespace"]}:{npc["identifier"]}.name'}]},
            "text": {"rawtext": [{"translate": f'QGen.{npc["identifier"]}.{questName}.intro{index}'}]},
            "on_open_commands": ["/playsound mob.villager.yes @initiator"],
            "on_close_commands": createIntroCloseCommands(quest, index, questName),
            "buttons": createIntroButtons(quest, index, questName)
        })
    return arr


def createIntroCloseCommands(quest: dict, index: int, questName: str):
    if index < (len(quest['dialogue']) - 1):
        return []
    else:
        return ["/tag @s add inProgress", f'/tag @a[tag=host] add QGen_{questName}', "/function showQuest"]


def createIntroButtons(quest: dict, index: int, questName: str):
    if index < (len(quest['dialogue']) - 1):
        return [
            {
                "name": {"rawtext": [{"translate": "QGen.dialogue.ok"}]},
                "commands": [
                    f'/dialogue open @s @initiator QGen_{questName}.intro{index}'
                ]
            },
            {
                "name": {"rawtext": [{"translate": "dialogue.bye"}]},
                "commands": [
                ]
            }
        ]
    else:
        return [
            {
                "name": {"rawtext": [{"translate": "dialogue.bye"}]},
                "commands": [
                ]
            }
        ]


def createProgressDialogue(npc: dict, quest: dict):
    arr = []
    questName = quest['name'].replace(" ", "_").lower()
    for index, dialogue in enumerate(quest['progressDialogue']):
        arr.append({
            "scene_tag": f'QGen.{questName}.inProgress{index}',
            "npc_name": {"rawtext": [{"translate": f'entity.{npc["namespace"]}:{npc["identifier"]}.name'}]},
            "text": {"rawtext": [{"translate": f'QGen.{npc["identifier"]}.{questName}.progress{index}'}]},
            "on_open_commands": ["/playsound mob.villager.yes @initiator"],
            "buttons": createIntroButtons(quest, index, questName)
        })
    return arr


def createProgressButtons(quest: dict, index: int, questName: str):
    if index < (len(quest['progressDialogue']) - 1):
        return [
            {
                "name": {"rawtext": [{"translate": "QGen.dialogue.give_items"}]},
                "commands": [
                    "/scriptevent pb:checkConditions"
                ]
            },
            {
                "name": {"rawtext": [{"translate": "QGen.dialogue.ok"}]},
                "commands": [
                    f'/dialogue open @s @initiator QGen_{questName}.progress{index}'
                ]
            },
            {
                "name": {"rawtext": [{"translate": "dialogue.bye"}]},
                "commands": [
                ]
            }
        ]
    else:
        return [
            {
                "name": {"rawtext": [{"translate": "QGen.dialogue.give_items"}]},
                "commands": [
                    "/scriptevent pb:checkConditions"
                ]
            },
            {
                "name": {"rawtext": [{"translate": "dialogue.bye"}]},
                "commands": [
                ]
            }
        ]


def createFinishedDialogue(npc: dict, quest: dict, quests: list, questIndex: int):
    arr = []
    questName = quest['name'].replace(" ", "_").lower()
    for index, dialogue in enumerate(quest['finishedDialogue']):
        arr.append({
            "scene_tag": f'QGen.{questName}.finished{index}',
            "npc_name": {"rawtext": [{"translate": f'entity.{npc["namespace"]}:{npc["identifier"]}.name'}]},
            "text": {"rawtext": [{"translate": f'QGen.{npc["identifier"]}.{questName}.finished{index}'}]},
            "on_open_commands": ["/playsound mob.villager.yes @initiator"],
            "on_close_commands": createFinishedCloseCommands(quest, index, questName, quests, questIndex),
            "buttons": createFinishedButtons(quest, index, questName)
        })
    return arr


def createFinishedCloseCommands(quest: dict, index: int, questName: str, quests: list, questIndex: int):
    if index < (len(quest['finishedDialogue']) - 1):
        return []
    else:
        if questIndex < (len(quests) - 1):
            return ["/tag @s remove finished", f'/tag @s remove QGen_{questName}', "/function hideQuest",
                    f'/tag @s add QGen_{quests[questIndex + 1]["name"]}']
        else:
            return ["/tag @s remove finished", f'/tag @s remove QGen_{questName}', "/function hideQuest"]


def createFinishedButtons(quest: dict, index: int, questName: str):
    if index < (len(quest['finishedDialogue']) - 1):
        return [
            {
                "name": {"rawtext": [{"translate": "QGen.dialogue.ok"}]},
                "commands": [
                    f'/dialogue open @s @initiator QGen_{questName}.finished{index}'
                ]
            },
            {
                "name": {"rawtext": [{"translate": "dialogue.bye"}]},
                "commands": [
                ]
            }
        ]
    else:
        return [
            {
                "name": {"rawtext": [{"translate": "dialogue.bye"}]},
                "commands": [
                ]
            }
        ]
