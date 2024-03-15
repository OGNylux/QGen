<script lang="ts">
   import { CodeBlock } from "@skeletonlabs/skeleton";
   import * as Carousel from "$lib/components/ui/carousel/index.js";
   import hljs from "highlight.js/lib/core";
   import "highlight.js/styles/atom-one-dark.css";
   import { storeHighlightJs } from "@skeletonlabs/skeleton";

   import javascript from "highlight.js/lib/languages/javascript";
   import json from "highlight.js/lib/languages/json";
   import "$lib/utils/lang.min.js";
   import "$lib/utils/lang.es.min.js";
   import lang from "$lib/utils/lang.js";
   import { download, postQuestToGenerator } from "$lib/helper";
   import { QuestStore } from "$lib/store";
   import { goto } from "$app/navigation";
   import { onMount } from "svelte";
    import NavBar from "$lib/components/navBar.svelte";
    import Footer from "$lib/components/footer.svelte";

   hljs.registerLanguage("json", json);
   hljs.registerLanguage("javascript", javascript);
   hljs.registerLanguage("lang", lang);

   storeHighlightJs.set(hljs);

   let data: string[];

   onMount(async () => {
      data = await postQuestToGenerator();
   });

   if (QuestStore.getNPC().identifier === "") goto("/editor");
</script>

<NavBar/>
{#if data}
   <div class="flex justify-center gap-2 mb-2">
      <div
         class="w-2/5 h-72 overflow-y-auto rounded-md border-2 border-neutral-700 shadow-popover"
      >
         <CodeBlock language="js" code={data[0]} background="bg-neutral-900/50"
         ></CodeBlock>
      </div>
      <div
         class="w-2/5 h-72 overflow-y-auto rounded-md border-2 border-neutral-700 shadow-popover"
      >
         <CodeBlock
            language="lang"
            code={data[1]}
            background="bg-neutral-900/50"
         ></CodeBlock>
      </div>
   </div>
   <Carousel.Root
      class="w-1/2 mx-auto"
      opts={{
         align: "start",
         loop: true,
      }}
   >
      <Carousel.Content>
         {#each data.slice(2) as code}
            <Carousel.Item>
               <div class="p-1">
                  <div
                     class="h-72 mx-auto overflow-y-auto rounded-md border-2 border-neutral-700 shadow-popover"
                  >
                     <CodeBlock
                        language="json"
                        {code}
                        background="bg-neutral-900/50"
                     ></CodeBlock>
                  </div>
               </div>
            </Carousel.Item>
         {/each}
      </Carousel.Content>
      <Carousel.Previous
         class="bg-neutral-900 border-neutral-700 border-2 text-neutral-700 hover:bg-neutral-900 hover:border-emerald-600 hover:text-emerald-600"
      />
      <Carousel.Next
         class="bg-neutral-900 border-neutral-700 border-2 text-neutral-700 hover:bg-neutral-900 hover:border-emerald-600 hover:text-emerald-600"
      />
   </Carousel.Root>
   <div class="w-[90%] inline-flex gap-2 mt-2 mx-auto justify-end">
      <a
         href="/form"
         class="flex items-center rounded-md w-32 h-10 bg-neutral-800 border-emerald-600 border-2 hover:bg-neutral-700/50 focus:outline-none text-xl justify-center"
      >
         Edit
      </a>
      <button
         on:click={() => download()}
         class="flex items-center rounded-md w-32 h-10 bg-emerald-600 hover:bg-emerald-500 focus:outline-none text-xl justify-center"
      >
         Download
      </button>
   </div>
{:else}
   <div class="flex w-full h-[80vh] justify-center place-items-center">
      <img src="spin.svg" alt="" class="w-28" />
   </div>
{/if}
<Footer/>
