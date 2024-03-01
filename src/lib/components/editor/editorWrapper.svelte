<script>
    import { Tabs } from "bits-ui";
    import Vault from "./vault.svelte";
    import { Landmark } from "lucide-svelte";
    import EditorDialog from "./editorDialog.svelte";
</script>

<Tabs.Root value="vault" class="flex flex-row w-full h-full mb-20">
    <Tabs.List
        class="flex flex-col w-64 h-[512px] rounded-md bg-neutral-800 overflow-y-auto mt-32"
    >
        <div class="flex flex-col p-2 gap-1">
            <EditorDialog />
            <Tabs.Trigger value={"vault"}>
                <div
                    class="flex items-center rounded-md p-1 gap-1 bg-neutral-800 border-emerald-600 border-2 hover:bg-neutral-700/50"
                >
                    <Landmark />
                    <span class="text-lg font-bold">Vault</span>
                </div>
            </Tabs.Trigger>
        </div>
    </Tabs.List>
    <div class="w-full">
        <Tabs.Content value={"vault"} class="pt-10 px-4">
            <div class="w-5/6 ml-[72px]">
                <Vault />
            </div>
        </Tabs.Content>
    </div>
</Tabs.Root>
