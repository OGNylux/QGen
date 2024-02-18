<script lang="ts">
    import type { QuestItem } from "$lib/data";
    import { Separator } from "bits-ui";

    export let quest : QuestItem;
</script>

<div class="flex flex-col w-full gap-2">
    <h1 class="text-4xl font-bold">This is the form page</h1>
    <Separator.Root orientation="horizontal" class="w-3/4 h-1 rounded-xl bg-slate-100" />
    <div class="flex flex-row w-full gap-8">
        <div class="flex flex-col gap-1">
            <span class="text-2xl font-bold">Quest Name</span>
            <input class="bg-slate-200 w-96 rounded-lg text-lg" type="text" bind:value={quest.name} />
        </div>
        <div class="flex flex-col gap-1">
            <span class="text-2xl font-bold">Quest Description</span>
            <input class="bg-slate-200 w-96 rounded-lg text-lg" type="text" bind:value={quest.description} />
        </div>
    </div>
</div>