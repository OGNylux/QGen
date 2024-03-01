<script>
    import { Tabs } from "bits-ui";
    import Vault from "./vault.svelte";
    import { Landmark, PencilRuler } from "lucide-svelte";
</script>

<Tabs.Root value="editor" class="flex flex-row w-full h-full mb-20">
    <Tabs.List
        class="flex flex-col w-64 h-[512px] rounded-lg bg-neutral-800 overflow-y-auto mt-32"
    >
        <div class="flex flex-col p-2 gap-1">
            <Tabs.Trigger value={"editor"}>
                <div
                    class="flex items-center rounded-lg p-1 gap-1 bg-neutral-800 border-emerald-600 border-2 hover:bg-neutral-700/50"
                >
                    <PencilRuler />
                    <span class="text-lg font-bold">Editor</span>
                </div>
            </Tabs.Trigger>
            <Tabs.Trigger value={"vault"}>
                <div
                    class="flex items-center rounded-lg p-1 gap-1 bg-neutral-800 border-emerald-600 border-2 hover:bg-neutral-700/50"
                >
                    <Landmark />
                    <span class="text-lg font-bold">Vault</span>
                </div>
            </Tabs.Trigger>
        </div>
    </Tabs.List>
    <div class="w-full">
        <Tabs.Content value={"editor"} class="pt-10 px-4">
            <span>hi</span>
        </Tabs.Content>
        <Tabs.Content value={"vault"} class="pt-10 px-4">
            <div class="w-5/6 mx-auto">
                <Vault />
            </div>
        </Tabs.Content>
    </div>
</Tabs.Root>
