<script lang="ts">
    import { onMount } from "svelte";
    import { reset } from "$lib/helper";
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