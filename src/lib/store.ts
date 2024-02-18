import { writable, get } from "svelte/store";
import { QuestItem } from "./data"

function questStore() {
    const store = writable<QuestItem[]>([]);
    const { subscribe, set, update } = store;
    return {
        subscribe,
        update: (item: QuestItem) => update(n => n.map(i => i.name == item.name ? item : i)), // if the item is already in the store, update it, otherwise add it
        add: (item: QuestItem) => update(n => [...n, item]),
        contains: (item: QuestItem) => get(store).some(x => x.name == item.name),
        get: () => get(store),
        reset: () => set([]),
    };
}
export const QuestStore = questStore();