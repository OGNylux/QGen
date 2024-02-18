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
        dialogue: [],
        progressDialogue: [],
        finishedDialogue: [],
        itemConditions: [],
        tagConditions: [],
        itemRewards: [],
        tagRewards: []
        }));
    }

</script>

<div>
    <Tabs.Root value="0" class="flex flex-row h-screen relative">
      <Tabs.List class="flex flex-col items-center p-1.5 w-16 m-1 gap-2 rounded-2xl bg-slate-200">
        {#each $QuestStore as _, i }
            <Tabs.Trigger value={String(i)} class="flex justify-center items-center w-12 h-12 rounded-full bg-slate-100">
                <span class="text-2xl font-bold pb-1">Q{i}</span>
            </Tabs.Trigger>
        {/each}
        <button on:click={() => newQuest()} class="flex rounded-full justify-center items-center p-2 m-1 bg-slate-100 text-slate-700">
            <Plus size={36}/>
        </button>
      </Tabs.List>
      <div class="">
          {#each $QuestStore as item, i }
            <Tabs.Content value={String(i)} class="pt-3">
                <Form quest={item} />
            </Tabs.Content>
          {/each}
      </div>
    </Tabs.Root>
  </div>