<script lang="ts">
    import type { QuestItem } from "$lib/data";
    import { MinusCircle, Plus } from "lucide-svelte";

    export let quest : QuestItem;
    export let mode : string;

    function newDialogue() {
        if(mode === "start") {quest.dialogue.push(""); quest.dialogue = [...quest.dialogue]}
        else if(mode === "progress") {quest.progressDialogue.push(""); quest.progressDialogue = [...quest.progressDialogue]}
        else {quest.finishedDialogue.push(""); quest.finishedDialogue = [...quest.finishedDialogue]}
    }

    function removeFromArray(arr: string[], index: number) {
        if(arr.length > 1) arr.splice(index, 1);
        else arr[0] = "";
    }
</script>



<div class="grid w-full h-40 pr-3 place-items-center overflow-y-auto rounded-md border-2 border-neutral-700 p-2 shadow-popover">
    {#if mode === "start"}
        {#each quest.dialogue as _, i}
            <div class="w-full z-10 relative group">
                <textarea placeholder="Enter the {i+1}. Dialogue" 
                    class="block bg-neutral-800 w-full h-24 rounded-md py-1.5 pl-3 pr-3 mb-2 resize-none focus:outline-none focus:ring-2 focus:ring-emerald-600" 
                    bind:value={quest.dialogue[i]} />   
                <button on:click={() => {removeFromArray(quest.dialogue, i); quest.dialogue = [...quest.dialogue]}}
                    class="absolute -right-1 -top-1 pb-4 opacity-0 group-hover:opacity-100 add-button-hover text-red-700">
                    <MinusCircle size={20} strokeWidth={3} />
                </button>
            </div>
        {/each}
    {:else if mode === "progress"}
        {#each quest.progressDialogue as _, i}
            <div class="w-full z-10 relative group">
                <textarea placeholder="Enter the {i+1}. Dialogue" 
                    class="block bg-neutral-800 w-full h-24 rounded-md py-1.5 pl-3 pr-3 mb-2 resize-none focus:outline-none focus:ring-2 focus:ring-emerald-600" 
                    bind:value={quest.progressDialogue[i]} />   
                <button on:click={() => {removeFromArray(quest.progressDialogue, i); quest.progressDialogue = [...quest.progressDialogue]}}
                    class="absolute -right-1 -top-1 pb-4 opacity-0 group-hover:opacity-100 add-button-hover text-red-700">
                    <MinusCircle size={20} strokeWidth={3} />
                </button>
            </div>
        {/each}
    {:else}
        {#each quest.finishedDialogue as _, i}
            <div class="w-full z-10 relative group">
                <textarea placeholder="Enter the {i+1}. Dialogue" 
                    class="block bg-neutral-800 w-full h-24 rounded-md py-1.5 pl-3 pr-3 mb-2 resize-none focus:outline-none focus:ring-2 focus:ring-emerald-600" 
                    bind:value={quest.finishedDialogue[i]} />   
                <button on:click={() => {removeFromArray(quest.finishedDialogue, i); quest.finishedDialogue = [...quest.finishedDialogue]}}
                    class="absolute -right-1 -top-1 pb-4 opacity-0 group-hover:opacity-100 add-button-hover text-red-700">
                    <MinusCircle size={20} strokeWidth={3} />
                </button>
            </div>
        {/each}
    {/if}
    <button on:click={() => newDialogue()} 
        class="flex rounded-md justify-self-center justify-center items-center w-24 p-0.5 mx-1 opacity-20 hover:opacity-100 add-button-hover
        bg-neutral-800 border-emerald-600 border-2 shadow-md shadow-emerald-600/50 hover:bg-neutral-700/50">
        <Plus size={20} strokeWidth={3}/>
    </button>
</div>