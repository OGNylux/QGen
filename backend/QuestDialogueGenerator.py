def QuestDialogueGenerator(quests: list):
    scenes = []
    for quest in quests:
        scene = {

        }

#def createDialogue(quest, scenes):
#    for i in range(len(quest['dialogue'])):
#        scenes.append({
#            "scene_tag": f"QGenQuest_{quest['name']}.intro{i}",
#            "npc_name": {"rawtext": [{"translate": f"entity.pb:hugo.name"}]},
#            "text": {
#                "rawtext": [
#                    {"translate": f"dialogue.{self.npcName}.{self.questName}_i{i}"}]},
#            "on_open_commands": self.introOpenCmdCreator(quest, i),
#            "on_close_commands": introCloseCmdCreator(quest, i),
#            "buttons": [{"name": {"rawtext": [{"translate": "dialogue.next_line"}]},
#                         "commands": [
#                             f"/event entity @s core:quest_{self.questName}_i{i + 1}"
#                             if i < len(quest.getDialogue()) - 1 else
#                             f"/event entity @s core:quest_{self.questName}_uf"
#                         ]},
#                        {"name": {"rawtext": [{"translate": "dialogue.ok"}]},
#                         "commands": []}]
#        })