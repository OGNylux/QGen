<script lang="ts">
    import { QuestStore } from "$lib/store";
    import { newQuestLine } from "$lib/helper";
    import { goto } from "$app/navigation";
    import { Tabs } from "bits-ui";
    import { Plus, Trash2 } from "lucide-svelte";
    import Form from "$lib/components/form/form.svelte";
    import { QuestItem } from "$lib/data";
    import { newQuest, postQuestDB, putQuestDB } from "$lib/helper";

    if(!QuestStore.getQuestItems()) newQuestLine();
    if(QuestStore.getNPC().identifier === "") goto('/editor');
    
    let questItems: QuestItem[] = [];
    
    questItems = QuestStore.getQuestItems();

    function addNewQuest() {
        newQuest();
        questItems = QuestStore.getQuestItems();
    }

    function deleteQuestItem(index: number) {
        if (questItems.length === 1) {
            QuestStore.setQuestItem([
                new QuestItem({
                    name: "",
                    description: "",
                    dialogue: [""],
                    progressDialogue: [""],
                    finishedDialogue: [""],
                    itemConditions: [{ id: "", amount: 1 }],
                    tagConditions: [""],
                    itemRewards: [{ id: "", amount: 1 }],
                    tagRewards: [""],
                }),
            ]);
            questItems = QuestStore.getQuestItems();
        } else {
            QuestStore.removeQuestItem(index);
            questItems = QuestStore.getQuestItems();
        }
    }

    function saveToDB() {
        if ($QuestStore._id) putQuestDB($QuestStore._id.$oid);
        else postQuestDB();
    }
</script>

{#if QuestStore}
    <Tabs.Root value="0" class="flex flex-row w-full h-full mb-40">
        <Tabs.List
            class="flex flex-col w-64 h-[512px] rounded-md bg-neutral-800 overflow-y-auto mt-32"
        >
            <div class="flex flex-col grow p-2 gap-1">
                {#each questItems as quest, i}
                    <Tabs.Trigger value={String(i)}>
                        <div
                            class="flex items-center rounded-md p-1 gap-1 bg-neutral-800 border-emerald-600 border-2 hover:bg-neutral-700/50 group"
                        >
                            <div
                                class="flex justify-center items-center bg-neutral-700/50 w-7 h-7 rounded-full"
                            >
                                <span class="text font-bold">Q{i}</span>
                            </div>
                            <span class="text-lg text-start font-bold grow truncate"
                                >{quest.name || "Custom Quest"}</span
                            >
                            <button
                                on:click={() => deleteQuestItem(i)}
                                class="flex justify-center items-center w-8 h-8 rounded justify-self-end opacity-0 group-hover:opacity-100 hover:bg-neutral-700/50 add-button-hover text-red-700"
                            >
                                <Trash2 size={20} strokeWidth={3} />
                            </button>
                        </div>
                    </Tabs.Trigger>
                {/each}
                <button
                    on:click={() => addNewQuest()}
                    class="flex rounded-md self-center justify-center items-center w-24 p-0.5 m-1 opacity-20 hover:opacity-100 add-button-hover
                    bg-neutral-800 border-emerald-600 border-2 shadow-md shadow-emerald-600/50 hover:bg-neutral-700/50"
                >
                    <Plus size={20} strokeWidth={3} />
                </button>
            </div>
            <a
                on:click={() => saveToDB()} href="/download"
                class="flex rounded-md self-center justify-center items-center w-24 p-0.5 m-1 sticky z-50 bottom-1
              bg-neutral-800 border-emerald-600 border-2 hover:bg-neutral-700/50"
            >
                Generate
            </a></Tabs.List
        >
        <div class="w-full">
            {#each questItems as item, i}
                <Tabs.Content value={String(i)} class="pt-10 px-4 mx-auto">
                    <Form quest={item} />
                </Tabs.Content>
            {/each}
        </div>
        <div class="w-64">
        </div>
    </Tabs.Root>
{:else}
    <div class="flex w-full h-[80vh] justify-center place-items-center">
      <img src="spin.svg" alt="" class="w-28">
    </div>
{/if}