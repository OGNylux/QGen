<script lang="ts">
    import type { QuestItem } from "$lib/data";
    import { Separator } from "bits-ui";

    export let quest : QuestItem;

    let i = 0;
</script>

<div class="flex flex-col w-full gap-2">
    <h1 class="text-4xl font-bold">This is the form page</h1>
    <Separator.Root orientation="horizontal" class="w-3/4 h-1 rounded-xl bg-emerald-600" />
    <div class="flex flex-row w-full gap-8">
        <div class="flex flex-col gap-1">
            <span class="text-2xl">Quest Name</span>
            <input placeholder="Enter a Quest Name" class="bg-neutral-800 w-96 rounded-lg text-lg px-1" type="text" bind:value={quest.name} />
        </div>
        <div class="flex flex-col gap-1">
            <span class="text-2xl">Quest Description</span>
            <input class="bg-neutral-800 w-96 rounded-lg text-lg px-1" type="text" bind:value={quest.description} />
        </div>
    </div>
    <h2 class="text-4xl font-bold">Quest Progress</h2>
    <Separator.Root orientation="horizontal" class="w-full h-1 rounded-xl bg-emerald-600" />
    <div class="flex flex-row w-full gap-8">
        <div class="flex flex-col gap-1 w-full">
            <span class="text-2xl">Quest Start Dialogue</span>
            {#each quest.dialogue as _, i}
                <textarea class="bg-neutral-800 w-2/3 h-24 align-top rounded-lg text-lg resize-none" bind:value={quest.dialogue[i]} />
            {/each}
        </div>
    </div>

</div>