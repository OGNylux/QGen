<script lang="ts">
  import * as Table from "$lib/components/ui/table/index";
  import { QuestLine } from "$lib/data";
  import DeleteDialog from "$lib/components/deleteDialog.svelte";
  import { deleteQuestDB, getQuestsDB, postQuestDB, sortDatesByNewest } from "$lib/helper";
  import { beforeUpdate, onMount } from "svelte";
  import Pagination from "./pagination.svelte";

  let data: QuestLine[];
  let test = 1;

  const itemsPerPage = 10;

  let paginatedData: QuestLine[];

  onMount(async () => {
    postQuestDB()
    data = await getQuestsDB().then((res) => {
      sortDatesByNewest(res);
      return res;
    });
    paginatedData = getPaginatedData();
  });

  function getPaginatedData() {
    const startIndex = (test - 1) * itemsPerPage;
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
    if (!questLine.quests) return "";
    let test: string[] = [];

    questLine.quests.forEach((element) => {
      test.push(element.name);
    });

    return test.join(", ");
  }

  function formatDate(date: Date) {
    return date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
      hour12: true,
    });
  }
</script>

{#if paginatedData}
<div class="min-h-[70vh]">
  <Table.Root>
    <Table.Header>
      <Table.Row class="hover:bg-neutral-900">
        <Table.Head class="w-[150px]"></Table.Head>
        <Table.Head>NPC</Table.Head>
        <Table.Head>Quests</Table.Head>
        <Table.Head class="text-right">Creation Date</Table.Head>
      </Table.Row>
    </Table.Header>
    <Table.Body>
      {#each paginatedData as quest }
        <Table.Row class="hover:bg-neutral-900">
          <Table.Cell class="flex flex-row font-medium">
            <button  
              class="flex rounded-lg self-center justify-center items-center w-24 p-0.5
            bg-neutral-800 border-emerald-600 border-2 shadow-md shadow-emerald-600/50 hover:bg-neutral-700/50">
              Edit
            </button>
            <DeleteDialog quest={quest} updateData={updateData} />
          </Table.Cell>
          <Table.Cell>{quest.npc.namespace}:{quest.npc.identifier}</Table.Cell>
          <Table.Cell class="truncate">{getNames(quest)}</Table.Cell>
          <Table.Cell class="text-right">{formatDate(new Date(quest.date))}</Table.Cell>
        </Table.Row>
      {/each}
    </Table.Body>
  </Table.Root>
</div>
<Pagination bind:currentPage={test} count={data.length} perPage={itemsPerPage} />
{:else}
   ...waiting
{/if}
