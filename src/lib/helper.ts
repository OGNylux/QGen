import { QuestItem, QuestLine } from "./data";
import { QuestStore } from "./store";

export function reset() {
    QuestStore.reset();
    newQuest()
}

export function newQuest() {
    QuestStore.add(new QuestItem({
    name: "",
    description: "",
    dialogue: [""],
    progressDialogue: [""],
    finishedDialogue: [""],
    itemConditions: [{id: "", amount: 1}],
    tagConditions: [""],
    itemRewards: [{id: "", amount: 1}],
    tagRewards: [""]
    }));
}

export function sortDatesByNewest(questLines: QuestLine[]): QuestLine[] {
    return questLines.slice().sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
}
	
export async function postQuestToGenerator () {
	const res = await fetch('http://localhost:80/test2', {
		method: 'POST',
		body: JSON.stringify({
			quests: QuestStore.get()
		})
	})
	
	const json = await res.json()
	const result = JSON.stringify(json)
    console.log(result)
}

export async function getQuestsDB() {
    const response = await fetch('http://localhost:80/db/questlines')
	
	const tmp : string = await response.json();
    const test: QuestLine[] = JSON.parse(JSON.stringify(tmp))
    return test
}

export async function postQuestDB() {
    const data = new QuestLine({"namespace": "minecraft", "identifier": "villager"}, QuestStore.get());
    console.log(data)

	const res = await fetch('http://localhost:80/db/questlines', {
		method: 'POST',
		body: JSON.stringify({
            data
		})
	})
	
	const result = await res.text()
    console.log(result)
}

export async function deleteQuestDB(id: string) {
	const response = await fetch(`http://localhost:80/db/questlines/${id}`, {
		method: 'DELETE'
	})
	
	const tmp : string = await response.json();
    const test: QuestLine[] = JSON.parse(JSON.stringify(tmp))
    return test
}