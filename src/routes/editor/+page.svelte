<script lang="ts">
    import { onMount } from "svelte";
    import { reset } from "$lib/helper";
    import NavBar from "$lib/components/navBar.svelte";
    import FormsWrapper from "$lib/components/form/formsWrapper.svelte";
    import Footer from "$lib/components/footer.svelte";
    import Vault from "$lib/components/vault.svelte";
    import EditorWrapper from "$lib/components/editorWrapper.svelte";

    onMount(() => {
    });
</script>

<div class="">
    <NavBar />
    <EditorWrapper />
    <Footer/>
</div>