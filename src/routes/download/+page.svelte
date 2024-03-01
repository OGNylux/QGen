<script lang="ts">
    import NavBar from "$lib/components/navBar.svelte";
    import Footer from "$lib/components/footer.svelte";
    
    import { CodeBlock } from 'svhighlight';

    let code = `
    <CodeBlock
    language="svelte" 
    {code}
    showHeader={true}
    showLineNumbers={true}
/>
    `;

</script>

<div class="">
    <NavBar />
    ...
    <Footer/>
</div>