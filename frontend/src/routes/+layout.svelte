<script>
    import "../app.css";
    import { Toaster } from "$lib/components/ui/sonner";
    import NavBar from "$lib/components/navBar.svelte";
    import Footer from "$lib/components/footer.svelte";
</script>

<div class="bg-neutral-900 h-screen font-poppins text-white overflow-x-hidden">
    <Toaster />
    <slot />
</div>