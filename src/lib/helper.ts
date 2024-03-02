import { QuestItem, QuestLine } from "./data";
import { QuestStore } from "$lib/store";
import JSZip from "jszip";

export function reset() {
    QuestStore.reset();
    newQuest()
}

export function newQuest() {
    QuestStore.addQuestItem(new QuestItem({
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

export function newQuestLine() {
    QuestStore.set(new QuestLine({namespace: "", identifier: ""}, [
        new QuestItem({
            name: "",
            description: "",
            dialogue: [""],
            progressDialogue: [""],
            finishedDialogue: [""],
            itemConditions: [{id: "", amount: 1}],
            tagConditions: [""],
            itemRewards: [{id: "", amount: 1}],
            tagRewards: [""]
            })
    ]));
}

export function formatDate(date: Date) {
    return date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
      hour12: true,
    });
  }

export function updateQuestStore(questline: QuestLine) {
  QuestStore.set(questline);
}

export function sortDatesByNewest(questLines: QuestLine[]): QuestLine[] {
    return questLines.slice().sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
}

export async function download() {
	// get zip file from endpoint
	let res = await fetch(`http://localhost:80/test`, {
		method: 'GET',
	});

	// convert zip file to url object (for anchor tag download)
	let blob = await res.blob();
	var url = window.URL || window.webkitURL;
	let link = url.createObjectURL(blob);

	let a = document.createElement("a");
	a.setAttribute("download", `image.txt`);
	a.setAttribute("href", link);
	document.body.appendChild(a);
	a.click();
	document.body.removeChild(a);
}
	
export async function postQuestToGenerator () {
	const response = await fetch('http://localhost:80/generator', {
		method: 'POST',
		body: JSON.stringify({
			quests: QuestStore.get()
		})
	})
	
	const tmp : string = await response.json();
    const test: string[] = JSON.parse(JSON.stringify(tmp))
    return test
}

export async function getQuestsDB() {
    const response = await fetch('http://localhost:80/db/questlines')
	
	const tmp : string = await response.json();
    const test: QuestLine[] = JSON.parse(JSON.stringify(tmp))
    return test
}

export async function postQuestDB() {
    const data = new QuestLine(QuestStore.getNPC(), QuestStore.getQuestItems());

	const res = await fetch('http://localhost:80/db/questlines', {
		method: 'POST',
		body: JSON.stringify({
            data
		})
	})
	
	const result = await res.text()
    console.log(result)
}

export async function putQuestDB(id: string) {
    let data = new QuestLine(QuestStore.getNPC(), QuestStore.getQuestItems());
    data.date = new Date();

	const res = await fetch(`http://localhost:80/db/questlines/${id}`, {
		method: 'PUT',
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