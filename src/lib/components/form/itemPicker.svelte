<script lang="ts">
    import { Combobox } from "bits-ui";
    import { flyAndScale } from "$lib/utils/transitions";
    import { Check, ChevronsUpDown } from "lucide-svelte";
    import type { MinecraftItem } from "$lib/data";

    export let item: MinecraftItem
   
    const items = [
      { value: "minecraft:apple", data: 0, label: "Apple" }
    ];
   
    let inputValue = "";
   
    $: filteredItems = inputValue
      ? items.filter((item) => item.value.includes(inputValue.toLowerCase()))
      : items;

    $: item.id = items.find(item => item.label === inputValue)?.value || inputValue;
    $: item.data = items.find(item => item.label === inputValue)?.data || 0;
</script>

<div class="flex flex-row w-full mb-1">
  <Combobox.Root items={filteredItems} bind:inputValue>
    <div class="flex relative w-full">
      <Combobox.Input class="inline-flex h-input w-full truncate bg-neutral-800 rounded-md py-1.5 pl-3 pr-3 focus:outline-none focus:ring-2 focus:ring-emerald-600"
        placeholder="Select a fruit"
        aria-label="Select a fruit"
      />
      <ChevronsUpDown class="absolute end-3 top-1/2 size-6 -translate-y-1/2 text-neutral-600"/>
    </div>
   
    <Combobox.Content class="w-full max-h-96 overflow-y-auto rounded-xl bg-neutral-800 px-1 py-3 shadow-popover text-white"
      transition={flyAndScale}
      sideOffset={8}
    >
      {#each filteredItems as item (item.value)}
        <Combobox.Item
          class="flex h-10 w-full select-none items-center rounded-md py-3 pl-5 pr-1.5 transition-all duration-75 data-[highlighted]:bg-neutral-700/50"
          value={item.value}
          label={item.label}
        >
          {item.label}
          <Combobox.ItemIndicator class="ml-auto" asChild={false}> <Check /> </Combobox.ItemIndicator>
        </Combobox.Item>
      {:else}
        <span class="block px-5">
          {inputValue}
        </span>
      {/each}
    </Combobox.Content>
  </Combobox.Root>
  <input type="number" placeholder="Amount" min="1" bind:value={item.amount}
    class="block bg-neutral-800 w-24 rounded-md ml-2 py-1.5 pl-3 pr-3 focus:outline-none focus:ring-2 focus:ring-emerald-600" />
</div>

