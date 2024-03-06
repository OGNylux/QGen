<script>
    import "../app.css";
    import { Toaster } from "$lib/components/ui/sonner";
    import NavBar from "$lib/components/navBar.svelte";
    import Footer from "$lib/components/footer.svelte";
</script>

<div id="top" class="bg-neutral-900 h-screen font-poppins text-white overflow-x-hidden">
    <Toaster />
    <NavBar />
    <div class="my-12">
        <slot />
    </div>
    <Footer/>
</div>