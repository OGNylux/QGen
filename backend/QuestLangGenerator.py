def QuestLangGenerator(npc: dict, quests: list):
    lang = ""
    for quest in quests:
        questName = quest['name'].replace(" ", "_").lower()
        for i, dialogue in enumerate(quest['dialogue']):
            intro = f'QGen.{npc["identifier"]}.{questName}.intro{i}={dialogue}\n'
            lang += intro

        for i, dialogue in enumerate(quest['progressDialogue']):
            progress = f'QGen.{npc["identifier"]}.{questName}.progress{i}={dialogue}\n'
            lang += progress

        for i, dialogue in enumerate(quest['finishedDialogue']):
            finished = f'QGen.{npc["identifier"]}.{questName}.finished{i}={dialogue}\n'
            lang += finished

        lang += "QGen.dialogue.ok=Okay\n"
        lang += "QGen.dialogue.give_items=Give\n"
        lang += "QGen.dialogue.bye=Bye\n"

    return lang
