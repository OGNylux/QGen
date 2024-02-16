import { EmptyQuest } from "./data";
import { QuestStore } from "./store";

export function reset() {
    QuestStore.reset();
    QuestStore.add(EmptyQuest);
}