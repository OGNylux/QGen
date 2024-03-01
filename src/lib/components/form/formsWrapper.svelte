<script lang="ts">
    import { QuestStore } from "$lib/store";
    import { Tabs } from "bits-ui";
    import { Plus } from "lucide-svelte";
    import Form from "$lib/components/form/form.svelte";
    import type { QuestItem } from "$lib/data";
    import { postQuestToGenerator, newQuest, getQuestsDB, postQuestDB, putQuestDB } from "$lib/helper";
    import { beforeUpdate } from "svelte";
    
    let questItems: QuestItem[] = [];
    
    questItems = QuestStore.getQuestItems();

    function addNewQuest() {
        newQuest()
        questItems = QuestStore.getQuestItems();
    }

    function saveToDB() {
        console.log($QuestStore._id)
        if($QuestStore._id) putQuestDB($QuestStore._id.$oid)
        else postQuestDB()
    }
</script>

{#if QuestStore}
    <Tabs.Root value="0" class="flex flex-row w-full h-full mb-20">
        <Tabs.List class="flex flex-col w-64 h-[512px] rounded-md bg-neutral-800 overflow-y-auto mt-32">
            <div class="flex flex-col grow p-2 gap-1">
                {#each questItems as quest, i }
                    <Tabs.Trigger value={String(i)}>
                        <div class="flex items-center rounded-md p-1 gap-1 bg-neutral-800 border-emerald-600 border-2 hover:bg-neutral-700/50">
                            <div class="flex justify-center items-center bg-neutral-700/50 w-7 h-7 rounded-full">
                                <span class="text font-bold">Q{i}</span>
                            </div>
                            <span class="text-lg font-bold">{quest.name || "Custom Quest"}</span>
                        </div>
                    </Tabs.Trigger>
                {/each}
                <button on:click={() => addNewQuest()} 
                    class="flex rounded-md self-center justify-center items-center w-24 p-0.5 m-1 opacity-20 hover:opacity-100 add-button-hover
                    bg-neutral-800 border-emerald-600 border-2 shadow-md shadow-emerald-600/50 hover:bg-neutral-700/50">
                    <Plus size={20} strokeWidth={3}/>
                </button>
            </div>
          <button on:click={() => saveToDB()} 
              class="flex rounded-md self-center justify-center items-center w-24 p-0.5 m-1 sticky z-50 bottom-1
              bg-neutral-800 border-emerald-600 border-2 shadow-md shadow-emerald-600/50">
              <Plus size={20} strokeWidth={3}/>
        </Tabs.List>
        <div class="w-full">
            {#each questItems as item, i }
              <Tabs.Content value={String(i)} class="pt-10 px-4">
                  <Form quest={item} />
              </Tabs.Content>
            {/each}
        </div>
    </Tabs.Root>
{:else}
    ...waiting
{/if}