<script lang="ts">
    import { Separator, Tabs } from "bits-ui";
    import { Github, HelpCircle, Home, Plus } from "lucide-svelte";
    import { onMount } from "svelte";
    import { reset } from "$lib/helper";
    import { QuestStore } from "$lib/store";
    import { QuestItem } from "$lib/data";
    import Form from "$lib/components/form.svelte";

    onMount(() => {
        reset();
    });

    function newQuest() {
        QuestStore.add(new QuestItem({
        name: "",
        description: "",
        dialogue: [""],
        progressDialogue: [],
        finishedDialogue: [],
        itemConditions: [],
        tagConditions: [],
        itemRewards: [],
        tagRewards: []
        }));
    }

</script>

<div class="flex h-screen">
    <Tabs.Root value="0" class="flex flex-row w-full">
      <Tabs.List class="flex flex-col p-2 w-64 h-2/3 gap-1 rounded-lg bg-neutral-800 overflow-y-auto my-auto">
        {#each $QuestStore as quest, i }
            <Tabs.Trigger value={String(i)}>
                <div class="flex items-center rounded-lg p-1 gap-1 bg-neutral-800 border-emerald-600 border-2 hover:bg-neutral-700/50">
                    <div class="flex justify-center items-center bg-neutral-700/50 w-7 h-7 rounded-full">
                        <span class="text font-bold">Q{i}</span>
                    </div>
                    <span class="text-lg font-bold">{quest.name || "Custom Quest"}</span>
                </div>
            </Tabs.Trigger>
        {/each}
        <button on:click={() => newQuest()} 
            class="flex rounded-lg self-center justify-center items-center w-24 p-0.5 m-1 opacity-20 hover:opacity-100 add-button-hover
            bg-neutral-800 border-emerald-600 border-2 shadow-md shadow-emerald-600/50 hover:bg-neutral-700/50">
            <Plus size={20} strokeWidth={3}/>
        </button>
      </Tabs.List>
      <div class="w-full">
          {#each $QuestStore as item, i }
            <Tabs.Content value={String(i)} class="pt-20 px-4">
                <Form quest={item} />
            </Tabs.Content>
          {/each}
      </div>
    </Tabs.Root>
</div>


<style>
    .add-button-hover {
        transition: opacity 0.25s;
    }
</style>