<script lang="ts">
    import { onMount } from "svelte";
    import NavBar from "$lib/components/navBar.svelte";
    import Footer from "$lib/components/footer.svelte";
    import EditorWrapper from "$lib/components/editor/editorWrapper.svelte";

    onMount(() => {
    });
</script>

<div class="">
    <NavBar />
    <EditorWrapper />
    <Footer/>
</div>