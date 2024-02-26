<script lang="ts">
    import type { QuestItem } from "$lib/data";
    import { Plus } from "lucide-svelte";

    export let quest : QuestItem;
    export let mode : string;

    let arr : string[] = mode === "start" ? quest.dialogue : mode === "progress" ? quest.progressDialogue : quest.finishedDialogue;
    function newDialogue() {
        arr.push("");
        arr = [...arr]; 
    }
</script>



<div class="grid w-full h-40 pr-3 place-items-center overflow-y-auto rounded-xl border-2 border-neutral-700 p-2 shadow-popover">
    {#each arr as tt, i}
        <div class="w-full">
            <textarea placeholder="Enter the {tt}. Dialogue" 
                class="block bg-neutral-800 w-full h-24 rounded-md py-1.5 pl-3 pr-3 mb-2 resize-none focus:outline-none focus:ring-2 focus:ring-emerald-600" 
                bind:value={arr[i]} on:input={()=> console.log(quest.dialogue)} />
        </div>
    {/each}
    <button on:click={() => newDialogue()} 
        class="flex rounded-lg justify-self-center justify-center items-center w-24 p-0.5 mx-1 opacity-20 hover:opacity-100 add-button-hover
        bg-neutral-800 border-emerald-600 border-2 shadow-md shadow-emerald-600/50 hover:bg-neutral-700/50">
        <Plus size={20} strokeWidth={3}/>
    </button>
</div>


<style>
    .add-button-hover {
        transition: opacity 0.25s;
    }
</style>