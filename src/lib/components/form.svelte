<script lang="ts">
    import type { QuestItem } from "$lib/data";
    import { Separator } from "bits-ui";
    import { Plus } from "lucide-svelte";
    import ItemPicker from "./itemPicker.svelte";

    export let quest : QuestItem;

    function newDialogue() {
        quest.dialogue = [...quest.dialogue, ""];
    }
</script>

<div class="flex flex-col w-full gap-2">
    <h1 class="text-4xl font-bold">This is the form page</h1>
    <Separator.Root orientation="horizontal" class="w-3/4 h-1 rounded-xl bg-emerald-600" />
    <div class="flex flex-row w-full gap-8">
        <div class="flex flex-col gap-1 w-1/3">
            <span class="text-2xl">Quest Name</span>
            <input placeholder="Enter a Quest Name" class="block bg-neutral-800 w-full rounded-md py-1.5 pl-3 pr-3 focus:outline-none focus:ring-2 focus:ring-emerald-600" type="text" bind:value={quest.name} />
        </div>
        <div class="flex flex-col gap-1 w-1/3">
            <span class="text-2xl">Quest Description</span>
            <input class="block bg-neutral-800 w-full rounded-md py-1.5 pl-3 pr-3 focus:outline-none focus:ring-2 focus:ring-emerald-600" type="text" bind:value={quest.description} />
        </div>
    </div>
    <h2 class="text-4xl font-bold">Quest Progress</h2>
    <Separator.Root orientation="horizontal" class="w-full h-1 rounded-xl bg-emerald-600" />
    <div class="flex flex-row w-full gap-8">
        <div class="flex flex-col gap-1 w-1/2">
            <span class="text-2xl">Quest Start Dialogue</span>
            {#each quest.dialogue as _, i}
                <textarea class="block bg-neutral-800 w-full h-24 rounded-md py-1.5 pl-3 pr-3 resize-none focus:outline-none focus:ring-2 focus:ring-emerald-600" bind:value={quest.dialogue[i]} />
            {/each}
            <button on:click={() => newDialogue()} 
                class="flex rounded-lg self-center justify-center items-center w-24 p-0.5 m-1 opacity-20 hover:opacity-100 add-button-hover
                bg-neutral-800 border-emerald-600 border-2 shadow-md shadow-emerald-600/50 hover:bg-neutral-700/50">
                <Plus size={20} strokeWidth={3}/>
            </button>
        </div>
        <div class="flex flex-col gap-1">
            <span class="text-2xl">Quest Start Dialogue</span>
            <ItemPicker />
        </div>
    </div>
</div>

<style>
    .add-button-hover {
        transition: opacity 0.25s;
    }
</style>