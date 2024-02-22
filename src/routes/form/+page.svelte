<script lang="ts">
    import { Separator, Tabs } from "bits-ui";
    import { Github, HelpCircle, Home, Plus } from "lucide-svelte";
    import { onMount } from "svelte";
    import { reset } from "$lib/helper";
    import { QuestStore } from "$lib/store";
    import { QuestItem } from "$lib/data";
    import NavBar from "$lib/components/navBar.svelte";
    import FormsWrapper from "$lib/components/formsWrapper.svelte";

    onMount(() => {
        reset();
    });
</script>

<div class="h-full">
    <NavBar />
    <FormsWrapper />
</div>