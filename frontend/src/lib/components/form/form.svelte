<script lang="ts">
    import type { QuestItem } from "$lib/data";
    import { Separator } from "bits-ui";
    import MultiTextarea from "./multiTextarea.svelte";
    import MultiInput from "./multiInput.svelte";
    import MultiItemPicker from "./multiItemPicker.svelte";
    import { QuestStore } from "$lib/store";
    import EditNameDialog from "./editNameDialog.svelte";

    export let quest: QuestItem;
</script>

<div class="flex flex-col w-full h-full gap-2">
    <div class="flex ml-28 group">
        <h1 class="text-2xl font-bold">
            {$QuestStore.npc.namespace}:{$QuestStore.npc.identifier}
        </h1>
        <EditNameDialog />
    </div>
    <Separator.Root
        orientation="horizontal"
        class="w-[90%] mb-3 h-1 rounded-xl bg-emerald-600 mx-auto"
    />
    <div class="flex flex-row w-full gap-8 justify-center">
        <div class="flex flex-col gap-4 w-1/3">
            <div>
                <span class="text-2xl">Quest Name</span>
                <input
                    placeholder="Enter a Quest Name"
                    class="block bg-neutral-800 w-full rounded-md py-1.5 pl-3 pr-3 focus:outline-none focus:ring-2 focus:ring-emerald-600"
                    type="text"
                    bind:value={quest.name}
                />
            </div>
            <div>
                <span class="text-2xl">Quest Description</span>
                <input
                    placeholder="Enter a Quest Description"
                    class="block bg-neutral-800 w-full rounded-md py-1.5 pl-3 pr-3 focus:outline-none focus:ring-2 focus:ring-emerald-600"
                    type="text"
                    bind:value={quest.description}
                />
            </div>
        </div>

        <div class="flex flex-col w-1/2">
            <span class="text-2xl">Quest Start Dialogue</span>
            <MultiTextarea {quest} mode="start" />
        </div>
    </div>
    <Separator.Root
        orientation="horizontal"
        class="w-[90%] my-3 h-1 rounded-xl bg-emerald-600 mx-auto"
    />
    <div class="flex flex-row w-full gap-8 justify-center">
        <div class="flex flex-col gap-4 w-1/3">
            <div>
                <span class="text-2xl">Quest Condition Items</span>
                <MultiItemPicker {quest} mode="condition" />
            </div>
            <div>
                <span class="text-2xl">Quest Condition Tags</span>
                <MultiInput {quest} mode="condition" />
            </div>
        </div>

        <div class="flex flex-col w-1/2">
            <span class="text-2xl">Quest in Progress Dialogue</span>
            <MultiTextarea {quest} mode="progress" />
        </div>
    </div>
    <Separator.Root
        orientation="horizontal"
        class="w-[90%] my-3 h-1 rounded-xl bg-emerald-600 mx-auto"
    />
    <div class="flex flex-row w-full gap-8 justify-center">
        <div class="flex flex-col gap-4 w-1/3">
            <div>
                <span class="text-2xl">Quest Reward Items</span>
                <MultiItemPicker {quest} mode="reward" />
            </div>
            <div>
                <span class="text-2xl">Quest Reward Tags</span>
                <MultiInput {quest} mode="reward" />
            </div>
        </div>

        <div class="flex flex-col w-1/2">
            <span class="text-2xl">Quest Finished Dialogue</span>
            <MultiTextarea {quest} mode="end" />
        </div>
    </div>
</div>
