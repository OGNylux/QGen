import io
import uuid
import zipfile

from QuestDataGenerator import QuestDataGenerator
from QuestDialogueGenerator import QuestDialogueGenerator
from QuestLangGenerator import QuestLangGenerator
from QuestScripts import createMainJS, createQuestJS, createQuestCompletionJS, createQuestHudJS


def zipFile(npc: dict, quests: list):
    b = io.BytesIO()
    zf = zipfile.ZipFile(b, mode='w')
    zf.writestr('scripts/questData.js', QuestDataGenerator(quests))
    zf.writestr('scripts/main.js', createMainJS())
    zf.writestr('scripts/quest.js', createQuestJS())
    zf.writestr('scripts/questCompletion.js', createQuestCompletionJS())
    zf.writestr('scripts/questHud.js', createQuestHudJS())
    zf.writestr('lang/en_US.lang', QuestLangGenerator(npc, quests))

    arr = QuestDialogueGenerator(npc, quests)
    for index, quest in enumerate(arr):
        questName = quests[index]['name']
        zf.writestr(f'dialogue/QGen.{questName}.json', quest)

    zf.close()

    newUuid = uuid.uuid4()
    fileName = f'QGen_{newUuid}.zip'

    open(fileName, 'wb').write(b.getbuffer())
    return fileName
