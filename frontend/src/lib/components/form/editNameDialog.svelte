<script lang="ts">
    import { QuestStore } from "$lib/store";
    import { flyAndScale } from "$lib/utils/transitions";
    import { Dialog, Separator } from "bits-ui";
    import { PencilRuler, X } from "lucide-svelte";
    import { fade } from "svelte/transition";

</script>

<Dialog.Root>
    <Dialog.Trigger
        class="flex items-center rounded-md p-1 opacity-0 group-hover:opacity-100 add-button-hover hover:bg-neutral-800 focus:outline-none text-emerald-600"
    >
        <PencilRuler />
    </Dialog.Trigger>
    <Dialog.Portal>
        <Dialog.Overlay
            transition={fade}
            transitionConfig={{ duration: 150 }}
            class="fixed inset-0 z-50 bg-black/60"
        />
        <Dialog.Content
            transition={flyAndScale}
            class="fixed left-[50%] top-[50%] z-50 w-full max-w-[94%] translate-x-[-50%] translate-y-[-50%] rounded-md bg-neutral-900 p-5 shadow-popover outline-none sm:max-w-[490px] md:w-full"
        >
            <Dialog.Title
                class="flex w-full items-center justify-center text-2xl"
            >
                Create an NPC
            </Dialog.Title>
            <Separator.Root
                class="mx-5 mb-6 mt-5 block h-0.5 rounded-xl bg-emerald-600"
            />
            <div class="flex flex-row items-start justify-center pb-11 gap-2">
                <div class="flex flex-col">
                    <span class="text-xl pb-1">Namespace</span>
                    <input
                        placeholder="minecraft"
                        class="block bg-neutral-800 w-28 rounded-md py-1.5 pl-3 pr-3 focus:outline-none focus:ring-2 focus:ring-emerald-600"
                        type="text"
                        bind:value={$QuestStore.npc.namespace}
                    />
                </div>
                <div class="flex flex-col grow">
                    <span class="text-xl pb-1">Identifier</span>
                    <input
                        placeholder="villager"
                        class="block bg-neutral-800 w-full rounded-md py-1.5 pl-3 pr-3 focus:outline-none focus:ring-2 focus:ring-emerald-600"
                        type="text"
                        bind:value={$QuestStore.npc.identifier}
                    />
                </div>
            </div>
            <div class="flex w-full justify-between gap-4">
                <Dialog.Close
                    class="flex items-center rounded-md py-1 w-full bg-neutral-800 border-emerald-600 border-2 hover:bg-neutral-700/50 focus:outline-none text-xl font-bold justify-center"
                >
                    Close
                </Dialog.Close>
                {#if $QuestStore.npc.identifier != "" && $QuestStore.npc.namespace != ""}
                    <Dialog.Close
                        class="flex items-center rounded-md py-1 w-full bg-neutral-800 border-emerald-600 border-2 hover:bg-neutral-700/50 focus:outline-none text-xl font-bold justify-center"
                    >
                        Save
                    </Dialog.Close>
                {:else}
                    <div
                        class="flex items-center rounded-md py-1 w-full bg-neutral-800 border-emerald-600/50 border-2 cursor-not-allowed text-muted-foreground text-xl font-bold justify-center"
                    >
                        Start
                    </div>
                {/if}
            </div>
            <Dialog.Close
                class="absolute right-5 top-5 rounded-md focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-foreground focus-visible:ring-offset-2 focus-visible:ring-offset-background active:scale-98"
            >
                <div>
                    <X class="size-5" />
                    <span class="sr-only">Close</span>
                </div>
            </Dialog.Close>
        </Dialog.Content>
    </Dialog.Portal>
</Dialog.Root>
