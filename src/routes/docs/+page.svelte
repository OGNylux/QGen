<script lang="ts">
    import { CodeBlock } from "@skeletonlabs/skeleton";
    import hljs from "highlight.js/lib/core";
    import "highlight.js/styles/atom-one-dark.css";
    import { storeHighlightJs } from "@skeletonlabs/skeleton";
 
    import json from "highlight.js/lib/languages/json";
 
    hljs.registerLanguage("json", json);
 
    storeHighlightJs.set(hljs);
    const code = 
    `"minecraft:entity_spawned": {
    "queue_command": {
        "command": ["tag @s add QGenQuest_{NAME_OF_YOUR_FIRST_QUEST}"]
    }
},`;
</script>

<div class="grid sm:grid-cols-2 sm:grid-rows-4 gap-10 w-2/3 mx-auto">
    <div>
        <h1 class="text-xl font-bold">1. Create your NPC</h1>
        <p>
            Every questline needs an NPC. You can create a new NPC at the Editor page. Just go to the Editor page and click on the "Editor" button. <br> Then fill out the form and click on "Start".
            It's important that the namespace and identifier match the namespace and identifier of the NPC in your behavior pack. 
        </p>
    </div>
    <img src="/createNpc.png" alt="createNpc" class="h-[auto] w-[80%] rounded-md" />
    <div>
        <h2 class="text-xl font-bold">2. Create your Questline</h2>
        <p>
            After you created your NPC you can create a new questline. Another form should appear after you created your NPC. You don't have to fill out the entire form, you can leave either the item or the tag conditions/reward empty. 
            Add as many elements to the quest as you want. You can also add as many quests to the questline as you want.
        </p>
    </div>
    <img src="/fillOutForm.png" alt="fillOutForm" class="h-[auto] w-[80%] rounded-md" />
    <div>
        <h3 class="text-xl font-bold">3. Get your generated Code</h3>
        <p>
            When you are done with your questline you can click on the "Generate" button. This will generate a code that you can add to your NPC. <br> Another page will open with the generated code that can either be copied or downloaded.
        </p>
    </div>
    <div></div>
    <div>
        <h4 class="text-xl font-bold">4. Add event to the NPC</h4>
        <p>
            For the last step you have to add an event to your NPC. You can do this by opening the NPC file in your behavior pack and adding this to the NPCs events.
        </p>
    </div>
    <CodeBlock
        language="json"
        code={code}
        background="bg-neutral-900/50"
    ></CodeBlock>
</div>
<div class="w-2/3 mx-auto mb-12">
    <h5 class="text-xl font-bold">Disclaimer</h5>
    <p>
        As of Minecraft Bedrock Version 1.20.62 this generator needs the 'Beta-APIs' to be activated. This also means that scripting needs to be enabled in the manifest.json file. This is a limitation of the game and not the generator.
    </p>
</div>