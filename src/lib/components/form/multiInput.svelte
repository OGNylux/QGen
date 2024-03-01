<script lang="ts">
    import type { QuestItem } from "$lib/data";
    import { MinusCircle, Plus } from "lucide-svelte";

    export let quest : QuestItem;
    export let mode : string;

    function newDialogue() {
        if(mode === "condition") {quest.tagConditions.push(""); quest.tagConditions = [...quest.tagConditions]}
        else {quest.tagRewards.push(""); quest.tagRewards = [...quest.tagRewards]}
    }

    function removeFromArray(arr: string[], index: number) {
        if(arr.length > 1) arr.splice(index, 1);
        else arr[0] = "";
    }
</script>

<div class="flex flex-col w-full h-36 place-items-center overflow-y-auto rounded-xl border-2 border-neutral-700 p-2 shadow-popover">
    {#if mode === "condition"}
        {#each quest.tagConditions as _, i}
            <div class="w-full z-10 relative group">
                <input placeholder="Enter the {i+1}. Tag"
                    class="block bg-neutral-800 w-full rounded-md py-1.5 pl-3 pr-3 mb-1 focus:outline-none focus:ring-2 focus:ring-emerald-600" 
                    type="text" bind:value={quest.tagConditions[i]} /> 
                <button on:click={() => {removeFromArray(quest.tagConditions, i); quest.tagConditions = [...quest.tagConditions]}}
                    class="absolute -right-1 -top-1 pb-4 opacity-0 group-hover:opacity-100 add-button-hover text-red-700">
                    <MinusCircle size={20} strokeWidth={3} />
                </button>
            </div>
        {/each}
    {:else}
        {#each quest.tagRewards as _, i}
            <div class="w-full z-10 relative group">
                <input placeholder="Enter the {i+1}. Tag"
                    class="block bg-neutral-800 w-full rounded-md py-1.5 pl-3 pr-3 mb-1 focus:outline-none focus:ring-2 focus:ring-emerald-600" 
                    type="text" bind:value={quest.tagRewards[i]} /> 
                <button on:click={() => {removeFromArray(quest.tagRewards, i); quest.tagRewards = [...quest.tagRewards]}}
                    class="absolute -right-1 -top-1 pb-4 opacity-0 group-hover:opacity-100 add-button-hover text-red-700">
                    <MinusCircle size={20} strokeWidth={3} />
                </button>
            </div>
        {/each}
    {/if}
    
    <button on:click={() => newDialogue()} 
        class="flex rounded-md justify-self-center justify-center items-center w-24 p-0.5 mt-1 opacity-20 hover:opacity-100 add-button-hover
        bg-neutral-800 border-emerald-600 border-2 shadow-md shadow-emerald-600/50 hover:bg-neutral-700/50">
        <Plus size={20} strokeWidth={3}/>
    </button>
</div>