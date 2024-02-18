import { QuestItem } from "./data";
import { QuestStore } from "./store";

export function reset() {
    QuestStore.reset();
    QuestStore.add(new QuestItem({
        name: "",
        description: "",
        dialogue: [],
        progressDialogue: [],
        finishedDialogue: [],
        itemConditions: [],
        tagConditions: [],
        itemRewards: [],
        tagRewards: []
    }));
}