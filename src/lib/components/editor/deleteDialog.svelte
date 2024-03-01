<script lang="ts">
    import { AlertDialog } from "bits-ui";
    import { flyAndScale } from "$lib/utils/transitions";
    import { fade } from "svelte/transition";
    import { Trash2 } from "lucide-svelte";
    import { QuestLine } from "$lib/data";

    export let quest: QuestLine;
    export let updateData: (quest: QuestLine) => void;
</script>

<AlertDialog.Root>
    <AlertDialog.Trigger class="flex justify-center items-center mx-3 w-8 h-8 text-red-700 rounded-md hover:bg-neutral-800 opacity-20 hover:opacity-100 .add-button-hover">
        <Trash2 size={20} strokeWidth={3} />
    </AlertDialog.Trigger>
    <AlertDialog.Portal>
        <AlertDialog.Overlay
            transition={fade}
            transitionConfig={{ duration: 150 }}
            class="fixed inset-0 z-50 bg-black/80"
        />
        <AlertDialog.Content
            transition={flyAndScale}
            class="fixed left-[50%] top-[50%] z-50 grid w-full max-w-[94%] translate-x-[-50%] translate-y-[-50%] gap-4 rounded-md bg-neutral-900 p-7 shadow-popover outline-none sm:max-w-lg md:w-full"
        >
            <div class="flex flex-col gap-4 pb-6">
                <AlertDialog.Title class="text-lg font-semibold tracking-tight"
                    >Confirm your deletion</AlertDialog.Title
                >
                <AlertDialog.Description class="text-sm text-foreground-alt">
                    This action cannot be undone. This will permanently delete this questline. Do you wish to contionue?
                </AlertDialog.Description>
            </div>
            <div class="flex w-full items-center justify-center gap-2">
                <AlertDialog.Cancel
                    class="inline-flex h-10 w-full items-center justify-center self-center rounded-md opacity-20 hover:opacity-100 add-button-hover
                    bg-neutral-800 border-emerald-600 border-2 shadow-md shadow-emerald-600/50 hover:bg-neutral-700/50"
                    >Cancel</AlertDialog.Cancel
                >
                <AlertDialog.Action on:click={() => updateData(quest)}
                    class="inline-flex h-10 w-full items-center justify-center self-center rounded-md
                    bg-neutral-800 border-emerald-600 border-2 shadow-md shadow-emerald-600/50 hover:bg-neutral-700/50"
                    >Continue</AlertDialog.Action
                >
            </div>
        </AlertDialog.Content>
    </AlertDialog.Portal>
</AlertDialog.Root>
