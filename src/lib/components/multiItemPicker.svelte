<script lang="ts">
    import type { QuestItem } from "$lib/data";
    import { Plus } from "lucide-svelte";
    import ItemPicker from "./itemPicker.svelte";

    export let quest : QuestItem;
    export let mode : string;

    let arr = mode == "condition" ? quest.itemConditions : quest.itemRewards;

    function newDialogue() {
        arr = [...arr, {id: "", amount: 0}];
    }
</script>



<div class="grid w-full max-h-48 place-items-center overflow-y-auto rounded-xl border-2 border-neutral-700 p-2 shadow-popover">
    {#each arr as _}
        <ItemPicker/>
    {/each}
    <button on:click={() => newDialogue()} 
        class="flex rounded-lg justify-self-center justify-center items-center w-24 p-0.5 m-1 opacity-20 hover:opacity-100 add-button-hover
        bg-neutral-800 border-emerald-600 border-2 shadow-md shadow-emerald-600/50 hover:bg-neutral-700/50">
        <Plus size={20} strokeWidth={3}/>
    </button>
</div>


<style>
    .add-button-hover {
        transition: opacity 0.25s;
    }
</style>