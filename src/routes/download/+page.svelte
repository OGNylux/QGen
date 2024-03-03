<script lang="ts">
   import NavBar from "$lib/components/navBar.svelte";
   import Footer from "$lib/components/footer.svelte";
   import { CodeBlock } from "@skeletonlabs/skeleton";
   import * as Carousel from "$lib/components/ui/carousel/index.js";
   import hljs from "highlight.js/lib/core";
   import "highlight.js/styles/atom-one-dark.css";
   import { storeHighlightJs } from "@skeletonlabs/skeleton";

   import javascript from "highlight.js/lib/languages/javascript";
   import json from "highlight.js/lib/languages/json";
   import "$lib/utils/lang.min.js"
   import "$lib/utils/lang.es.min.js"
   import lang from "$lib/utils/lang.js"
   import { postQuestToGenerator } from "$lib/helper";

   hljs.registerLanguage("json", json);
   hljs.registerLanguage("javascript", javascript);
   hljs.registerLanguage("lang", lang);

   storeHighlightJs.set(hljs);

   const codeArray = postQuestToGenerator();
</script>

<div class="">
   <NavBar />
   <div class="mt-12 mb-6">
      <div class="flex justify-center gap-2 mb-2">
           <div class="w-2/5 h-96 overflow-y-auto rounded-md border-2 border-neutral-700 shadow-popover">
            {#await codeArray}
               waiting for code to load...
            {:then value}
               <CodeBlock
                   language="js"
                   code={value[0]}
                   background="bg-neutral-900/50"
               ></CodeBlock>
            {/await}
           </div>
           <div class="w-2/5 h-96 overflow-y-auto rounded-md border-2 border-neutral-700 shadow-popover">
               {#await codeArray}
                  waiting for code to load...
               {:then value}
                  <CodeBlock
                      language="lang"
                      code={value[1]}
                      background="bg-neutral-900/50"
                  ></CodeBlock>
               {/await}
           </div>
       </div>
       <Carousel.Root class="w-1/2 mx-auto"
         opts={{
           align: "start",
           loop: true,
         }}>
         <Carousel.Content>
            {#await codeArray}
                  waiting for code to load...
               {:then value}
                  {#each value.splice(0,2) as _, i (i)}
                   <Carousel.Item>
                     <div class="p-1">
                        <div class="h-96 mx-auto overflow-y-auto rounded-md border-2 border-neutral-700 shadow-popover">
                           <CodeBlock
                           language="json"
                           code={value[i]}
                           background="bg-neutral-900/50"
                       ></CodeBlock>
                        </div>
                     </div>
                   </Carousel.Item>
                  {/each}
               {/await}
         </Carousel.Content>
         <Carousel.Previous class="bg-neutral-900 border-neutral-700 border-2 text-neutral-700 hover:bg-neutral-900 hover:border-emerald-600 hover:text-emerald-600" />
         <Carousel.Next class="bg-neutral-900 border-neutral-700 border-2 text-neutral-700 hover:bg-neutral-900 hover:border-emerald-600 hover:text-emerald-600" />
      </Carousel.Root>
   </div>
   <div class="w-[90%] inline-flex gap-2 mb-12 mx-auto justify-end">
      <a href="/form"
      class="flex items-center rounded-md w-32 h-10 bg-neutral-800 border-emerald-600 border-2 hover:bg-neutral-700/50 focus:outline-none text-xl justify-center">
         Edit
      </a>
      <button on:click={()=> postQuestToGenerator()}
      class="flex items-center rounded-md w-32 h-10 bg-emerald-600 hover:bg-emerald-500 focus:outline-none text-xl justify-center">
         Download
      </button>
   </div>
   <Footer />
</div>
