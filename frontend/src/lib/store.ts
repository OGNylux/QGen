import { writable, get } from "svelte/store";
import { QuestItem, QuestLine } from "./data"

function questStore() {
    const store = writable<QuestLine>();
    const { subscribe, set, update } = store;
    return {
        subscribe,
        add: (quest: QuestLine) => update(n => quest),
        get: () => get(store),
        set: (items: QuestLine) => set(items),
        reset: () => set(new QuestLine({namespace: "", identifier: ""}, [])),

        addQuestItem: (questItem: QuestItem) => update(n => {
            n.questData.push(questItem);
            return n;
        }),
        removeQuestItem: (index: number) => update(n => {
            n.questData.splice(index, 1);
            return n;
        }),
        setQuestItem: (questData: QuestItem[]) => update(n => {
            n.questData = questData;
            return n;
        }),
        getQuestItems: () => get(store)?.questData,

        getNPC: () => get(store)?.npc
    };
}
export const QuestStore = questStore();