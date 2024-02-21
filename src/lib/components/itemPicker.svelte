<script lang="ts">
    import { Combobox } from "bits-ui";
    import { flyAndScale } from "$lib/transitions";
    import { Check, ChevronsUpDown } from "lucide-svelte";


   
    const fruits = [
      { value: "mango", label: "Mango" },
      { value: "watermelon", label: "Watermelon" },
      { value: "apple", label: "Apple" },
      { value: "pineapple", label: "Pineapple" },
      { value: "orange", label: "Orange" },
      { value: "orange1", label: "Orange" },
      { value: "orange2", label: "Orange" },
      { value: "orange3", label: "Orange" },
      { value: "orange4", label: "Orange" },
      { value: "orange5", label: "Orange" },
      { value: "orange6", label: "Orange" },
      { value: "orange7", label: "Orange" }
    ];
   
    let inputValue = "";
   
    $: filteredFruits = inputValue
      ? fruits.filter((fruit) => fruit.value.includes(inputValue.toLowerCase()))
      : fruits;
  </script>
   
<Combobox.Root items={filteredFruits} bind:inputValue>
    <div class="flex relative w-[296px]">
      <Combobox.Input
        class="inline-flex h-input w-[296px] truncate bg-neutral-800 rounded-md py-1.5 pl-3 pr-3 focus:outline-none focus:ring-2 focus:ring-emerald-600"
        placeholder="Select a fruit"
        aria-label="Select a fruit"
      />
      <ChevronsUpDown class="absolute end-3 top-1/2 size-6 -translate-y-1/2 text-neutral-600"/>
    </div>
   
    <Combobox.Content
      class="w-full max-h-96 overflow-y-auto rounded-xl border-2 border-emerald-600 bg-neutral-800 px-1 py-3 shadow-popover text-white"
      transition={flyAndScale}
      sideOffset={8}
    >
      {#each filteredFruits as fruit (fruit.value)}
        <Combobox.Item
          class="flex h-10 w-full select-none items-center rounded-md py-3 pl-5 pr-1.5 transition-all duration-75 data-[highlighted]:bg-neutral-700/50"
          value={fruit.value}
          label={fruit.label}
        >
          {fruit.label}
          <Combobox.ItemIndicator class="ml-auto" asChild={false}>
            <Check />
          </Combobox.ItemIndicator>
        </Combobox.Item>
      {:else}
        <span class="block px-5">
          {inputValue}
        </span>
      {/each}
    </Combobox.Content>
</Combobox.Root>
