import type { list } from "postcss";
import { QuestStore } from "./store";

interface Item {
    name: string;
    description: string;
    dialogue: string[];
    progressDialogue: string[];
    finishedDialogue: string[];
    itemConditions: MinecraftItem[];
    tagConditions: string[];
    itemRewards: MinecraftItem[];
    tagRewards: string[];
}

class QuestItem {
    name: string;
    description: string;
    dialogue: string[];
    progressDialogue: string[];
    finishedDialogue: string[];
    itemConditions: MinecraftItem[];
    tagConditions: string[];
    itemRewards: MinecraftItem[];
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

class NPC {
    namespace: string = "";
    identifier: string = "";
}

class QuestLine {
    _id?: any;
    npc: NPC;
    questData: QuestItem[] = [];
    date: Date = new Date();

    constructor(npc: NPC, questData: QuestItem[]) {
        this.npc = npc;
        this.questData = questData;
    }

}

class MinecraftItem {
    id: string = "";
    data?: number = 0;
    amount: number = 0;
}

export { QuestItem, QuestLine, MinecraftItem };