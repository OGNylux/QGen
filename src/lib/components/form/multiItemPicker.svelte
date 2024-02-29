<script lang="ts">
    import type { MinecraftItem, QuestItem } from "$lib/data";
    import { MinusCircle, Plus } from "lucide-svelte";
    import ItemPicker from "./itemPicker.svelte";

    export let quest : QuestItem;
    export let mode : string;

    function newDialogue() {
        if(mode === "condition") {quest.itemConditions.push({id: "", amount: 1}); quest.itemConditions = [...quest.itemConditions]}
        else {quest.itemRewards.push({id: "", amount: 1}); quest.itemRewards = [...quest.itemRewards]}
    }

    function removeFromArray(arr: MinecraftItem[], index: number) {
        if(arr.length > 1) arr.splice(index, 1);
        else arr[0] = {id: "", amount: 1};
    }
</script>



<div class="flex flex-col w-full h-36 place-items-center overflow-y-auto rounded-xl border-2 border-neutral-700 p-2 shadow-popover">
    {#if mode === "condition"}
        {#each quest.itemConditions as item, i}
            <div class="w-full z-10 relative group">
                <ItemPicker {item}/>
                <button on:click={() => {removeFromArray(quest.itemConditions, i); quest.itemConditions = [...quest.itemConditions]}}
                    class="absolute -right-1 -top-1 pb-4 opacity-0 group-hover:opacity-100 add-button-hover text-red-700">
                    <MinusCircle size={20} strokeWidth={3} />
                </button>
            </div>
        {/each}
    {:else}
        {#each quest.itemRewards as item, i}
            <div class="w-full z-10 relative group">
                <ItemPicker {item}/>
                <button on:click={() => {removeFromArray(quest.itemRewards, i); quest.itemConditions = [...quest.itemConditions]}}
                    class="absolute -right-1 -top-1 pb-4 opacity-0 group-hover:opacity-100 add-button-hover text-red-700">
                    <MinusCircle size={20} strokeWidth={3} />
                </button>
            </div>
        {/each}
    {/if}
    <button on:click={() => newDialogue()} 
        class="flex rounded-lg justify-self-center justify-center items-center w-24 p-0.5 mt-1 opacity-20 hover:opacity-100 add-button-hover
        bg-neutral-800 border-emerald-600 border-2 shadow-md shadow-emerald-600/50 hover:bg-neutral-700/50">
        <Plus size={20} strokeWidth={3}/>
    </button>
</div>