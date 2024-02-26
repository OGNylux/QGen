import { QuestItem } from "./data";
import { QuestStore } from "./store";

export function reset() {
    QuestStore.reset();
    QuestStore.add(new QuestItem({
        name: "",
        description: "",
        dialogue: [""],
        progressDialogue: [""],
        finishedDialogue: [""],
        itemConditions: [{ id: "", amount: 1}],
        tagConditions: [""],
        itemRewards: [{ id: "", amount: 1}],
        tagRewards: [""]
    }));
}

let result = null
	
export async function doPost () {
	const res = await fetch('http://localhost:80/test2', {
		method: 'POST',
		body: JSON.stringify({
			quests: QuestStore.get()
		})
	})
	
	const json = await res.json()
	result = JSON.stringify(json)
    console.log(result)
}