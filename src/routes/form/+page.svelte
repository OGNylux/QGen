<script lang="ts">
    import { Separator } from "bits-ui";
    import { HelpCircle, Home, Plus } from "lucide-svelte";
    import { onMount } from "svelte";
    import { reset } from "../../helper";
    import { QuestStore } from "../../store";
    import { EmptyQuest } from "../../data";

    onMount(() => {
        reset();
    });

    function newQuest() {
        QuestStore.add(EmptyQuest);
    }

</script>

<div class="flex flex-row h-screen">
    <div class="flex flex-col items-center p-1.5 w-16 m-1 gap-2 rounded-2xl bg-slate-200">
        <button class="flex rounded-full justify-center items-center p-2 bg-slate-100 text-slate-700">
            <Home size={36}/>
        </button>
        <button class="flex rounded-full justify-center items-center p-2 bg-slate-100 text-slate-700">
            <HelpCircle size={36}/>
        </button>
        <Separator.Root orientation="horizontal" class="w-12 h-0.5 rounded-xl bg-slate-100" />
        {#each $QuestStore as _, i}
            <button class="flex rounded-full justify-center items-center p-2 bg-slate-100 text-slate-700">
                <span class="font-bold text-2xl p-0.5">Q{i + 1}</span>
            </button>   
        {/each}
        <button on:click={() => newQuest()} class="flex rounded-full justify-center items-center p-2 bg-slate-100 text-slate-700">
            <Plus size={36}/>
        </button>
    </div>
    <p class="text-4xl">This is the form page</p>
</div>