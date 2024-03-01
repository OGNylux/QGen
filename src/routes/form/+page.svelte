<script lang="ts">
    import NavBar from "$lib/components/navBar.svelte";
    import FormsWrapper from "$lib/components/form/formsWrapper.svelte";
    import Footer from "$lib/components/footer.svelte";
    import { QuestStore } from "$lib/store";
    import { newQuestLine } from "$lib/helper";

    if(!QuestStore.getQuestItems()) newQuestLine();
</script>

<div class="h-full">
    <NavBar />
    <FormsWrapper />
    <Footer/>
</div>