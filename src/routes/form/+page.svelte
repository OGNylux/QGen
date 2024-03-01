<script lang="ts">
    import { onMount } from "svelte";
    import NavBar from "$lib/components/navBar.svelte";
    import FormsWrapper from "$lib/components/form/formsWrapper.svelte";
    import Footer from "$lib/components/footer.svelte";
    import { QuestStore } from "$lib/store";
    import { newQuest, newQuestLine } from "$lib/helper";
    import Form from "$lib/components/form/form.svelte";

    if(!QuestStore.getQuestItems()) newQuestLine();
    
</script>

<div class="h-full">
    <NavBar />
    <FormsWrapper />
    <Footer/>
</div>