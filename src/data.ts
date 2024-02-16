import type { list } from "postcss";

interface Item {
    name: string;
    description: string;
    dialogue: string[];
    progressDialogue: string[];
    finishedDialogue: string[];
    itemConditions: Map<string, number>[];
    tagConditions: string[];
    itemRewards: Map<string, number>[];
    tagRewards: string[];
}

class QuestItem {
    name: string;
    description: string;
    dialogue: string[];
    progressDialogue: string[];
    finishedDialogue: string[];
    itemConditions: Map<string, number>[];
    tagConditions: string[];
    itemRewards: Map<string, number>[];
    tagRewards: string[];

    constructor(item: Item) {
        this.name = item.name;
        this.description = item.description;
        this.dialogue = item.dialogue;
        this.progressDialogue = item.progressDialogue;
        this.finishedDialogue = item.finishedDialogue;
        this.itemConditions = item.itemConditions;
        this.tagConditions = item.tagConditions;
        this.itemRewards = item.itemRewards;
        this.tagRewards = item.tagRewards;
    }
}

let EmptyQuest = new QuestItem({
    name: "",
    description: "",
    dialogue: [],
    progressDialogue: [],
    finishedDialogue: [],
    itemConditions: [],
    tagConditions: [],
    itemRewards: [],
    tagRewards: []
});

export { QuestItem, EmptyQuest };