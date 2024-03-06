<script lang="ts">
    import NavBar from "$lib/components/navBar.svelte";
    import FormsWrapper from "$lib/components/form/formsWrapper.svelte";
    import Footer from "$lib/components/footer.svelte";
    import { QuestStore } from "$lib/store";
    import { newQuestLine } from "$lib/helper";
    import { goto } from "$app/navigation";

    if(!QuestStore.getQuestItems()) newQuestLine();
    if(QuestStore.getNPC().identifier === "") goto('/editor');
</script>

<div class="h-full">
    <NavBar />
    <div class="mb-4">
        <FormsWrapper />
    </div>
    <Footer/>
</div>