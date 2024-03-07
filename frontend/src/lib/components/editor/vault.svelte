<script lang="ts">
  import * as Table from "$lib/components/ui/table/index";
  import { QuestLine } from "$lib/data";
  import DeleteDialog from "$lib/components/editor/deleteDialog.svelte";
  import { deleteQuestDB, formatDate, getQuestsDB, sortDatesByNewest, updateQuestStore } from "$lib/helper";
  import { beforeUpdate, onMount } from "svelte";
  import { toast } from "svelte-sonner";
  import Pagination from "./pagination.svelte";

  let data: QuestLine[];
  let page = 1;

  const itemsPerPage = 10;

  let paginatedData: QuestLine[];

  onMount(async () => {
    data = await getQuestsDB().then((res) => {
      return sortDatesByNewest(res);
    }).catch((err) => {
      toast.error("An Error has occured", {
        description: `Error: ${err.message}`
      });
    });
    paginatedData = getPaginatedData();
  });

  function getPaginatedData() {
    const startIndex = (page - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    return data?.slice(startIndex, endIndex);
  }

  beforeUpdate(() => {
    paginatedData = getPaginatedData();
  });

  async function updateData(quest: QuestLine) {
    data = await deleteQuestDB(quest._id?.$oid)
  }

  function getNames(questLine: QuestLine) {
    if (!questLine.questData) return "";
    let names: string[] = [];

    questLine.questData.forEach((element) => {
      names.push(element.name);
    });

    return names.join(", ");
  }
</script>

{#if paginatedData}
  <div class="h-[70vh]">
    <Table.Root>
      <Table.Header>
        <Table.Row class="hover:bg-neutral-900">
          <Table.Head class="w-[150px]"></Table.Head>
          <Table.Head>NPC</Table.Head>
          <Table.Head>Quests</Table.Head>
          <Table.Head class="text-right">Last Edit</Table.Head>
        </Table.Row>
      </Table.Header>
      <Table.Body>
        {#if paginatedData.length > 0}
          {#each paginatedData as quest }
            <Table.Row class="hover:bg-neutral-900">
              <Table.Cell class="flex flex-row font-medium w-[150px]">
                <a on:click={() => updateQuestStore(quest)} href="/form"
                  class="flex rounded-md self-center justify-center items-center w-24 p-0.5
                bg-neutral-800 border-emerald-600 border-2  hover:bg-neutral-700/50">
                  Edit
                </a>
                <DeleteDialog quest={quest} updateData={updateData} />
              </Table.Cell>
              <Table.Cell class="w-1/5 truncate">{quest.npc.namespace}:{quest.npc.identifier}</Table.Cell>
              <Table.Cell class="truncate">{getNames(quest)}</Table.Cell>
              <Table.Cell class="w-64 text-right">{formatDate(new Date(quest.date))}</Table.Cell>
            </Table.Row>
          {/each}
        {/if}
      </Table.Body>
    </Table.Root>
    {#if paginatedData.length == 0}
      <p class="mt-4 text-center">Nothing to see here... Maybe add a quest?</p>
    {/if}
  </div>
  {#if paginatedData.length > 0}
    <Pagination bind:currentPage={page} count={data.length} perPage={itemsPerPage} />
  {:else}  
    <div class="h-8 my-8"></div>
  {/if}
{:else}  
  <div class="flex w-full h-[80vh] justify-center place-items-center">
    <img src="spin.svg" alt="" class="w-28">
  </div>
{/if}
