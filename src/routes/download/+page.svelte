<script lang="ts">
    import NavBar from "$lib/components/navBar.svelte";
    import Footer from "$lib/components/footer.svelte";
    import { CodeBlock } from "@skeletonlabs/skeleton";
    import hljs from "highlight.js/lib/core";
    import "highlight.js/styles/atom-one-dark.css";
    import { storeHighlightJs } from "@skeletonlabs/skeleton";

    import javascript from "highlight.js/lib/languages/javascript";
    import json from "highlight.js/lib/languages/json";

    hljs.registerLanguage("json", json);
    hljs.registerLanguage("javascript", javascript);

    storeHighlightJs.set(hljs);

    
    let code2 = `{
   "format_version":"1.17.100",
   "minecraft:npc_dialogue":{
      "scenes":[
         {
            "scene_tag":"QGenQuest_test.intro00",
            "npc_name":{
               "rawtext":[
                  {
                     "translate":"entity.pb:hugo.name"
                  }
               ]
            },
            "text":{
               "rawtext":[
                  {
                     "translate":"dialogue.hugo_intro00"
                  }
               ]
            },
            "on_open_commands":[
               "/playsound mob.villager.yes @initiator"
            ],
            "buttons":[
               {
                  "name":{
                     "rawtext":[
                        {
                           "translate":"dialogue.ok"
                        }
                     ]
                  },
                  "commands":[
                     "/dialogue open @s @initiator QGenQuest_test.intro01"
                  ]
               },
               {
                  "name":{
                     "rawtext":[
                        {
                           "translate":"dialogue.bye"
                        }
                     ]
                  },
                  "commands":[
                     
                  ]
               }
            ]
         },
         {
            "scene_tag":"QGenQuest_test.intro01",
            "npc_name":{
               "rawtext":[
                  {
                     "translate":"entity.pb:hugo.name"
                  }
               ]
            },
            "text":{
               "rawtext":[
                  {
                     "translate":"dialogue.hugo_intro01"
                  }
               ]
            },
            "on_open_commands":[
               "/playsound mob.villager.yes @initiator"
            ],
            "on_close_commands":[
               "/tag @s add notFinished",
               "/tag @a[tag=host] add QGenQuest_test",
               "/function showQuest"
            ],
            "buttons":[
               {
                  "name":{
                     "rawtext":[
                        {
                           "translate":"dialogue.bye"
                        }
                     ]
                  },
                  "commands":[
                     
                  ]
               }
            ]
         },
         {
            "scene_tag":"QGenQuest_test.notFinished00",
            "npc_name":{
               "rawtext":[
                  {
                     "translate":"entity.pb:hugo.name"
                  }
               ]
            },
            "text":{
               "rawtext":[
                  {
                     "translate":"dialogue.hugo_notFinished00"
                  }
               ]
            },
            "on_open_commands":[
               "/playsound mob.villager.yes @initiator"
            ],
            "buttons":[
               {
                  "name":{
                     "rawtext":[
                        {
                           "translate":"dialogue.give_items"
                        }
                     ]
                  },
                  "commands":[
                     "/scriptevent pb:checkConditions"
                  ]
               },
               {
                  "name":{
                     "rawtext":[
                        {
                           "translate":"dialogue.ok"
                        }
                     ]
                  },
                  "commands":[
                     "/dialogue open @s @initiator QGenQuest_test.notFinished01"
                  ]
               },
               {
                  "name":{
                     "rawtext":[
                        {
                           "translate":"dialogue.bye"
                        }
                     ]
                  },
                  "commands":[
                     
                  ]
               }
            ]
         },
         {
            "scene_tag":"QGenQuest_test.notFinished01",
            "npc_name":{
               "rawtext":[
                  {
                     "translate":"entity.pb:hugo.name"
                  }
               ]
            },
            "text":{
               "rawtext":[
                  {
                     "translate":"dialogue.hugo_notFinished01"
                  }
               ]
            },
            "on_open_commands":[
               "/playsound mob.villager.yes @initiator"
            ],
            "buttons":[
               {
                  "name":{
                     "rawtext":[
                        {
                           "translate":"dialogue.give_items"
                        }
                     ]
                  },
                  "commands":[
                     "/scriptevent pb:checkConditions"
                  ]
               },
               {
                  "name":{
                     "rawtext":[
                        {
                           "translate":"dialogue.bye"
                        }
                     ]
                  },
                  "commands":[
                     
                  ]
               }
            ]
         },
         {
            "scene_tag":"QGenQuest_test.finished00",
            "npc_name":{
               "rawtext":[
                  {
                     "translate":"entity.pb:hugo.name"
                  }
               ]
            },
            "text":{
               "rawtext":[
                  {
                     "translate":"dialogue.hugo_finished00"
                  }
               ]
            },
            "on_open_commands":[
               "/playsound mob.villager.yes @initiator"
            ],
            "buttons":[
               {
                  "name":{
                     "rawtext":[
                        {
                           "translate":"dialogue.ok"
                        }
                     ]
                  },
                  "commands":[
                     "/dialogue open @s @initiator QGenQuest_test.finished01"
                  ]
               },
               {
                  "name":{
                     "rawtext":[
                        {
                           "translate":"dialogue.bye"
                        }
                     ]
                  },
                  "commands":[
                     
                  ]
               }
            ]
         },
         {
            "scene_tag":"QGenQuest_test.finished01",
            "npc_name":{
               "rawtext":[
                  {
                     "translate":"entity.pb:hugo.name"
                  }
               ]
            },
            "text":{
               "rawtext":[
                  {
                     "translate":"dialogue.hugo_finished01"
                  }
               ]
            },
            "on_open_commands":[
               "/playsound mob.villager.yes @initiator"
            ],
            "on_close_commands":[
               "/tag @s remove finished",
               "/tag @s remove QGenQuest_test",
               "/function hideQuest",
               "/tag @s add QGenQuest_test2"
            ],
            "buttons":[
               {
                  "name":{
                     "rawtext":[
                        {
                           "translate":"dialogue.bye"
                        }
                     ]
                  },
                  "commands":[
                     
                  ]
               }
            ]
         }
      ]
   }
}`

    const code = `export const QGenQuestConditions = [
        {
            name: "QGenQuest_test",
            conditions: [
                {
                    items: [
                        { id: "minecraft:apple", data: 0, amount: 5 },
                        { id: "minecraft:carrot", data: 0, amount: 5 },
                    ],
                },
            ],
            rewards: [
                {
                    items: [
                        { id: "minecraft:diamond", data: 0, amount: 1 },
                        { id: "minecraft:iron_ingot", data: 0, amount: 1 },
                    ],
                },
                { tags: ["svvsv"] },
            ],
            notFinishedTexts: 2,
        },
        {
            name: "QGenQuest_test2",
            conditions: [{ tags: ["huhhu"] }],
            rewards: [{ tags: ["lelelel"] }],
            notFinishedTexts: 2,
        },
    ];`;
</script>

<div class="">
    <NavBar />
    <div class="flex justify-center h-[70vh] mt-12 gap-2">
        <div class="w-1/3 h-96 overflow-y-auto rounded-md border-2 border-neutral-700 shadow-popover">
            <CodeBlock
                language="js"
                code={code}
                background="bg-neutral-800/50"
            ></CodeBlock>
        </div>
        <div class="w-1/3 h-96 overflow-y-auto rounded-md border-2 border-neutral-700 shadow-popover">
            <CodeBlock
                language="json"
                code={code2}
                background="bg-neutral-800/50"
            ></CodeBlock>
        </div>
    </div>
    <Footer />
</div>
